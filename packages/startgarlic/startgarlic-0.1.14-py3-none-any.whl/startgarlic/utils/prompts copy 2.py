from typing import List, Dict

# AD_STYLES = {
#     "default": {
#         "prefix": "Ad: ",
#         "separator": " - ",
#         "format": "{prefix}{company_name}{separator}{description}"
#     }
# }

class PromptManager:
    def __init__(self):
        self.tracking_params = {
            "ref": "garlic",
            "utm_source": "garlic",
            "utm_medium": "llm_ad",
            "utm_campaign": "contextual"
        }

    def add_tracking_params(self, url: str, company_id: str = None) -> str:
        """Add tracking parameters to URL"""
        try:
            # Check if URL already has parameters
            separator = '&' if '?' in url else '?'
            
            # Add tracking parameters
            tracking_string = '&'.join([f"{k}={v}" for k, v in self.tracking_params.items()])
            
            # Add company ID if provided
            if company_id:
                tracking_string += f"&cid={company_id}"
                
            return f"{url}{separator}{tracking_string}"
        except Exception:
            return url

    def format_prompt(self, query: str, companies: List[dict], chat_history: List[dict] = None) -> str:
        """Format prompt with companies and chat history"""
        try:
            # Return just the styled ad if there's a relevant company
            if companies and len(companies) > 0:
                company = companies[0]
                if company.get('similarity', 0) > 0.3:
                    # Add tracking parameters to the website URL
                    tracked_url = self.add_tracking_params(
                        company['website'], 
                        company.get('id')
                    )
                    return f"Ad: {company['name']} @{tracked_url}"
            
            return ""

        except Exception as e:
            return ""

    def format_recommendation_prompt(self, query: str, main_response: str) -> str:
        """Format prompt for generating follow-up recommendations"""
        return f"""Based on this conversation:

        User Query: "{query}"
        Assistant Response: "{main_response}"

        Generate ONE natural follow-up suggestion that:
        - Adds value to the conversation
        - Relates to the user's interests
        - Encourages learning more
        - Feels like a natural continuation

        Format: Start with "💡" and make it sound conversational.
        Example: "💡 Have you considered exploring quantum computing's impact on cybersecurity? It's another fascinating application in finance!"
        """