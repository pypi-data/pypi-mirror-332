from .utils.database import DatabaseManager
from .utils.embeddings import EmbeddingManager
# from .utils.analytics import AnalyticsManager
from .utils.prompts import PromptManager
from .utils.auction import AuctionManager
from typing import List, Dict, Optional
# import numpy as np

class Garlic:
    def __init__(self, api_key: str):
        """Initialize RAG system with API key authentication"""
        if not api_key:
            raise ValueError("API key is required")
            
        try:
            # Initialize database first to verify API key
            self.db = DatabaseManager()
            
            # Clean up the API key
            api_key = api_key.strip().strip('"\'')
            
            # Verify API key (now returns tuple of validity and key_id)
            is_valid, self.key_id = self.db.verify_api_key(api_key)
            if not is_valid:
                raise ValueError("Invalid API key")
            
            # Initialize other managers only after successful authentication
            self.embedding_manager = EmbeddingManager()
            self.prompt_manager = PromptManager()
            self.auction_manager = AuctionManager()
            
            # Load companies data
            self.df = self.db.get_companies()
            # print(f"Loaded {len(self.df)} companies")
            
        except Exception as e:
            # print(f"Error initializing system: {e}")
            raise

    def find_similar_companies(self, query: str, top_k: int = 5) -> List[dict]:
        """Find companies similar to the query"""
        try:
            # print(f"Processing query: {query}")  # Debug print
            
            # Create query embedding
            query_embedding = self.embedding_manager.embed_query(query)
            
            if len(query_embedding) == 0:
                # print("Error: Failed to create query embedding")
                return []
            
            # print(f"Created query embedding of length {len(query_embedding)}")  # Debug print
            
            # Convert to list for Supabase
            query_embedding = query_embedding.tolist()
            
            # Get similar companies with scores
            results = self.db.search_similar_companies(query_embedding, top_k)
            
            if not results:
                # print("No similar companies found for query:", query)
                return []
            
            # print(f"Found {len(results)} companies:")  # Debug print
            for r in results:
                # print(f"- {r.get('name', 'Unknown')}: {r.get('similarity', 0):.2%}")
                pass
            
            return results
            
        except Exception as e:
            # print(f"Error finding similar companies: {e}")
            # print(f"Full error details: {str(e)}")  # More detailed error
            return []

    def generate_response(self, query: str, chat_history: Optional[List] = None) -> str:
        """Generate just the ad response"""
        try:
            # Get candidate companies
            candidates = self.find_similar_companies(query)
            
            # Select ad through auction mechanism
            selected_companies = self.auction_manager.select_ad(candidates)
            
            # Get the formatted ad
            ad_response = self.prompt_manager.format_prompt(query, selected_companies, chat_history)
            
            return ad_response

        except Exception as e:
            return ""

    def parse_response(self, response: Dict) -> Dict:
        """Parse the response into a clean format"""
        return {
            "query": response.get("query"),
            "response": response.get("response", ""),
            "recommendation": response.get("recommendation", ""),
            "companies": response.get("companies", [])
        }

    # def track_company_interaction(self, company_name: str, interaction_type: str = 'view'):
    #     """Track company interactions (view/access)"""
    #     try:
    #         if interaction_type == 'view':
    #             self.analytics.increment_views([{'name': company_name}])
    #         elif interaction_type == 'access':
    #             self.analytics.increment_access(company_name)
    #     except Exception as e:
    #         print(f"Error tracking interaction: {e}")

    # def get_company_analytics(self, company_name: str = None):
    #     """Get detailed analytics for a company"""
    #     return self.analytics.get_company_stats(company_name)

    # def get_trending_companies(self, days: int = 7, limit: int = 5):
    #     """Get trending companies"""
    #     return self.analytics.get_trending_companies(days, limit)
