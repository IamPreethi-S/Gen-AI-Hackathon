# # src/Prompts/lead_generation_prompt.py

# lead_generation_prompt = """
# Analyze the following product information and create a comprehensive lead generation strategy:

# Product Details:
# - Name: {Product_Name}
# - Description: {Product_Description}
# - Category: {Product_Category}
# - Stage: {Product_Stage}
# - Target Audience: {Audience}
# - Region: {Region}
# - Pricing: {Pricing}
# - USP: {Unique_Selling_Points}
# - Goals: {Marketing_Goals}
# - Budget: {Budget_Range}

# Provide a detailed strategy including:
# 1. Lead Qualification Criteria
# 2. Target Account Profile
# 3. Channel Strategy
# 4. Content Recommendations
# 5. Outreach Templates
# 6. Follow-up Sequences
# 7. Lead Scoring Model
# 8. Conversion Optimization Tips

# Return the response in the following JSON format:
# {
#     "lead_generation_strategy": {
#         "qualification_criteria": [],
#         "target_profile": {},
#         "channels": [],
#         "content_plan": {},
#         "templates": [],
#         "follow_up": [],
#         "scoring_model": {},
#         "optimization_tips": []
#     }
# }
# """

# src/Prompts/lead_generation_prompt.py

lead_generation_prompt = """
Analyze the following product information and create a detailed B2B lead generation strategy:

Product Details:
- Name: {Product_Name}
- Description: {Product_Description}
- Category: {Product_Category}
- Stage: {Product_Stage}
- Target Audience: {Audience}
- Region: {Region}
- Pricing: {Pricing}
- USP: {Unique_Selling_Points}
- Goals: {Marketing_Goals}
- Budget: {Budget_Range}

Develop a comprehensive lead generation strategy focusing on:

1. Lead Qualification Framework:
- Define MQL and SQL criteria
- Set scoring thresholds
- Identify disqualification factors

2. Target Account Profile:
- Company size ranges
- Industry segments
- Technology stack requirements
- Budget indicators
- Decision-maker profiles

3. Channel Strategy:
- Primary lead sources
- Channel mix recommendations
- Budget allocation
- Expected CPL by channel

4. Content Strategy:
- Content types by funnel stage
- Distribution channels
- Engagement triggers
- Conversion assets

5. Outreach Plan:
- Email templates
- LinkedIn connection messages
- Follow-up sequences
- Timing recommendations

6. Lead Scoring Model:
- Demographic scores
- Behavioral scores
- Engagement scores
- Lead stage definitions

7. Conversion Optimization:
- Landing page recommendations
- Form optimization
- CTA suggestions
- A/B testing priorities

Return the response in the following JSON format:
{
    "lead_generation_strategy": {
        "qualification_framework": {
            "mql_criteria": [],
            "sql_criteria": [],
            "disqualification_factors": [],
            "scoring_thresholds": {}
        },
        "target_profile": {
            "company_size": [],
            "industries": [],
            "tech_requirements": [],
            "budget_range": "",
            "decision_makers": []
        },
        "channel_strategy": {
            "primary_channels": [],
            "budget_allocation": {},
            "expected_cpl": {},
            "channel_mix": []
        },
        "content_strategy": {
            "awareness_stage": [],
            "consideration_stage": [],
            "decision_stage": [],
            "distribution_plan": {}
        },
        "outreach_templates": {
            "email_templates": [],
            "linkedin_messages": [],
            "follow_up_sequences": [],
            "timing_guidelines": {}
        },
        "scoring_model": {
            "demographic_scoring": {},
            "behavioral_scoring": {},
            "engagement_scoring": {},
            "stage_definitions": {}
        },
        "conversion_optimization": {
            "landing_pages": [],
            "form_optimization": [],
            "cta_recommendations": [],
            "testing_priorities": []
        }
    }
}
"""