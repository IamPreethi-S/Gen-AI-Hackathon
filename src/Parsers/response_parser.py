# import json
# import re

# class ResponseParser:
#     def __init__(self, response_str):
#         self.response_str = response_str

#     def _parse_response(self):
#         """Helper method to extract JSON content using regex."""
#         # Regular expression to extract the JSON part from the response
#         json_match = re.search(r'<response>(.*?)</response>', self.response_str, re.DOTALL)
#         if json_match:
#             json_content = json_match.group(1).strip()
#             try:
#                 return json.loads(json_content)
#             except json.JSONDecodeError as e:
#                 print(f"Error decoding JSON: {e}")
#                 return None
#         else:
#             print("No valid JSON content found in the response.")
#             return None

#     def parse_instagram_post(self):
#         """Parse the response for an Instagram post."""
#         response_json = self._parse_response()
#         if response_json:
#             return {
#                 "action": response_json.get('action'),
#                 "content": response_json.get('response')
#             }
#         return None

#     def parse_linkedin_post(self):
#         """Parse the response for a LinkedIn post."""
#         response_json = self._parse_response()
#         if response_json:
#             return {
#                 "action": response_json.get('action'),
#                 "content": response_json.get('response')
#             }
#         return None

#     def parse_email_template(self):
#         """Parse the response for an email template."""
#         response_json = self._parse_response()
#         if response_json:
#             return {
#                 "action": response_json.get('action'),
#                 "content": response_json.get('response')
#             }
#         return None



# ```python
# response_parser.py
import json
import re
from typing import Dict, Any, Optional, List
from datetime import datetime

class LeadGenerationResponseParser:
    def __init__(self, response_str: str):
        self.response_str = response_str
        self.required_strategy_fields = [
            "qualification_framework",
            "target_profile",
            "channel_strategy",
            "content_strategy",
            "outreach_templates",
            "scoring_model",
            "conversion_optimization"
        ]

    def _parse_response(self) -> Optional[Dict[str, Any]]:
        """Extract and parse JSON content from response."""
        try:
            # First try to parse as direct JSON
            return json.loads(self.response_str)
        except json.JSONDecodeError:
            # Try to extract JSON from XML tags
            json_match = re.search(r'<response>(.*?)</response>', self.response_str, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1).strip())
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from XML tags: {e}")
                    return None
            else:
                print("No valid JSON content found in response.")
                return None

    def parse_lead_generation_strategy(self) -> Dict[str, Any]:
        """Parse comprehensive lead generation strategy."""
        response_json = self._parse_response()
        if not response_json:
            return self._generate_error_response("Invalid strategy response format")

        try:
            strategy = response_json.get('lead_generation_strategy', {})
            
            # Validate required fields
            missing_fields = [field for field in self.required_strategy_fields 
                            if field not in strategy]
            
            if missing_fields:
                return self._generate_error_response(
                    f"Missing required strategy fields: {', '.join(missing_fields)}"
                )

            return {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "strategy": {
                    "qualification_framework": strategy.get('qualification_framework', {}),
                    "target_profile": strategy.get('target_profile', {}),
                    "channel_strategy": strategy.get('channel_strategy', {}),
                    "content_strategy": strategy.get('content_strategy', {}),
                    "outreach_templates": strategy.get('outreach_templates', {}),
                    "scoring_model": strategy.get('scoring_model', {}),
                    "conversion_optimization": strategy.get('conversion_optimization', {})
                }
            }

        except Exception as e:
            return self._generate_error_response(f"Strategy parsing error: {str(e)}")

    def parse_lead_score(self) -> Dict[str, Any]:
        """Parse lead scoring response."""
        response_json = self._parse_response()
        if not response_json:
            return self._generate_error_response("Invalid lead score response format")

        try:
            score_data = response_json.get('lead_score', {})
            return {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "scoring_result": {
                    "total_score": score_data.get('lead_score', 0),
                    "qualification_status": score_data.get('qualification_status', ''),
                    "scoring_factors": score_data.get('scoring_factors', {}),
                    "recommendations": score_data.get('recommendations', []),
                    "next_actions": score_data.get('next_actions', [])
                }
            }
        except Exception as e:
            return self._generate_error_response(f"Lead score parsing error: {str(e)}")

    def parse_outreach_content(self) -> Dict[str, Any]:
        """Parse personalized outreach content."""
        response_json = self._parse_response()
        if not response_json:
            return self._generate_error_response("Invalid outreach content format")

        try:
            outreach_data = response_json
            return {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "outreach_content": {
                    "email_subject": outreach_data.get('email_subject', ''),
                    "email_body": outreach_data.get('email_body', ''),
                    "linkedin_message": outreach_data.get('linkedin_message', ''),
                    "follow_up_sequence": outreach_data.get('follow_up_sequence', []),
                    "call_scripts": outreach_data.get('call_scripts', [])
                }
            }
        except Exception as e:
            return self._generate_error_response(f"Outreach content parsing error: {str(e)}")

    def parse_nurture_campaign(self) -> Dict[str, Any]:
        """Parse nurture campaign response."""
        response_json = self._parse_response()
        if not response_json:
            return self._generate_error_response("Invalid nurture campaign format")

        try:
            campaign_data = response_json
            return {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "nurture_campaign": {
                    "campaign_strategy": campaign_data.get('campaign_strategy', {}),
                    "content_plan": campaign_data.get('content_plan', {}),
                    "automation_rules": campaign_data.get('automation_rules', {}),
                    "success_metrics": campaign_data.get('success_metrics', {})
                }
            }
        except Exception as e:
            return self._generate_error_response(f"Nurture campaign parsing error: {str(e)}")

    def validate_response_format(self, response_type: str) -> bool:
        """Validate response format based on type."""
        response_json = self._parse_response()
        if not response_json:
            return False

        validation_schemas = {
            'strategy': self.required_strategy_fields,
            'lead_score': ['lead_score', 'qualification_status', 'scoring_factors'],
            'outreach': ['email_subject', 'email_body', 'follow_up_sequence'],
            'nurture': ['campaign_strategy', 'content_plan', 'automation_rules']
        }

        required_fields = validation_schemas.get(response_type, [])
        if response_type == 'strategy':
            return all(field in response_json.get('lead_generation_strategy', {}) 
                      for field in required_fields)
        else:
            return all(field in response_json for field in required_fields)

    def _generate_error_response(self, error_message: str) -> Dict[str, Any]:
        """Generate standardized error response."""
        return {
            "timestamp": datetime.now().isoformat(),
            "status": "error",
            "error": error_message,
            "original_response": self.response_str[:200] + "..."  # Truncated for brevity
        }

    def format_response_for_database(self, parsed_response: Dict[str, Any]) -> Dict[str, Any]:
        """Format parsed response for database storage."""
        return {
            "timestamp": datetime.now().isoformat(),
            "response_type": self._determine_response_type(parsed_response),
            "content": parsed_response,
            "metadata": {
                "parser_version": "1.0",
                "validation_status": "valid" if parsed_response.get("status") == "success" else "invalid"
            }
        }

    def _determine_response_type(self, response: Dict[str, Any]) -> str:
        """Determine the type of response based on content."""
        if 'strategy' in response:
            return 'lead_generation_strategy'
        elif 'scoring_result' in response:
            return 'lead_score'
        elif 'outreach_content' in response:
            return 'outreach'
        elif 'nurture_campaign' in response:
            return 'nurture_campaign'
        else:
            return 'unknown'
# ```

# Example usage:

# ```python

# # Example usage
# def process_lead_generation_responses():
#     # Example strategy response
#     strategy_response = """
#     {
#         "lead_generation_strategy": {
#             "qualification_framework": {},
#             "target_profile": {},
#             "channel_strategy": {},
#             "content_strategy": {},
#             "outreach_templates": {},
#             "scoring_model": {},
#             "conversion_optimization": {}
#         }
#     }
#     """
    
#     # Parse strategy
#     parser = LeadGenerationResponseParser(strategy_response)
#     strategy_result = parser.parse_lead_generation_strategy()
    
#     if strategy_result["status"] == "success":
#         # Process successful response
#         print("Strategy parsed successfully:", strategy_result["strategy"])
#     else:
#         # Handle error
#         print("Error parsing strategy:", strategy_result["error"])

#     # Example lead score response
#     score_response = """
#     {
#         "lead_score": 85,
#         "qualification_status": "MQL",
#         "scoring_factors": {
#             "firmographic": {"score": 90, "factors": []},
#             "behavioral": {"score": 80, "factors": []},
#             "intent": {"score": 85, "factors": []}
#         }
#     }
#     """
    
#     # Parse lead score
#     parser = LeadGenerationResponseParser(score_response)
#     score_result = parser.parse_lead_score()
    
#     if score_result["status"] == "success":
#         print("Lead score parsed successfully:", score_result["scoring_result"])
#     else:
#         print("Error parsing lead score:", score_result["error"])

# # Run example
# if __name__ == "__main__":
#     process_lead_generation_responses()
# ```

# Key improvements:
# 1. Specialized parsing for lead generation responses
# 2. Structured validation for different response types
# 3. Error handling and reporting
# 4. Database-ready output formatting
# 5. Response type detection
# 6. Comprehensive validation schemas

# Would you like me to:
# 1. Add more validation rules?
# 2. Include additional response types?
# 3. Enhance error handling?
# 4. Add data transformation features?