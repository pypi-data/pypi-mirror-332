from typing import List, Dict

AD_STYLES = {
    "default": {
        "prefix": "Ad: ",
        "separator": " - ",
        "format": "{prefix}{company_name}{separator}{description}"
    }
}

class PromptManager:
    def format_prompt(self, query: str, companies: List[dict], chat_history: List[dict] = None, style="default") -> str:
        """Format prompt with companies and chat history"""
        try:
            if companies and len(companies) > 0:
                company = companies[0]
                if company.get('similarity', 0) > 0.3:
                    style_config = AD_STYLES.get(style, AD_STYLES["default"])
                    return style_config["format"].format(
                        prefix=style_config["prefix"],
                        company_name=company['name'],
                        separator=style_config["separator"],
                        description=company.get('description', 'Professional services')
                    )
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