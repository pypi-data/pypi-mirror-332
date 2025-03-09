from supabase import create_client, Client
import os
from dotenv import load_dotenv
from typing import Dict, List, Optional
from datetime import datetime
import pandas as pd
import numpy as np
from .config import get_credentials
# import bcrypt
import uuid

class DatabaseManager:
    def __init__(self):
        try:
            # Get credentials using existing config
            credentials = get_credentials()
            
            # Decode/decrypt the credentials here
            url = credentials.get("url")  
            key = credentials.get("key")
            self.supabase_url = url or os.getenv("SUPABASE_URL")
            self.supabase_key = key or os.getenv("SUPABASE_KEY")
            if not self.supabase_url or not self.supabase_key:
                raise ValueError("Missing Supabase credentials")
                
            # Make sure the key is clean (no quotes or whitespace)
            self.supabase_key = self.supabase_key.strip().strip('"\'')
            
            # Initialize Supabase client
            self.supabase = create_client(self.supabase_url, self.supabase_key)
            
            # print("Successfully connected to Supabase")
            
        except Exception as e:
            # print(f"Error initializing database: {e}")
            raise

    def get_companies(self):
        """Get all companies from ads table"""
        try:
            # Remove access from selection
            response = self.supabase.table('ads').select(
                'id, name, website, description, category, embedding, views'
            ).execute()
            
            # print(f"Retrieved {len(response.data)} companies")
            
            df = pd.DataFrame(response.data)
            
            # Check for records with null embeddings
            null_embeddings = df[df['embedding'].isna()]
            if not null_embeddings.empty:
                # print(f"Found {len(null_embeddings)} records without embeddings")
                embedding_columns = null_embeddings[['id', 'name', 'website', 'description', 'category']]
                self.update_missing_embeddings(embedding_columns)
                
                # Refresh data without access column
                response = self.supabase.table('ads').select(
                    'id, name, website, description, category, embedding, views'
                ).execute()
                df = pd.DataFrame(response.data)
            
            return df
            
        except Exception as e:
            # print(f"Error getting companies: {e}")
            return pd.DataFrame()

    def store_all_embeddings(self, companies: pd.DataFrame, embeddings: np.ndarray) -> bool:
        """Store embeddings directly in ads table"""
        try:
            for i, (_, company) in enumerate(companies.iterrows()):
                # Only update the embedding column
                self.supabase.table('ads').update({
                    'embedding': embeddings[i].tolist()
                }).eq('id', company['id']).execute()
                
            # print(f"Successfully stored {len(companies)} embeddings")
            return True
        except Exception as e:
            # print(f"Error storing embeddings: {e}")
            return False

    def search_similar_companies(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        """Search for similar companies using vector similarity"""
        try:
            # print(f"Searching for similar companies with embedding of length {len(query_embedding)}")  # Debug log
            
            # Get candidates for auction with debug logging
            # print("Executing database query...")  # Debug log
            response = self.supabase.rpc(
                'match_ads',
                {
                    'query_embedding': query_embedding,
                    'match_count': top_k,
                    'similarity_threshold': 0.1
                }
            ).execute()
            
            # print(f"Database response: {response.data}")  # Debug log
            
            if not response.data:
                # print("No companies found in database")  # Debug log
                return []
            
            # Prepare companies with similarities and bids
            results = []
            for item in response.data:
                if item.get('similarity', 0) > 0.3:  # Minimum similarity threshold
                    company = {
                        'id': item['id'],
                        'name': str(item['name']),
                        'website': str(item['website']) if item.get('website') else None,
                        'similarity': float(item['similarity']),
                        'bid': float(item['bid']) if item.get('bid') else 0.0
                    }
                    # print(f"Found company: {company}")  # Debug log
                    results.append(company)
            
            # print(f"Returning {len(results)} companies")  # Debug log
            return results
            
        except Exception as e:
            # print(f"Error searching similar companies: {e}")
            # print(f"Full error details: {str(e)}")
            return []

    def increment_views(self, companies: List[Dict]):
        """Increment view count for companies mentioned in response"""
        try:
            for company in companies:
                company_name = company.get('name', '')
                if not company_name:
                    continue
                    
                # print(f"Incrementing views for: {company_name}")  # Debug log
                
                # Get current views
                response = self.supabase.table('ads') \
                    .select('views') \
                    .eq('name', company_name) \
                    .execute()
                
                if response.data:
                    current_views = response.data[0].get('views', 0)
                    
                    # Update views count
                    update_response = self.supabase.table('ads') \
                        .update({'views': current_views + 1}) \
                        .eq('name', company_name) \
                        .execute()
                    
                    # print(f"Updated views for {company_name}: {current_views + 1}")  # Debug log
                    
                    # Log the view
                    self.insert_analytics_log(company_name, 'view')
                
            return True
            
        except Exception as e:
            # print(f"Error incrementing views: {e}")
            return False

    def insert_analytics_log(self, company_name: str, interaction_type: str = 'view'):
        """Insert analytics log for views"""
        try:
            if not company_name or not isinstance(company_name, str):
                return
            
            # print(f"Logging view for: {company_name}")  # Debug log
            
            self.supabase.table('analytics_logs').insert({
                'company_name': company_name,
                'interaction_type': interaction_type,
                'timestamp': datetime.now().isoformat()
            }).execute()
            
        except Exception as e:
            # print(f"Error inserting analytics log: {e}")
            pass  # Added pass statement

    def update_missing_embeddings(self, companies: pd.DataFrame):
        """Update embeddings for companies with null embeddings"""
        try:
            from .embeddings import EmbeddingManager
            embedding_manager = EmbeddingManager()
            
            # Create embeddings for companies
            embeddings = embedding_manager.create_embeddings(companies)
            
            # Update each company with its new embedding
            for i, (_, company) in enumerate(companies.iterrows()):
                self.supabase.table('ads').update({
                    'embedding': embeddings[i].tolist()
                }).eq('id', company['id']).execute()
                
            # print(f"Updated embeddings for {len(companies)} companies")
            
        except Exception as e:
            # print(f"Error updating missing embeddings: {e}")
            pass  # Added pass statement

    def verify_api_key(self, api_key: str) -> tuple[bool, Optional[str]]:
        """Verify API key and return validity and key ID"""
        try:
            # Query to verify key and get ID
            print(f"Verifying API key...")  # Debug print
            result = self.supabase.table('api_keys') \
                .select('id, key, revoked_at') \
                .eq('key', api_key) \
                .is_('revoked_at', 'null') \
                .execute()
            
            if result.data and len(result.data) > 0:
                key_id = result.data[0]['id']
                print(f"Found valid key with ID: {key_id}")  # Debug print
                # Update last_used timestamp
                self.update_key_last_used(key_id)
                return True, key_id
            print("No valid key found")  # Debug print
            return False, None
            
        except Exception as e:
            print(f"Error verifying API key: {e}")
            return False, None

    # def create_update_key_last_used_function(self):
    #     """Create the RPC function to update the last_used timestamp for an API key"""
    #     try:
    #         sql = """
    #         CREATE OR REPLACE FUNCTION update_key_last_used(key_value text)
    #         RETURNS void AS $$
    #         BEGIN
    #             UPDATE api_keys 
    #             SET last_used = NOW() 
    #             WHERE key = key_value 
    #             AND revoked_at IS NULL;
    #         END;
    #         $$ LANGUAGE plpgsql;
    #         """
            
    #         # Execute the SQL to create the function
    #         response = self.supabase.rpc('sql', {'query': sql}).execute()
            
    #         if response.error:
    #             print(f"Error creating function: {response.error}")
    #             return
            
    #         print("Function created successfully.")

    #     except Exception as e:
    #         print(f"Error creating function: {e}")

    def update_key_last_used(self, key_id: str):
        """Update the last_used timestamp for an API key"""
        try:
            print(f"Updating last_used for key {key_id}")

            # Call the function and get the updated row
            response = self.supabase.from_('api_keys') \
                .select('*') \
                .eq('id', key_id) \
                .single() \
                .execute()

            if not response.data:
                print("No key found")
                return False

            # Update using the function
            update_response = self.supabase.rpc(
                'update_api_key_last_used',
                {'api_key_id': key_id}
            ).execute()

            if hasattr(update_response, 'error') and update_response.error:
                print(f"Error updating last_used: {update_response.error}")
                return False

            print(f"Update successful: {update_response.data}")
            return True

        except Exception as e:
            print(f"Error updating key last_used: {e}")
            print(f"Full error details: {str(e)}")
            return False

