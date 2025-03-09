import numpy as np
from typing import List, Dict

class AuctionManager:
    def __init__(self):
        """Initialize auction manager"""
        self.context_threshold = 0.3    # Minimum similarity threshold
        self.context_weight = 2.0       # Weight for context relevance
        self.min_bid = 0.1              # Minimum required bid
        
    def is_relevant(self, similarity: float) -> bool:
        """Determine if an ad is relevant based on context similarity"""
        return similarity >= self.context_threshold
        
    def has_valid_bid(self, bid: float) -> bool:
        """Check if bid meets minimum requirement"""
        return bid > 0
        
    def calculate_score(self, bid: float, similarity: float) -> float:
        """Calculate combined score for valid bids"""
        return bid * (similarity ** self.context_weight)
        
    def select_ad(self, companies: List[Dict]) -> List[Dict]:
        """Select ad based on auction mechanism and context relevance"""
        try:
            if not companies:
                return []
            
            # Extract similarities and bids
            candidates = [
                {
                    'company': company,
                    'similarity': company.get('similarity', 0),
                    'bid': company.get('bid', 0)
                }
                for company in companies
            ]
            
            # Filter for both relevance AND valid bids
            valid_candidates = [
                c for c in candidates 
                if self.is_relevant(c['similarity']) and self.has_valid_bid(c['bid'])
            ]
            
            # If no valid candidates, return empty
            if not valid_candidates:
                return []
                
            # Calculate scores for valid candidates
            for candidate in valid_candidates:
                candidate['score'] = self.calculate_score(
                    candidate['bid'],
                    candidate['similarity']
                )
            
            # Sort by combined score
            valid_candidates.sort(key=lambda x: x['score'], reverse=True)
            
            # Handle tie-breaking for equal scores
            top_score = valid_candidates[0]['score']
            top_candidates = [
                c for c in valid_candidates 
                if abs(c['score'] - top_score) < 1e-10
            ]
            
            # Random selection if multiple candidates have same score
            if len(top_candidates) > 1:
                selected = np.random.choice(top_candidates)
            else:
                selected = top_candidates[0]
                
            return [selected['company']]
            
        except Exception as e:
            print(f"Error in ad selection: {e}")
            return [] 