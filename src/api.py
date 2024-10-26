# api.py
# from LLM.llm import generate_strategy
# from Parsers.response_parser import ResponseParser
# import re


from typing import Dict, Any, Optional
from LLM.llm import LeadGenerationLLM
from Parsers.response_parser import LeadGenerationResponseParser
from datetime import datetime
import json
import re

class LeadGenerationAPI:
    def __init__(self, db=None):
        self.llm = LeadGenerationLLM(db)
        self.db = db

    def generate_lead_strategy(self, 
                             product_name: str,
                             product_description: str,
                             product_category: str,
                             product_stage: str,
                             target_audience: str,
                             region: str,
                             product_pricing: str,
                             unique_selling_point: str,
                             marketing_goals: str,
                             budget_range: str) -> Dict[str, Any]:
        """
        Generate comprehensive lead generation strategy
        """
        try:
            # Generate strategy using LLM
            result = self.llm.generate_lead_strategy(
                product_name=product_name,
                product_description=product_description,
                product_category=product_category,
                product_stage=product_stage,
                target_audience=target_audience,
                region=region,
                product_pricing=product_pricing,
                unique_selling_point=unique_selling_point,
                marketing_goals=marketing_goals,
                budget_range=budget_range
            )

            # Clean response
            cleaned_result = self._clean_response(result)

            # Parse response
            parser = LeadGenerationResponseParser(cleaned_result)
            parsed_strategy = parser.parse_lead_generation_strategy()

            # Store in database if available
            if self.db and parsed_strategy.get('status') == 'success':
                self._store_strategy(parsed_strategy, product_name)

            return parsed_strategy

        except Exception as e:
            return self._generate_error_response(f"Strategy generation failed: {str(e)}")

    def analyze_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze and score a lead
        """
        try:
            # Generate lead analysis
            result = self.llm.score_lead(lead_data)
            cleaned_result = self._clean_response(result)

            # Parse response
            parser = LeadGenerationResponseParser(cleaned_result)
            parsed_analysis = parser.parse_lead_score()

            # Store analysis if database is available
            if self.db and parsed_analysis.get('status') == 'success':
                self._store_lead_analysis(parsed_analysis, lead_data.get('company_name'))

            return parsed_analysis

        except Exception as e:
            return self._generate_error_response(f"Lead analysis failed: {str(e)}")

    def generate_outreach_content(self, 
                                lead_data: Dict[str, Any], 
                                campaign_type: str = 'initial') -> Dict[str, Any]:
        """
        Generate personalized outreach content
        """
        try:
            # Generate outreach content
            result = self.llm.generate_personalized_outreach(lead_data, campaign_type)
            cleaned_result = self._clean_response(result)

            # Parse response
            parser = LeadGenerationResponseParser(cleaned_result)
            parsed_content = parser.parse_outreach_content()

            return parsed_content

        except Exception as e:
            return self._generate_error_response(f"Outreach content generation failed: {str(e)}")

    def create_nurture_campaign(self, 
                              lead_segment: str,
                              pain_points: list,
                              buying_stage: str) -> Dict[str, Any]:
        """
        Create lead nurture campaign
        """
        try:
            # Generate nurture campaign
            result = self.llm.create_nurture_campaign(
                lead_segment=lead_segment,
                pain_points=pain_points,
                buying_stage=buying_stage
            )
            cleaned_result = self._clean_response(result)

            # Parse response
            parser = LeadGenerationResponseParser(cleaned_result)
            parsed_campaign = parser.parse_nurture_campaign()

            return parsed_campaign

        except Exception as e:
            return self._generate_error_response(f"Nurture campaign creation failed: {str(e)}")

    def _clean_response(self, response: str) -> str:
        """
        Clean and format response string
        """
        if isinstance(response, dict):
            return json.dumps(response)
        
        # Remove special characters
        cleaned = re.sub(r'[\x00-\x1F\x7F]', '', response)
        # Remove extra whitespace
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned

    def _generate_error_response(self, error_message: str) -> Dict[str, Any]:
        """
        Generate standardized error response
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "error",
            "error": error_message
        }

    def _store_strategy(self, strategy: Dict[str, Any], product_name: str) -> None:
        """
        Store strategy in database
        """
        if self.db and hasattr(self.db, 'strategies'):
            try:
                self.db.strategies.insert_one({
                    "product_name": product_name,
                    "strategy": strategy,
                    "created_at": datetime.now().isoformat(),
                    "type": "lead_generation_strategy"
                })
            except Exception as e:
                print(f"Database storage error: {str(e)}")

    def _store_lead_analysis(self, analysis: Dict[str, Any], company_name: str) -> None:
        """
        Store lead analysis in database
        """
        if self.db and hasattr(self.db, 'lead_analyses'):
            try:
                self.db.lead_analyses.insert_one({
                    "company_name": company_name,
                    "analysis": analysis,
                    "created_at": datetime.now().isoformat(),
                    "type": "lead_analysis"
                })
            except Exception as e:
                print(f"Database storage error: {str(e)}")

if __name__ == "__main__":
    # Example usage
    lead_gen_api = LeadGenerationAPI()

    # Example product information
    product_info = {
        "product_name": "B2B Lead Gen Platform",
        "product_description": "AI-powered lead generation and qualification platform for B2B sales teams",
        "product_category": "SaaS",
        "product_stage": "Growth",
        "target_audience": "B2B Sales Teams, 50+ employees, Technology sector",
        "region": "North America",
        "product_pricing": "$500-$2000/month",
        "unique_selling_point": "AI-driven lead scoring with 95% accuracy",
        "marketing_goals": "Generate 200 qualified leads per month",
        "budget_range": "$50,000-$100,000"
    }

    # Generate strategy
    strategy_result = lead_gen_api.generate_lead_strategy(**product_info)
    print("\nGenerated Lead Generation Strategy:")
    print(json.dumps(strategy_result, indent=2))

    # Example lead analysis
    lead_data = {
        "company_name": "TechCorp Inc",
        "industry": "Software",
        "company_size": "500-1000",
        "budget": "$50k-$100k",
        "engagement_history": [
            "Downloaded whitepaper",
            "Attended webinar",
            "Viewed pricing page"
        ]
    }

    # Analyze lead
    lead_analysis = lead_gen_api.analyze_lead(lead_data)
    print("\nLead Analysis Result:")
    print(json.dumps(lead_analysis, indent=2))

    # Generate outreach content
    outreach_content = lead_gen_api.generate_outreach_content(lead_data)
    print("\nGenerated Outreach Content:")
    print(json.dumps(outreach_content, indent=2))
    
# ```

# Key improvements:
# 1. Dedicated lead generation API class
# 2. Comprehensive error handling
# 3. Response cleaning and formatting
# 4. Database integration
# 5. Structured response formats
# 6. Multiple lead generation functions
# 7. Example usage implementation

# To use this API:

# 1. Set up environment:
# ```python
# from api import LeadGenerationAPI
# ```

# 2. Initialize API:
# ```python
# lead_gen_api = LeadGenerationAPI()
# ```

# 3. Generate strategy:
# ```python
# strategy = lead_gen_api.generate_lead_strategy(
#     product_name="Your Product",
#     product_description="Description",
#     product_category="Category",
#     product_stage="Stage",
#     target_audience="Audience",
#     region="Region",
#     product_pricing="Pricing",
#     unique_selling_point="USP",
#     marketing_goals="Goals",
#     budget_range="Budget"
# )
# ```

# Would you like me to:
# 1. Add more API endpoints?
# 2. Enhance error handling?
# 3. Add validation layers?
# 4. Include authentication?


# if __name__ == "__main__":
#     product_name = "TexSneaks"
#     product_description = "TexSneaks offers trendy, high-quality, and eye-catching sneakers that are perfect for fashion-forward teenagers. With bold designs and vibrant colors, our shoes stand out from the crowd and help young people express their individuality. Our collection includes limited-edition drops and collaborations with local artists."
#     product_category = "Shoes"
#     product_stage = "Launch"
#     target_audience = "Teenagers aged 13-19, fashion-conscious, interested in streetwear, and looking for bold, statement shoes that reflect their unique personalities."
#     region = "Texas"
#     product_pricing = "Mid-range to high-end"
#     unique_selling_point = "No competition in market right now"
#     marketing_goals = "To sell 1000 pieces per day"
#     budget_range = "20 USD"

#     result = generate_strategy(
#         product_name,
#         product_description,
#         product_category,
#         product_stage,
#         target_audience,
#         region,
#         product_pricing,
#         unique_selling_point,
#         marketing_goals,
#         budget_range
#     )

#     print("Generated Market Strategy:")
#     print(result)

#     # result.replace("\n", "").replace("\t", "").replace("\r", "")
#     result=re.sub(r'[\x00-\x1F\x7F]', '', result)
#     parser = ResponseParser(result)
#     # parsed_linked_post= parser.parse_linkedin_post()
#     #parsed_instagram_post = parser.parse_instagram_post()
#     parsed_email = parser.parse_linkedin_post()


#     if parsed_email:
#         print("Parsed LinkedIn Post:")
#         print(f"Action: {parsed_email['action']}")
#         print(f"Content: {parsed_email['content']}")
