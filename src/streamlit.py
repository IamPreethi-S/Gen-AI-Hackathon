# from datetime import datetime

# import streamlit as st
# from pathlib import Path
# import json
# from Parsers.response_parser import ResponseParser
# import re
# from config import OPENAI_API_KEY, ROOT_PATH
# from database import MongoDBData
# import openai
# from dotenv import load_dotenv
# from Prompts.promptss import linkedin_post_creation_prompt, instagram_post_creation_prompt, email_template_prompt, \
#     channel_investment_guidance_prompt, detailed_stategy_development_prompt, digital_marketing_focus_prompt, \
#     generate_user_persona

# load_dotenv()  # Load environment variables
# openai.api_key = OPENAI_API_KEY
# # db = MongoDBData('prompt_db', 'input_prompt')


# if 'generated_history' not in st.session_state:
#     st.session_state['generated_history'] = []  # List to store previous responses

# # Function to generate marketing strategies
# def generate_strategy(product_name, product_description, product_category, product_stage, target_audience, region,
#                       product_pricing, unique_selling_point, marketing_goals, budget_range, prompts,persona_attributes):
#     results = {}

#     for prompt in prompts:

#         if prompt=="linkedin_post_creation_prompt":
#             test_prompt=linkedin_post_creation_prompt
#         elif prompt=="instagram_post_creation_prompt":
#             test_prompt=instagram_post_creation_prompt
#         elif prompt=="email_template_prompt":
#             test_prompt=email_template_prompt
#         elif prompt=="channel_investment_guidance_prompt":
#             test_prompt=channel_investment_guidance_prompt
#         elif prompt=="detailed_stategy_development_prompt":
#             test_prompt=detailed_stategy_development_prompt
#         elif prompt=="digital_marketing_focus_prompt":
#             test_prompt = digital_marketing_focus_prompt
#         else:
#             test_prompt = generate_user_persona

#         final_prompt = test_prompt.format(
#             Product_Name=product_name,
#             Product_Description=product_description,
#             Product_Category=product_category,
#             Product_Stage=product_stage,
#             Audience=target_audience,
#             Region=region,
#             Pricing=product_pricing,
#             Unique_Selling_Points=unique_selling_point,
#             Marketing_Goals=marketing_goals,
#             Budget_Range=budget_range
#         )
#         # print("final prommpt:",final_prompt)

#         messages = [

#             {"role": "system", "content": final_prompt},
#             {"role": "user", "content": "help me generate a marketing output for my Product"}
#         ]

#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=messages,
#             max_tokens=1500
#         )

#         # Clean and store the result
#         results[prompt] = re.sub(r'[\x00-\x1F\x7F]', '', response['choices'][0]['message']['content'])
#     return results


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css(Path(ROOT_PATH, 'src/css/style.css'))

# # Sidebar with logo
# st.sidebar.image("src/logo.png", use_column_width=True)
# st.sidebar.title("Marketing Strategy Generator")

# # History sidebar
# st.sidebar.subheader("History")
# if st.session_state['generated_history']:
#     for i, entry in enumerate(st.session_state['generated_history']):
#         if st.sidebar.button(f"Result {i + 1} - {entry['timestamp']}"):
#             st.write("## Previous Generated Results")
#             st.write(entry['content'])
# else:
#     st.sidebar.write("No history yet.")

# # Streamlit app title and description
# st.title("Marketing Strategy Generator")
# st.write('<p class="title-subtext">Generate marketing strategies for different platforms (Instagram, LinkedIn, Email) based on product details.</p><hr>', unsafe_allow_html=True)

# # Input fields for product details
# col1, col2 = st.columns(2)

# with col1:
#     product_name = st.text_input("Product Name", "TexSneaks", placeholder="Product Name")
#     st.write('<p class="input-example">Eg. TexSneaks</p>', unsafe_allow_html=True)

#     product_category = st.text_input("Product Category", "Shoes", placeholder="Product Category")
#     st.write('<p class="input-example">Eg. Shoes</p>', unsafe_allow_html=True)

#     product_stage = st.selectbox("Product Stage", ["Launch", "Growth", "Maturity", "Decline"], index=0)
#     st.write('<p class="input-example">Choose an option</p>', unsafe_allow_html=True)

# with col2:
#     product_description = st.text_area("Product Description",
#                                 "TexSneaks offers trendy, high-quality, and eye-catching sneakers that are perfect for fashion-forward teenagers.",
#                                 height=290)
    
# target_audience = st.text_area("Target Audience", "Teenagers aged 13-19, fashion-conscious, interested in streetwear.")

# col3, col4 = st.columns(2)

# with col3:
#     region = st.text_input("Region", "Texas")
#     st.write('<p class="input-example">Eg. Texas</p>', unsafe_allow_html=True)

#     product_pricing = st.text_input("Product Pricing", "Mid-range to high-end")
#     st.write('<p class="input-example">Eg. Mid-range to high-end</p>', unsafe_allow_html=True)

# with col4:
#     marketing_goals = st.text_input("Marketing Goals", "Increase brand awareness and sales.")
#     st.write('<p class="input-example">Eg. Increase brand awareness and sales</p>', unsafe_allow_html=True)

#     budget_range = st.text_input("Budget Range", "1000-5000")
#     st.write('<p class="input-example">Eg. 1000-5000</p>', unsafe_allow_html=True)

# unique_selling_point = st.text_input("Unique Selling Point", "Trendy and customizable designs.")
# st.write('<p class="input-example">Eg. Trendy and customizable designs</p><hr>', unsafe_allow_html=True)

# st.write("### Persona Details")

# # Input fields for product details
# col6, col7 = st.columns(2)

# with col6:
#     persona_gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0)
#     st.write('<p class="input-example">Eg. Male</p>', unsafe_allow_html=True)

# with col7:
#     persona_country = st.text_input("Country", "USA")
#     st.write('<p class="input-example">Eg. USA</p>', unsafe_allow_html=True)
    
# persona_age = st.text_input("Age", "25")
# st.write('<p class="input-example">Eg. 25</p>', unsafe_allow_html=True)

# persona_comments = st.text_area("Additional Comments", "The persona is tech-savvy and highly engaged on social media.")

# # Combine persona attributes into a dictionary
# persona_attributes = {
#     "gender": persona_gender,
#     "country": persona_country,
#     "age": persona_age,
#     "comments": persona_comments,
#     "product_category":product_category,
#     "product_description":product_description
# }

# st.write('<p class="multiselect-pretext">Select all the actions you want to include:</p>', unsafe_allow_html=True)
# action_choice = st.selectbox(
#     "Choose the action:",
#     options=["Generate Marketing Strategies", "Generate User Persona"]
# )

# available_prompts = {
#     'LinkedIn Post': "linkedin_post_creation_prompt",
#     'Instagram Post': "instagram_post_creation_prompt",
#     'Email Template': "email_template_prompt",
#     'Channel Guidance': "channel_investment_guidance_prompt",
#     'Detailed Strategy Development': "detailed_stategy_development_prompt",
#     'Digital Post': "digital_marketing_focus_prompt"
# }

# # Checkbox to select prompts
# selected_prompts = st.multiselect(
#     "Choose the marketing strategies to generate:",
#     options=["LinkedIn Post", "Instagram Post", "Email Template",
#             "Channel Investment Guidance", "Detailed Strategy Development",
#             "Digital Marketing Focus"],
#     default=["LinkedIn Post", "Instagram Post", "Email Template"]
# )
# st.write('<hr class="btn-separator">', unsafe_allow_html=True)

# # Generate button
# _, col8, _ = st.columns(3)
# if col8.button("Generate Analysis"):
#     if action_choice == "Generate Marketing Strategies":
#         if not selected_prompts:
#             selected_prompts = available_prompts.values()
#         else:
#             selected_prompts = [available_prompts[prompt] for prompt in selected_prompts]

#         results = generate_strategy(product_name, product_description, product_category, product_stage,
#                                     target_audience, region, product_pricing, unique_selling_point,
#                                     marketing_goals, budget_range, selected_prompts, persona_attributes)

#         st.session_state['generated_history'].append({
#             'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'content': results
#         })

#         st.write('<p class="output-title">Generated Marketing Strategies:</p>', unsafe_allow_html=True)
#         for prompt, result in results.items():
#             result = re.sub(r'[\x00-\x1F\x7F]', '', result)

#             # Remove leading/trailing tags
#             json_part = re.search(r'\{.*\}', result)
#             if json_part:
#                 result = json_part.group(0)

#             with st.expander(f"Click to Expand/Collapse details for {prompt.replace('_', ' ').title()}", expanded=False):
#                 st.subheader(f"Strategy for {prompt.replace('_', ' ').title()}:")
#                 parsed_result = eval(result)  # Assuming result is a JSON-like string

#                 # Display each part of the response in a structured manner
#                 if 'action' in parsed_result:
#                     st.write(f'<span class="highlight-text">Action</span>: {parsed_result["action"]}', unsafe_allow_html=True)
#                 if 'response' in parsed_result:
#                     st.write(f'<span class="highlight-text">Response</span>: {parsed_result["response"]}', unsafe_allow_html=True)
            
#         st.image("https://miro.medium.com/v2/resize:fit:1400/1*GugoFZUldUF6RncoKt_4Bw.png", caption="This is a AI generated image.",
#                  use_column_width=True)


#     elif action_choice == "Generate User Persona":
#         # Generate persona using the selected persona attributes
#         persona_prompt = generate_user_persona.format(**persona_attributes)

#         messages = [
#             {"role": "system", "content": persona_prompt},
#             {"role": "user", "content": "Generate a user persona"}
#         ]

#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=messages,
#             max_tokens=1500
#         )

#         persona_result = re.sub(r'[\x00-\x1F\x7F]', '', response['choices'][0]['message']['content'])
#         st.session_state['generated_history'].append({
#             'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'content': persona_result
#         })

#         try:
#             persona_result = json.loads(persona_result)  # Convert string to dictionary
#         except json.JSONDecodeError:
#             st.error("Error parsing the persona result. Please ensure it's in valid JSON format.")
#             persona_result = {}

#         # Append to session history if the result is valid
#         if persona_result:
#             st.session_state['generated_history'].append({
#                 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 'content': persona_result
#             })

#             # Display persona result
#             st.write("## Generated User Persona:")
#             st.write(persona_result)

#             # Emojis for different sections
#             emojis = ["✅", "🤔", "🎯", "🚀", "💡", "🔖"]

#             # Iterate over the persona result and display with corresponding emojis
#             for i, (key, value) in enumerate(persona_result.items()):
#                 if key != "Other options":  # Assuming you may have other options later
#                     st.write(f"{emojis[i]} **{key}**:")
#                     with st.expander(f"View details for {key}", expanded=False):
#                         st.write(value)
#                 else:
#                     # Handle "Other options" if needed
#                     st.write(f"{emojis[-1]} **{key}**:")
#                     st.write(persona_result[key])

# st.markdown("""
#     <style>
#     footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: #333;
#         color: white;
#         text-align: center;
#         padding: 10px;
#     }
#     </style>

#     <footer>
#         <p>© 2024 MarketIQ - All Rights Reserved</p>
#     </footer>
#     """, unsafe_allow_html=True)



# ```python

import streamlit as st
from pathlib import Path
import json
from datetime import datetime
from Parsers.response_parser import LeadGenerationResponseParser
from config import ANTHROPIC_API_KEY, ROOT_PATH
from database import MongoDBData
from LLM.llm import LeadGenerationLLM
from dotenv import load_dotenv

load_dotenv()

# # Initialize
# llm = LeadGenerationLLM(db=None)  # Initialize without DB for now

import streamlit as st
from database import MongoDBData
from LLM.llm import LeadGenerationLLM

# Initialize database connection with error handling
@st.cache_resource
def init_db():
    try:
        return MongoDBData()
    except Exception as e:
        st.error(f"Database connection failed: {str(e)}")
        return None

# Initialize database
db = init_db()

# Initialize LLM
llm = LeadGenerationLLM(db)

# Session State
if 'lead_history' not in st.session_state:
    st.session_state['lead_history'] = []
if 'current_lead' not in st.session_state:
    st.session_state['current_lead'] = None

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS
local_css(Path(ROOT_PATH, 'css/style.css'))

# Sidebar
with st.sidebar:
    st.image("logo.png", use_column_width=True)
    st.title("Lead Generation Hub")
    
    # Quick Stats
    st.subheader("📊 Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Leads", len(st.session_state['lead_history']))
    with col2:
        qualified_leads = sum(1 for lead in st.session_state['lead_history'] 
                            if lead.get('score', 0) > 70)
        st.metric("Qualified Leads", qualified_leads)
    
    # Lead History
    st.subheader("📝 Lead History")
    if st.session_state['lead_history']:
        for i, lead in enumerate(st.session_state['lead_history']):
            with st.expander(f"Lead #{i+1} - {lead.get('company_name', 'Unknown')}"):
                st.write(f"Score: {lead.get('score', 'N/A')}")
                st.write(f"Status: {lead.get('status', 'N/A')}")
                st.write(f"Created: {lead.get('timestamp', 'N/A')}")

# Main Content
st.title("LeadGen")


st.write("Generate, analyze, and nurture high-quality leads for your business.")

# Tabs for different functionalities
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Lead Generator",
    "📊 Lead Analyzer",
    "✉️ Outreach Manager",
    "🔄 Nurture Campaigns"
])

# with tab1:
#     st.header("Lead Generation Strategy")
    
#     # Company Information
#     with st.expander("🏢 Company Information", expanded=True):
#         col1, col2 = st.columns(2)
#         with col1:
#             company_name = st.text_input("Company Name", 
#                 help="Enter target company name")
#             industry = st.text_input("Industry",
#                 help="Company's primary industry")
#             company_size = st.select_slider("Company Size",
#                 options=["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"],
#                 help="Number of employees")
#         with col2:
#             region = st.text_input("Region",
#                 help="Geographic location")
#             budget = st.text_input("Estimated Budget",
#                 help="Annual budget for solutions")
#             decision_makers = st.text_input("Decision Makers",
#                 help="Key decision maker roles")

#     # Pain Points & Needs
#     with st.expander("🎯 Pain Points & Needs", expanded=True):
#         pain_points = st.multiselect("Pain Points",
#             ["Cost Efficiency", "Productivity", "Scalability", "Integration",
#              "Technical Support", "Training", "Customization"],
#             help="Select relevant pain points")
        
#         current_solutions = st.text_area("Current Solutions",
#             help="What solutions are they currently using?")
        
#         goals = st.text_area("Business Goals",
#             help="What are their primary business objectives?")

#     # Engagement History
#     with st.expander("📈 Engagement History", expanded=True):
#         engagement = st.multiselect("Previous Interactions",
#             ["Website Visit", "Content Download", "Email Open",
#              "Demo Request", "Meeting", "Pricing Page View"],
#             help="Select all relevant interactions")
        
#         last_contact = st.date_input("Last Contact Date",
#             help="When was the last interaction?")
        
#         engagement_score = st.slider("Engagement Score", 0, 100, 50,
#             help="Rate their engagement level")

#     if st.button("Generate Lead Strategy", type="primary"):
#         with st.spinner("Analyzing lead data and generating strategy..."):
#             try:
#                 lead_data = {
#                     "company_name": company_name,
#                     "industry": industry,
#                     "company_size": company_size,
#                     "region": region,
#                     "budget": budget,
#                     "decision_makers": decision_makers,
#                     "pain_points": pain_points,
#                     "current_solutions": current_solutions,
#                     "goals": goals,
#                     "engagement": engagement,
#                     "last_contact": str(last_contact),
#                     "engagement_score": engagement_score
#                 }

#                 # Generate strategy
#                 strategy = llm.generate_lead_strategy(
#                     product_name="Your Product",
#                     product_description="Your product description",
#                     product_category=industry,
#                     product_stage="Growth",
#                     target_audience=f"Companies in {industry} with {company_size} employees",
#                     region=region,
#                     product_pricing="Enterprise",
#                     unique_selling_point="Your USP",
#                     marketing_goals=f"Convert {company_name} into a qualified lead",
#                     budget_range=budget
#                 )

#                 if strategy:
#                     st.success("Strategy generated successfully!")
                    
#                     # Display Strategy
#                     with st.expander("📋 Lead Generation Strategy", expanded=True):
#                         # Qualification Framework
#                         st.subheader("Qualification Framework")
#                         col1, col2 = st.columns(2)
#                         with col1:
#                             st.markdown("**MQL Criteria:**")
#                             for criteria in strategy.get('qualification_framework', {}).get('mql_criteria', []):
#                                 st.write(f"• {criteria}")
#                         with col2:
#                             st.markdown("**SQL Criteria:**")
#                             for criteria in strategy.get('qualification_framework', {}).get('sql_criteria', []):
#                                 st.write(f"• {criteria}")

#                         # Channel Strategy
#                         st.subheader("Channel Strategy")
#                         channels = strategy.get('channel_strategy', {})
#                         st.json(channels)

#                         # Next Steps
#                         st.subheader("Recommended Next Steps")
#                         steps = strategy.get('next_steps', [])
#                         for i, step in enumerate(steps, 1):
#                             st.write(f"{i}. {step}")

#                     # Store in history
#                     st.session_state['lead_history'].append({
#                         'company_name': company_name,
#                         'strategy': strategy,
#                         'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                         'score': engagement_score,
#                         'status': 'New'
#                     })

#             except Exception as e:
#                 st.error(f"Error generating strategy: {str(e)}")


# with tab1:
#     st.header("Lead Generation Strategy")
    
#     # Product Information
#     with st.expander("🏢 Product Information", expanded=True):
#         col1, col2 = st.columns(2)
#         with col1:
#             product_name = st.text_input("Product Name", 
#                 value="RevenuePro CRM",
#                 help="Enter your product name")
#             product_category = st.text_input("Product Category",
#                 value="SaaS/CRM",
#                 help="E.g., SaaS, Hardware, Services")
#             product_stage = st.selectbox("Product Stage",
#                 options=["Launch", "Growth", "Maturity", "Decline"],
#                 help="Current stage of your product")
#         with col2:
#             product_description = st.text_area("Product Description",
#                 value="AI-powered customer relationship management platform designed for B2B sales teams.",
#                 help="Detailed description of your product")
#             product_pricing = st.text_input("Product Pricing",
#                 value="Tiered: $49-$199/user/month",
#                 help="Your pricing structure")

#     # Target Details
#     with st.expander("🎯 Target Market", expanded=True):
#         target_audience = st.text_area("Target Audience",
#             value="B2B sales teams in mid-market companies (50-500 employees)",
#             help="Describe your ideal customer profile")
        
#         col3, col4 = st.columns(2)
#         with col3:
#             region = st.text_input("Target Region",
#                 value="United States East Coast",
#                 help="Geographic focus area")
#         with col4:
#             budget_range = st.text_input("Marketing Budget",
#                 value="$25,000-$35,000 monthly",
#                 help="Available budget for lead generation")

#     # Strategic Elements
#     with st.expander("💡 Strategic Elements", expanded=True):
#         unique_selling_point = st.text_area("Unique Selling Points",
#             value="AI-powered sales forecasting with 95% accuracy, automated task prioritization",
#             help="What makes your product unique?")
        
#         marketing_goals = st.text_area("Marketing Goals",
#             value="- Acquire 200 new qualified leads per month\n- Achieve 30% trial-to-paid conversion",
#             help="Specific, measurable goals")

#     # Lead Qualification Criteria
#     with st.expander("📋 Lead Qualification", expanded=True):
#         col5, col6 = st.columns(2)
#         with col5:
#             company_size_range = st.select_slider("Target Company Size",
#                 options=["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"],
#                 value="51-200",
#                 help="Ideal company size")
#             decision_maker_roles = st.multiselect("Decision Maker Roles",
#                 ["CEO", "CTO", "Sales Director", "VP Sales", "IT Director"],
#                 default=["Sales Director", "VP Sales"],
#                 help="Key decision makers")
#         with col6:
#             min_budget = st.number_input("Minimum Budget Requirement",
#                 value=10000,
#                 help="Minimum customer budget")
#             tech_requirements = st.multiselect("Technical Requirements",
#                 ["CRM Integration", "API Access", "SSO", "Custom Development"],
#                 default=["CRM Integration"],
#                 help="Technical prerequisites")

#     if st.button("Generate Lead Strategy", type="primary"):
#         with st.spinner("Generating comprehensive lead generation strategy..."):
#             try:
#                 # Prepare strategy inputs
#                 strategy_input = {
#                     "product_name": product_name,
#                     "product_description": product_description,
#                     "product_category": product_category,
#                     "product_stage": product_stage,
#                     "target_audience": target_audience,
#                     "region": region,
#                     "product_pricing": product_pricing,
#                     "unique_selling_point": unique_selling_point,
#                     "marketing_goals": marketing_goals,
#                     "budget_range": budget_range
#                 }

#                 # Generate strategy using LLM
#                 strategy = llm.generate_lead_strategy(**strategy_input)

#                 if strategy:
#                     st.success("Lead generation strategy created successfully!")
                    
#                     # Display Strategy Components
#                     with st.expander("📊 Strategy Overview", expanded=True):
#                         # Lead Qualification Framework
#                         st.subheader("Lead Qualification Framework")
#                         col7, col8 = st.columns(2)
#                         with col7:
#                             st.markdown("**MQL Criteria**")
#                             qualification = strategy.get('qualification_framework', {})
#                             for criteria in qualification.get('mql_criteria', []):
#                                 st.write(f"• {criteria}")
#                         with col8:
#                             st.markdown("**SQL Criteria**")
#                             for criteria in qualification.get('sql_criteria', []):
#                                 st.write(f"• {criteria}")

#                         # Channel Strategy
#                         st.subheader("Channel Strategy")
#                         channels = strategy.get('channel_strategy', {})
#                         for channel, allocation in channels.get('budget_allocation', {}).items():
#                             st.progress(allocation/100)
#                             st.write(f"{channel}: {allocation}%")

#                         # Content Strategy
#                         st.subheader("Content Strategy")
#                         content = strategy.get('content_strategy', {})
#                         with st.expander("Content Plan"):
#                             for stage, content_items in content.items():
#                                 st.markdown(f"**{stage}**")
#                                 for item in content_items:
#                                     st.write(f"• {item}")

#                         # Outreach Templates
#                         st.subheader("Outreach Templates")
#                         templates = strategy.get('outreach_templates', {})
#                         with st.expander("Communication Templates"):
#                             for template_type, template in templates.items():
#                                 st.markdown(f"**{template_type}**")
#                                 st.text_area(f"{template_type} Template", 
#                                            value=template, 
#                                            height=100,
#                                            key=f"template_{template_type}")

#                     # Store in session state
#                     st.session_state['lead_history'].append({
#                         'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                         'strategy': strategy,
#                         'product_name': product_name,
#                         'status': 'New Strategy'
#                     })

#             except Exception as e:
#                 st.error(f"Error generating strategy: {str(e)}")


with tab1:
    st.header("Lead Generation Strategy")
    
    # Use columns for better organization
    col1, col2 = st.columns(2)
    
    with col1:
        # Product Information
        st.subheader("🏢 Product Information")
        product_name = st.text_input("Product Name", 
            value="RevenuePro CRM",
            help="Enter your product name")
        product_category = st.text_input("Product Category",
            value="SaaS/CRM",
            help="E.g., SaaS, Hardware, Services")
        product_stage = st.selectbox("Product Stage",
            options=["Launch", "Growth", "Maturity", "Decline"],
            help="Current stage of your product")
        product_description = st.text_area("Product Description",
            value="AI-powered customer relationship management platform designed for B2B sales teams.",
            help="Detailed description of your product")
        product_pricing = st.text_input("Product Pricing",
            value="Tiered: $49-$199/user/month",
            help="Your pricing structure")

    with col2:
        # Target Details
        st.subheader("🎯 Target Market")
        target_audience = st.text_area("Target Audience",
            value="B2B sales teams in mid-market companies (50-500 employees)",
            help="Describe your ideal customer profile")
        region = st.text_input("Target Region",
            value="United States East Coast",
            help="Geographic focus area")
        budget_range = st.text_input("Marketing Budget",
            value="$25,000-$35,000 monthly",
            help="Available budget for lead generation")
        
        # Strategic Elements
        st.subheader("💡 Strategic Elements")
        unique_selling_point = st.text_area("Unique Selling Points",
            value="AI-powered sales forecasting with 95% accuracy, automated task prioritization",
            help="What makes your product unique?")
        
        marketing_goals = st.text_area("Marketing Goals",
            value="- Acquire 200 new qualified leads per month\n- Achieve 30% trial-to-paid conversion",
            help="Specific, measurable goals")

    # Lead Qualification Criteria
    st.subheader("📋 Lead Qualification")
    qual_col1, qual_col2 = st.columns(2)
    
    with qual_col1:
        company_size_range = st.select_slider("Target Company Size",
            options=["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"],
            value="51-200",
            help="Ideal company size")
        decision_maker_roles = st.multiselect("Decision Maker Roles",
            ["CEO", "CTO", "Sales Director", "VP Sales", "IT Director"],
            default=["Sales Director", "VP Sales"],
            help="Key decision makers")
    
    with qual_col2:
        min_budget = st.number_input("Minimum Budget Requirement",
            value=10000,
            help="Minimum customer budget")
        tech_requirements = st.multiselect("Technical Requirements",
            ["CRM Integration", "API Access", "SSO", "Custom Development"],
            default=["CRM Integration"],
            help="Technical prerequisites")

    # Generate Strategy Button
    if st.button("Generate Lead Strategy", type="primary"):
        if 'lead_history' not in st.session_state:
            st.session_state['lead_history'] = []
        if 'current_lead' not in st.session_state:
            st.session_state['current_lead'] = None

        with st.spinner("Generating comprehensive lead generation strategy..."):
            try:
                # Prepare strategy inputs
                strategy_input = {
                    "product_name": product_name,
                    "product_description": product_description,
                    "product_category": product_category,
                    "product_stage": product_stage,
                    "target_audience": target_audience,
                    "region": region,
                    "product_pricing": product_pricing,
                    "unique_selling_point": unique_selling_point,
                    "marketing_goals": marketing_goals,
                    "budget_range": budget_range
                }

                # Generate strategy using LLM
                strategy = llm.generate_lead_strategy(**strategy_input)

                # if strategy:
                #     st.success("Lead generation strategy created successfully!")
                if strategy:
                    st.success("Lead generation strategy created successfully!")
    
                    # Store in session state with proper structure
                    lead_entry = {
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'strategy': strategy,
                        'product_name': product_name,
                        'company_name': product_name,  # Using product name as company name
                        'status': 'New Strategy',
                        'score': 0,  # Default score
                        'analysis': None  # Place for future analysis
                    }
                    st.session_state['lead_history'].append(lead_entry)
                                    
                    # Display Strategy Components
                    st.subheader("📊 Strategy Overview")
                    
                    # Tabs for different strategy components
                    strat_tab1, strat_tab2, strat_tab3, strat_tab4 = st.tabs([
                        "Qualification", "Channels", "Content", "Outreach"
                    ])
                    
                    with strat_tab1:
                        # Lead Qualification Framework
                        qual_col1, qual_col2 = st.columns(2)
                        with qual_col1:
                            st.markdown("**MQL Criteria**")
                            qualification = strategy.get('qualification_framework', {})
                            for criteria in qualification.get('mql_criteria', []):
                                st.write(f"• {criteria}")
                        with qual_col2:
                            st.markdown("**SQL Criteria**")
                            for criteria in qualification.get('sql_criteria', []):
                                st.write(f"• {criteria}")
                    
                    with strat_tab2:
                        # Channel Strategy
                        channels = strategy.get('channel_strategy', {})
                        for channel, allocation in channels.get('budget_allocation', {}).items():
                            st.progress(allocation/100)
                            st.write(f"{channel}: {allocation}%")
                    
                    with strat_tab3:
                        # Content Strategy
                        content = strategy.get('content_strategy', {})
                        for stage, content_items in content.items():
                            st.markdown(f"**{stage}**")
                            for item in content_items:
                                st.write(f"• {item}")
                    
                    with strat_tab4:
                        # Outreach Templates
                        templates = strategy.get('outreach_templates', {})
                        for template_type, template in templates.items():
                            st.markdown(f"**{template_type}**")
                            st.text_area(f"{template_type} Template", 
                                       value=template, 
                                       height=100,
                                       key=f"template_{template_type}")

                    # Store in session state
                    st.session_state['lead_history'].append({
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'strategy': strategy,
                        'product_name': product_name,
                        'status': 'New Strategy'
                    })

            except Exception as e:
                st.error(f"Error generating strategy: {str(e)}")


# with tab2:
#     st.header("Lead Analysis")
#     if st.session_state['lead_history']:
#         selected_lead = st.selectbox(
#             "Select Lead to Analyze",
#             options=[lead['company_name'] for lead in st.session_state['lead_history']]
#         )
        
#         if st.button("Analyze Lead"):
#             with st.spinner("Analyzing lead quality..."):
#                 lead_data = next(lead for lead in st.session_state['lead_history'] 
#                                if lead['company_name'] == selected_lead)
                
#                 analysis = llm.analyze_lead(lead_data)
#                 if analysis:
#                     # Display Analysis
#                     col1, col2, col3 = st.columns(3)
#                     with col1:
#                         st.metric("Lead Score", f"{analysis.get('score', 0)}/100")
#                     with col2:
#                         st.metric("Qualification", analysis.get('status', 'Unknown'))
#                     with col3:
#                         st.metric("Priority", analysis.get('priority', 'Medium'))
                    
#                     with st.expander("Detailed Analysis", expanded=True):
#                         st.json(analysis)

# with tab3:
#     st.header("Outreach Manager")
#     if st.session_state['lead_history']:
#         selected_lead = st.selectbox(
#             "Select Lead for Outreach",
#             options=[lead['company_name'] for lead in st.session_state['lead_history']],
#             key="outreach_lead"
#         )
        
#         campaign_type = st.selectbox(
#             "Campaign Type",
#             ["Initial Contact", "Follow Up", "Re-engagement"]
#         )
        
#         if st.button("Generate Outreach Content"):
#             with st.spinner("Generating personalized content..."):
#                 lead_data = next(lead for lead in st.session_state['lead_history'] 
#                                if lead['company_name'] == selected_lead)
                
#                 outreach = llm.generate_outreach_message(lead_data)
#                 if outreach:
#                     st.subheader("Generated Content")
                    
#                     # Email Content
#                     st.markdown("**Email Template**")
#                     st.text_input("Subject", outreach.get('email_subject', ''))
#                     st.text_area("Body", outreach.get('email_body', ''), height=200)
                    
#                     # LinkedIn Message
#                     st.markdown("**LinkedIn Message**")
#                     st.text_area("Message", outreach.get('linkedin_message', ''), height=100)

with tab2:
    st.header("Lead Analysis")
    if st.session_state['lead_history']:
        # Get company names safely
        lead_options = [
            lead.get('company_name', 'Unnamed Lead') 
            for lead in st.session_state['lead_history']
        ]
        
        selected_lead = st.selectbox(
            "Select Lead to Analyze",
            options=lead_options
        )
        
        if st.button("Analyze Lead"):
            with st.spinner("Analyzing lead quality..."):
                # Find selected lead safely
                selected_lead_data = next(
                    (lead for lead in st.session_state['lead_history'] 
                     if lead.get('company_name') == selected_lead),
                    None
                )
                
                if selected_lead_data:
                    analysis = llm.analyze_lead(selected_lead_data)
                    if analysis:
                        # Display Analysis
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric(
                                "Lead Score", 
                                f"{analysis.get('score', 0)}/100"
                            )
                        with col2:
                            st.metric(
                                "Qualification", 
                                analysis.get('status', 'Unknown')
                            )
                        with col3:
                            st.metric(
                                "Priority", 
                                analysis.get('priority', 'Medium')
                            )
                        
                        # Store analysis in lead history
                        for lead in st.session_state['lead_history']:
                            if lead.get('company_name') == selected_lead:
                                lead['analysis'] = analysis
                                lead['score'] = analysis.get('score', 0)
                        
                        st.subheader("Detailed Analysis")
                        st.json(analysis)
                else:
                    st.error("Selected lead not found in history")
    else:
        st.info("No leads available for analysis. Generate a lead strategy first.")

# Update tab3 (Outreach Manager)
with tab3:
    st.header("Outreach Manager")
    if st.session_state['lead_history']:
        lead_options = [
            lead.get('company_name', 'Unnamed Lead') 
            for lead in st.session_state['lead_history']
        ]
        
        selected_lead = st.selectbox(
            "Select Lead for Outreach",
            options=lead_options,
            key="outreach_lead"
        )
        
        campaign_type = st.selectbox(
            "Campaign Type",
            ["Initial Contact", "Follow Up", "Re-engagement"]
        )
        
        if st.button("Generate Outreach Content"):
            with st.spinner("Generating personalized content..."):
                selected_lead_data = next(
                    (lead for lead in st.session_state['lead_history'] 
                     if lead.get('company_name') == selected_lead),
                    None
                )
                
                if selected_lead_data:
                    outreach = llm.generate_outreach_message(selected_lead_data)
                    if outreach:
                        st.subheader("Generated Content")
                        
                        # Email Content
                        st.markdown("**Email Template**")
                        st.text_input(
                            "Subject", 
                            outreach.get('email_subject', '')
                        )
                        st.text_area(
                            "Body", 
                            outreach.get('email_body', ''), 
                            height=200
                        )
                        
                        # LinkedIn Message
                        st.markdown("**LinkedIn Message**")
                        st.text_area(
                            "Message", 
                            outreach.get('linkedin_message', ''), 
                            height=100
                        )
                else:
                    st.error("Selected lead not found")
    else:
        st.info("No leads available for outreach. Generate a lead strategy first.")

with tab4:
    st.header("Nurture Campaigns")
    
    campaign_name = st.text_input("Campaign Name")
    lead_segment = st.selectbox(
        "Lead Segment",
        ["Enterprise", "Mid-Market", "Small Business"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        buying_stage = st.selectbox(
            "Buying Stage",
            ["Awareness", "Consideration", "Decision"]
        )
    with col2:
        campaign_duration = st.selectbox(
            "Campaign Duration",
            ["2 weeks", "30 days", "60 days", "90 days"]
        )
    
    if st.button("Create Nurture Campaign"):
        with st.spinner("Creating nurture campaign..."):
            campaign = llm.create_nurture_campaign(
                lead_segment=lead_segment,
                pain_points=["Efficiency", "Cost", "Scale"],
                buying_stage=buying_stage
            )
            
            if campaign:
                st.success("Campaign created successfully!")
                with st.expander("Campaign Details", expanded=True):
                    st.json(campaign)

# Footer
st.markdown("""
    <footer>
        <p>© 2024 LeadGen </p>
    </footer>
    """, unsafe_allow_html=True)
# ```

# Key improvements:
# 1. Lead-specific interface
# 2. Comprehensive lead data collection
# 3. Strategy generation workflow
# 4. Lead analysis capabilities
# 5. Outreach management
# 6. Nurture campaign creation
# 7. Interactive dashboard
# 8. History tracking
# 9. Detailed analytics
# 10. Organized tabs

# Would you like me to:
# 1. Add more lead analysis features?
# 2. Enhance the visualization?
# 3. Add export capabilities?
# 4. Include more campaign templates?