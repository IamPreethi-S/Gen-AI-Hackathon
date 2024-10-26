# # llm.py
# from langchain_community.llms.openai import OpenAI
# from src.Prompts.prompts import post_creation_prompt
# from config import OPENAI_API_KEY
# import openai
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env

# openai.api_key = OPENAI_API_KEY

# class LLM:
#     def __init__(self, db):
#         self.db = db

# def generate_strategy(product_name, product_description, product_category, product_stage, target_audience, region,
#                       product_pricing,unique_selling_point,marketing_goals,budget_range):
#     # test_prompt = db.get_prompt_data()
#     test_prompt=post_creation_prompt
#     # print(test_prompt)

#     final_prompt = test_prompt.format(
#         Product_Name=product_name,
#         Product_Description=product_description,
#         Product_Category=product_category,
#         Product_Stage=product_stage,
#         Audience=target_audience,
#         Region=region,
#         Pricing=product_pricing,
#         Unique_Selling_Points = unique_selling_point,
#         Marketing_Goals = marketing_goals,
#         Budget_Range = budget_range
#     )

#     messages = [
#         {"role": "system", "content": final_prompt},
#         {"role": "user", "content": "help me generate a Channel Investment Guidelines for my Product"}
#     ]

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=messages,
#         max_tokens=1500
#     )

#     # Return the response content
#     return response['choices'][0]['message']['content']


# llm.py

# from anthropic import Anthropic
# from src.Prompts.prompts import post_creation_prompt, lead_generation_prompt
# from config import ANTHROPIC_API_KEY
# from typing import Dict, Any
# import json
# from dotenv import load_dotenv
# import asyncio

# load_dotenv()

# class LLM:
#     def __init__(self, db):
#         self.db = db
#         self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
#         self.model = "claude-3-opus-20240229"  # Using the latest Claude model

#     def generate_strategy(self, 
#                          product_name: str, 
#                          product_description: str, 
#                          product_category: str, 
#                          product_stage: str, 
#                          target_audience: str, 
#                          region: str,
#                          product_pricing: str,
#                          unique_selling_point: str,
#                          marketing_goals: str,
#                          budget_range: str) -> Dict[str, Any]:
#         """
#         Generate lead generation strategy using Claude AI
#         """
#         try:
#             # Combine prompts for lead generation
#             lead_prompt = lead_generation_prompt + post_creation_prompt

#             # Format the prompt with provided parameters
#             final_prompt = lead_prompt.format(
#                 Product_Name=product_name,
#                 Product_Description=product_description,
#                 Product_Category=product_category,
#                 Product_Stage=product_stage,
#                 Audience=target_audience,
#                 Region=region,
#                 Pricing=product_pricing,
#                 Unique_Selling_Points=unique_selling_point,
#                 Marketing_Goals=marketing_goals,
#                 Budget_Range=budget_range
#             )

#             # Create message for Claude
#             response = self.client.messages.create(
#                 model=self.model,
#                 max_tokens=3000,
#                 temperature=0.7,
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": "You are an expert lead generation strategist specializing in creating comprehensive marketing and lead generation strategies."
#                     },
#                     {
#                         "role": "user",
#                         "content": final_prompt
#                     }
#                 ]
#             )

#             # Process and structure the response
#             strategy = self._process_response(response.content)
            
#             # Store strategy in database if needed
#             if self.db:
#                 self._store_strategy(strategy)
            
#             return strategy

#         except Exception as e:
#             print(f"Error generating strategy: {str(e)}")
#             return {"error": str(e)}

#     async def generate_strategy_async(self, **kwargs) -> Dict[str, Any]:
#         """
#         Asynchronous version of generate_strategy for better performance
#         """
#         try:
#             # Create event loop and run the strategy generation
#             loop = asyncio.get_event_loop()
#             strategy = await loop.run_in_executor(None, 
#                                                 self.generate_strategy,
#                                                 kwargs.get('product_name'),
#                                                 kwargs.get('product_description'),
#                                                 kwargs.get('product_category'),
#                                                 kwargs.get('product_stage'),
#                                                 kwargs.get('target_audience'),
#                                                 kwargs.get('region'),
#                                                 kwargs.get('product_pricing'),
#                                                 kwargs.get('unique_selling_point'),
#                                                 kwargs.get('marketing_goals'),
#                                                 kwargs.get('budget_range'))
#             return strategy
#         except Exception as e:
#             print(f"Error in async strategy generation: {str(e)}")
#             return {"error": str(e)}

#     def analyze_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
#         """
#         Analyze lead quality and provide insights
#         """
#         try:
#             analysis_prompt = f"""
#             Analyze this lead information and provide detailed insights:
#             Company: {lead_data.get('company_name')}
#             Industry: {lead_data.get('industry')}
#             Size: {lead_data.get('company_size')}
#             Budget: {lead_data.get('budget')}
#             Engagement: {lead_data.get('engagement_history')}

#             Provide analysis including:
#             1. Lead score (0-100)
#             2. Qualification status
#             3. Recommended next actions
#             4. Potential challenges
#             5. Personalization suggestions
#             """

#             response = self.client.messages.create(
#                 model=self.model,
#                 max_tokens=1500,
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": "You are an expert lead analyst specializing in B2B lead qualification and scoring."
#                     },
#                     {
#                         "role": "user",
#                         "content": analysis_prompt
#                     }
#                 ]
#             )

#             return self._process_response(response.content)

#         except Exception as e:
#             print(f"Error analyzing lead: {str(e)}")
#             return {"error": str(e)}

#     def generate_outreach_message(self, lead_data: Dict[str, Any]) -> str:
#         """
#         Generate personalized outreach message for a lead
#         """
#         try:
#             message_prompt = f"""
#             Create a personalized outreach message for this lead:
#             Company: {lead_data.get('company_name')}
#             Industry: {lead_data.get('industry')}
#             Pain Points: {lead_data.get('pain_points')}
#             Previous Interactions: {lead_data.get('interactions')}

#             The message should:
#             1. Be personalized and relevant
#             2. Address specific pain points
#             3. Include clear value proposition
#             4. Have a compelling call to action
#             """

#             response = self.client.messages.create(
#                 model=self.model,
#                 max_tokens=1000,
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": "You are an expert sales copywriter specializing in B2B outreach."
#                     },
#                     {
#                         "role": "user",
#                         "content": message_prompt
#                     }
#                 ]
#             )

#             return response.content

#         except Exception as e:
#             print(f"Error generating outreach message: {str(e)}")
#             return f"Error: {str(e)}"

#     def _process_response(self, response: str) -> Dict[str, Any]:
#         """
#         Process and structure the AI response
#         """
#         try:
#             # Attempt to parse JSON response
#             if isinstance(response, str):
#                 return json.loads(response)
#             return response
#         except json.JSONDecodeError:
#             # If not JSON, return formatted dictionary
#             return {
#                 "content": response,
#                 "format": "text",
#                 "timestamp": asyncio.get_event_loop().time()
#             }

#     def _store_strategy(self, strategy: Dict[str, Any]) -> None:
#         """
#         Store strategy in database
#         """
#         if self.db and hasattr(self.db, 'strategies'):
#             try:
#                 self.db.strategies.insert_one({
#                     **strategy,
#                     "created_at": asyncio.get_event_loop().time()
#                 })
#             except Exception as e:
#                 print(f"Error storing strategy: {str(e)}")



# ```python

# llm.py
# from config import OPENAI_API_KEY
from anthropic import Anthropic
# import Anthropic
from Prompts.lead_generation_prompt import lead_generation_prompt
from config import ANTHROPIC_API_KEY
from typing import Dict, Any, List
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class LeadGenerationLLM:
    def __init__(self, db):
        self.db = db
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
        self.model = "claude-3-opus-20240229"

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
        Generate comprehensive B2B lead generation strategy
        """
        try:
            # Format the prompt with parameters
            final_prompt = lead_generation_prompt.format(
                Product_Name=product_name,
                Product_Description=product_description,
                Product_Category=product_category,
                Product_Stage=product_stage,
                Audience=target_audience,
                Region=region,
                Pricing=product_pricing,
                Unique_Selling_Points=unique_selling_point,
                Marketing_Goals=marketing_goals,
                Budget_Range=budget_range
            )

            # Generate strategy using Claude
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.7,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert B2B lead generation strategist. Create detailed, actionable strategies focusing on lead qualification, scoring, and conversion optimization."
                    },
                    {
                        "role": "user",
                        "content": final_prompt
                    }
                ]
            )

            # Process and validate response
            strategy = self._process_strategy_response(response.content)
            
            # Store strategy if database is available
            if self.db:
                self._store_strategy(strategy, product_name)
            
            return strategy

        except Exception as e:
            print(f"Strategy generation error: {str(e)}")
            return {"error": "Strategy generation failed", "details": str(e)}

    def score_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Score and qualify a lead based on provided data
        """
        try:
            scoring_prompt = f"""
            Score and qualify this B2B lead:

            Company Information:
            - Name: {lead_data.get('company_name')}
            - Industry: {lead_data.get('industry')}
            - Size: {lead_data.get('company_size')}
            - Budget: {lead_data.get('budget')}

            Engagement Data:
            - Activities: {lead_data.get('engagement_history', [])}
            - Technology: {lead_data.get('tech_stack', [])}
            - Timeline: {lead_data.get('buying_timeline', 'Unknown')}

            Provide detailed lead scoring analysis in this JSON format:
            {{
                "lead_score": 0-100,
                "qualification_status": "MQL/SQL/Unqualified",
                "scoring_factors": {{
                    "firmographic": {{
                        "score": 0-100,
                        "factors": []
                    }},
                    "behavioral": {{
                        "score": 0-100,
                        "factors": []
                    }},
                    "intent": {{
                        "score": 0-100,
                        "factors": []
                    }}
                }},
                "recommendations": [],
                "next_actions": []
            }}
            """

            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert lead scoring analyst. Provide detailed scoring and qualification analysis."
                    },
                    {
                        "role": "user",
                        "content": scoring_prompt
                    }
                ]
            )

            return json.loads(response.content)

        except Exception as e:
            print(f"Lead scoring error: {str(e)}")
            return {"error": "Lead scoring failed", "details": str(e)}

    def generate_personalized_outreach(self, 
                                     lead_data: Dict[str, Any], 
                                     campaign_type: str = "initial") -> Dict[str, Any]:
        """
        Generate personalized outreach content for different campaign types
        """
        try:
            outreach_prompt = f"""
            Create personalized B2B outreach content for:

            Lead Information:
            - Company: {lead_data.get('company_name')}
            - Industry: {lead_data.get('industry')}
            - Pain Points: {lead_data.get('pain_points', [])}
            - Engagement: {lead_data.get('engagement_history', [])}
            
            Campaign Type: {campaign_type}

            Generate these outreach elements in JSON format:
            {{
                "email_subject": "Attention-grabbing subject line",
                "email_body": "Personalized email content",
                "linkedin_message": "LinkedIn connection/InMail message",
                "follow_up_sequence": [
                    {{
                        "timing": "When to send",
                        "message": "Follow-up content"
                    }}
                ],
                "call_scripts": [
                    {{
                        "scenario": "Opening/Follow-up/Discovery",
                        "script": "Call script content"
                    }}
                ]
            }}
            """

            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert B2B sales copywriter. Create compelling, personalized outreach content."
                    },
                    {
                        "role": "user",
                        "content": outreach_prompt
                    }
                ]
            )

            return json.loads(response.content)

        except Exception as e:
            print(f"Outreach generation error: {str(e)}")
            return {"error": "Outreach generation failed", "details": str(e)}

    def create_nurture_campaign(self, 
                              lead_segment: str,
                              pain_points: List[str],
                              buying_stage: str) -> Dict[str, Any]:
        """
        Create lead nurture campaign strategy and content
        """
        try:
            nurture_prompt = f"""
            Create a lead nurturing campaign for:
            
            Segment: {lead_segment}
            Pain Points: {pain_points}
            Buying Stage: {buying_stage}

            Provide nurture campaign strategy in JSON format:
            {{
                "campaign_strategy": {{
                    "objective": "",
                    "key_messages": [],
                    "content_sequence": [],
                    "engagement_triggers": []
                }},
                "content_plan": {{
                    "emails": [],
                    "content_offers": [],
                    "social_messages": []
                }},
                "automation_rules": {{
                    "triggers": [],
                    "actions": [],
                    "exit_criteria": []
                }},
                "success_metrics": {{
                    "kpis": [],
                    "targets": {{}}
                }}
            }}
            """

            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in lead nurturing and marketing automation."
                    },
                    {
                        "role": "user",
                        "content": nurture_prompt
                    }
                ]
            )

            return json.loads(response.content)

        except Exception as e:
            print(f"Nurture campaign error: {str(e)}")
            return {"error": "Nurture campaign creation failed", "details": str(e)}

    def _process_strategy_response(self, response: str) -> Dict[str, Any]:
        """
        Process and validate strategy response
        """
        try:
            if isinstance(response, str):
                strategy = json.loads(response)
                
                # Validate required fields
                required_fields = [
                    "qualification_framework",
                    "target_profile",
                    "channel_strategy",
                    "content_strategy",
                    "outreach_templates",
                    "scoring_model",
                    "conversion_optimization"
                ]
                
                if "lead_generation_strategy" not in strategy:
                    raise ValueError("Missing lead_generation_strategy in response")
                
                strategy_content = strategy["lead_generation_strategy"]
                missing_fields = [field for field in required_fields 
                                if field not in strategy_content]
                
                if missing_fields:
                    raise ValueError(f"Missing required fields: {missing_fields}")
                
                return strategy
            return response
            
        except json.JSONDecodeError:
            return {
                "content": response,
                "format": "text",
                "timestamp": datetime.now().isoformat()
            }

    def _store_strategy(self, strategy: Dict[str, Any], product_name: str) -> None:
        """
        Store strategy in database with metadata
        """
        if self.db and hasattr(self.db, 'strategies'):
            try:
                strategy_doc = {
                    "product_name": product_name,
                    "strategy": strategy,
                    "created_at": datetime.now().isoformat(),
                    "version": "1.0",
                    "status": "active"
                }
                self.db.strategies.insert_one(strategy_doc)
            except Exception as e:
                print(f"Database storage error: {str(e)}")

# # Example usage
# from llm import LeadGenerationLLM
# from your_database import Database

# # Initialize
# db = Database()  # Your database connection
# llm = LeadGenerationLLM(db)

# # Generate lead generation strategy
# strategy = llm.generate_lead_strategy(
#     product_name="B2B Lead Gen Platform",
#     product_description="AI-powered lead generation and scoring",
#     product_category="SaaS",
#     product_stage="Growth",
#     target_audience="B2B Sales Teams",
#     region="North America",
#     product_pricing="$500-$2000/month",
#     unique_selling_point="AI-driven lead scoring with 95% accuracy",
#     marketing_goals="200 MQLs per month",
#     budget_range="$50,000-$100,000"
# )

# # Score a lead
# lead_score = llm.score_lead({
#     "company_name": "TechCorp",
#     "industry": "Software",
#     "company_size": "500-1000",
#     "budget": "$50k-$100k",
#     "engagement_history": [
#         "Downloaded whitepaper",
#         "Attended webinar",
#         "Viewed pricing page"
#     ]
# })

# # Generate outreach content
# outreach = llm.generate_personalized_outreach({
#     "company_name": "TechCorp",
#     "industry": "Software",
#     "pain_points": ["Manual lead scoring", "Low conversion rates"],
#     "engagement_history": ["Downloaded ROI calculator"]
# })

# # Create nurture campaign
# nurture = llm.create_nurture_campaign(
#     lead_segment="Enterprise Software Companies",
#     pain_points=["Long sales cycles", "Lead quality"],
#     buying_stage="Consideration"
# )
# ```

# Key improvements:
# 1. Focused solely on B2B lead generation
# 2. Enhanced lead scoring system
# 3. Comprehensive outreach content generation
# 4. Nurture campaign creation
# 5. Improved response validation
# 6. Better error handling
# 7. Structured database storage

# Would you like me to:
# 1. Add more lead generation features?
# 2. Enhance the response validation?
# 3. Add tracking mechanisms?
# 4. Include A/B testing capabilities?