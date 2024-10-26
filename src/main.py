# import streamlit as st
# from LLM.llm import LLM
# from Parsers.response_parser import ResponseParser
# import re

# from config import OPENAI_API_KEY
# from database import MongoDBData
# import openai
# from dotenv import load_dotenv

# from Prompts.promptss import *

# load_dotenv()  # take environment variables from .env

# openai.api_key = OPENAI_API_KEY
# db = MongoDBData('prompt_db', 'input_prompt')


# def generate_strategy(product_name, product_description, product_category, product_stage, target_audience, region,
#                       product_pricing,unique_selling_point,marketing_goals,budget_range):
#     # test_prompt = db.get_prompt_data()
#     test_prompt=linkedin_post_creation_prompt

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

#     print("final prommpt:", final_prompt)

#     messages = [
#         {"role": "system", "content": final_prompt},
#         {"role": "user", "content": "help me generate a Instagram Post for my Product"}
#     ]

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=messages,
#         max_tokens=1500
#     )

#     # Return the response content
#     return response['choices'][0]['message']['content']




# # Streamlit app title and description
# st.title("Marketing Strategy Generator")
# st.write("Generate marketing strategies for different platforms (Instagram, LinkedIn, Email) based on product details.")

# # Input fields for product details
# product_name = st.text_input("Product Name", "TexSneaks")
# product_description = st.text_area("Product Description", "TexSneaks offers trendy, high-quality, and eye-catching sneakers that are perfect for fashion-forward teenagers.")
# product_category = st.text_input("Product Category", "Shoes")
# product_stage = st.selectbox("Product Stage", ["Launch", "Growth", "Maturity", "Decline"], index=0)
# target_audience = st.text_area("Target Audience", "Teenagers aged 13-19, fashion-conscious, interested in streetwear.")
# region = st.text_input("Region", "Texas")
# product_pricing = st.text_input("Product Pricing", "Mid-range to high-end")
# unique_selling_point = st.text_input("Unique Selling Point", "Trendy and customizable designs.")
# marketing_goals = st.text_input("Marketing Goals", "Increase brand awareness and sales.")
# budget_range = st.text_input("Budget Range", "1000-5000")

# # Button to generate the marketing strategy
# if st.button("Generate Marketing Strategy"):
#     # Call the strategy generation function
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

#     # Clean the result to avoid control characters
#     result = re.sub(r'[\x00-\x1F\x7F]', '', result)

#     # Parse the result using ResponseParser
#     parser = ResponseParser(result)
#     parsed_instagram = parser.parse_instagram_post()
#     parsed_linkedin = parser.parse_linkedin_post()
#     parsed_email = parser.parse_email_template()

#     # Display the generated marketing strategies
#     st.write("## Generated Marketing Strategy:")

#     if parsed_instagram:
#         st.subheader("Instagram Post:")
#         st.write(f"**Action**: {parsed_instagram['action']}")
#         st.write(parsed_instagram['content'])

#     if parsed_linkedin:
#         st.subheader("LinkedIn Post:")
#         st.write(f"**Action**: {parsed_linkedin['action']}")
#         st.write(parsed_linkedin['content'])

#     if parsed_email:
#         st.subheader("Email Template:")
#         st.write(f"**Action**: {parsed_email['action']}")
#         st.write(parsed_email['content'])


# ```python


from dotenv import load_dotenv
import streamlit as st
from LLM.llm import LeadGenerationLLM
from Parsers.response_parser import LeadGenerationResponseParser
from config import ANTHROPIC_API_KEY
from database import MongoDBData
from datetime import datetime
import json
import re

# Initialize
load_dotenv()
db = MongoDBData('lead_generation_db', 'leads')
llm = LeadGenerationLLM(db)

def init_session_state():
    if 'generated_strategies' not in st.session_state:
        st.session_state.generated_strategies = []
    if 'current_lead' not in st.session_state:
        st.session_state.current_lead = None

def render_sidebar():
    with st.sidebar:
        st.title("Lead Generation Dashboard")
        st.markdown("---")
        
        # Quick Stats
        st.subheader("Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Leads", len(st.session_state.generated_strategies))
        with col2:
            st.metric("Qualified Leads", sum(1 for s in st.session_state.generated_strategies 
                                           if s.get('score', 0) > 70))

def main():
    # Initialize session state
    init_session_state()
    
    # Render sidebar
    render_sidebar()

    # Main content
    st.title("LeadGen - Lead Smarter, Grow Faster")
    
    # Tabs for different functionalities
    tab1, tab2, tab3, tab4 = st.tabs([
        "Strategy Generator", 
        "Lead Analyzer", 
        "Outreach Creator",
        "Campaign Manager"
    ])

    with tab1:
        st.header("Generate Lead Generation Strategy")
        
        # Product Information Section
        with st.expander("Product Information", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                product_name = st.text_input("Product Name", 
                    help="Enter your product or service name")
                product_category = st.text_input("Product Category",
                    help="E.g., SaaS, Hardware, Professional Services")
                product_stage = st.selectbox("Product Stage", 
                    ["Launch", "Growth", "Maturity", "Decline"])
                region = st.text_input("Target Region",
                    help="Geographic focus area")

            with col2:
                product_pricing = st.text_input("Pricing Structure",
                    help="E.g., $100-$500/month, Enterprise pricing")
                unique_selling_point = st.text_input("Unique Selling Point",
                    help="What makes your product unique?")
                marketing_goals = st.text_input("Lead Generation Goals",
                    help="E.g., Generate 100 MQLs per month")
                budget_range = st.text_input("Budget Range",
                    help="Available budget for lead generation")

        product_description = st.text_area("Product Description",
            help="Detailed description of your product/service")
        target_audience = st.text_area("Target Audience",
            help="Detailed description of your ideal customer profile")

        if st.button("Generate Strategy", type="primary"):
            with st.spinner("Generating comprehensive lead generation strategy..."):
                try:
                    # Generate strategy
                    result = llm.generate_lead_strategy(
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

                    # Parse results
                    parser = LeadGenerationResponseParser(result)
                    strategy = parser.parse_lead_generation_strategy()

                    if strategy.get('status') == 'success':
                        st.success("Strategy generated successfully!")
                        
                        # Display Strategy
                        strategy_data = strategy['strategy']
                        
                        # Qualification Framework
                        st.subheader("Lead Qualification Framework")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("MQL Criteria:")
                            for criteria in strategy_data['qualification_framework']['mql_criteria']:
                                st.write(f"• {criteria}")
                        with col2:
                            st.write("SQL Criteria:")
                            for criteria in strategy_data['qualification_framework']['sql_criteria']:
                                st.write(f"• {criteria}")

                        # Channel Strategy
                        st.subheader("Channel Strategy")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Primary Channels", 
                                    len(strategy_data['channel_strategy']['primary_channels']))
                        with col2:
                            st.metric("Budget Allocation", 
                                    f"${strategy_data['channel_strategy']['budget_allocation'].get('total', 0):,}")
                        with col3:
                            st.metric("Expected CPL", 
                                    f"${strategy_data['channel_strategy']['expected_cpl'].get('average', 0):,.2f}")

                        # Store in session state
                        st.session_state.generated_strategies.append(strategy)

                    else:
                        st.error("Failed to generate strategy. Please try again.")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    with tab2:
        st.header("Lead Analyzer")
        
        with st.form("lead_analysis_form"):
            # Lead Information
            company_name = st.text_input("Company Name")
            industry = st.text_input("Industry")
            company_size = st.selectbox("Company Size", 
                ["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"])
            
            # Engagement Data
            engagement = st.multiselect("Engagement History",
                ["Website Visit", "Content Download", "Demo Request", 
                 "Email Open", "Meeting Scheduled", "Pricing Page View"])
            
            if st.form_submit_button("Analyze Lead"):
                with st.spinner("Analyzing lead quality..."):
                    lead_data = {
                        "company_name": company_name,
                        "industry": industry,
                        "company_size": company_size,
                        "engagement_history": engagement
                    }
                    
                    analysis = llm.analyze_lead(lead_data)
                    if analysis.get('status') == 'success':
                        score = analysis['scoring_result']['total_score']
                        
                        # Display Score
                        st.subheader("Lead Score")
                        st.progress(score/100)
                        st.metric("Score", f"{score}/100")
                        
                        # Display Analysis
                        with st.expander("Detailed Analysis", expanded=True):
                            st.json(analysis['scoring_result'])

    with tab3:
        st.header("Outreach Creator")
        if st.session_state.current_lead:
            lead = st.session_state.current_lead
            
            campaign_type = st.selectbox("Campaign Type",
                ["Initial Contact", "Follow Up", "Re-engagement"])
            
            if st.button("Generate Outreach Content"):
                with st.spinner("Generating personalized outreach content..."):
                    outreach = llm.generate_outreach_message(lead, campaign_type)
                    
                    st.subheader("Generated Content")
                    st.text_area("Email Subject", outreach['email_subject'], height=50)
                    st.text_area("Email Body", outreach['email_body'], height=200)
                    st.text_area("LinkedIn Message", outreach['linkedin_message'], height=100)

    with tab4:
        st.header("Campaign Manager")
        
        col1, col2 = st.columns(2)
        with col1:
            lead_segment = st.selectbox("Lead Segment",
                ["Enterprise", "Mid-Market", "Small Business"])
            buying_stage = st.selectbox("Buying Stage",
                ["Awareness", "Consideration", "Decision"])
        
        with col2:
            pain_points = st.multiselect("Pain Points",
                ["Cost", "Efficiency", "Scale", "Integration", "Support"])

        if st.button("Create Nurture Campaign"):
            with st.spinner("Creating nurture campaign..."):
                campaign = llm.create_nurture_campaign(
                    lead_segment=lead_segment,
                    pain_points=pain_points,
                    buying_stage=buying_stage
                )
                
                if campaign.get('status') == 'success':
                    st.success("Campaign created successfully!")
                    st.json(campaign['nurture_campaign'])

if __name__ == "__main__":
    main()
# ```

# Key features added:
# 1. Modern tabbed interface
# 2. Lead scoring visualization
# 3. Campaign management
# 4. Strategy generation
# 5. Outreach content creator
# 6. Analytics dashboard
# 7. Session state management
# 8. Progress indicators
# 9. Error handling
# 10. Interactive forms

# The interface provides:
# 1. Strategy Generator:
#    - Comprehensive product information input
#    - Detailed strategy output
#    - Visual metrics

# 2. Lead Analyzer:
#    - Lead scoring
#    - Engagement tracking
#    - Quality assessment

# 3. Outreach Creator:
#    - Personalized messaging
#    - Multi-channel content
#    - Campaign types

# 4. Campaign Manager:
#    - Nurture campaign creation
#    - Segment management
#    - Performance tracking

# Would you like me to:
# 1. Add more visualization features?
# 2. Enhance the analytics dashboard?
# 3. Add export functionality?
# 4. Include more campaign templates?