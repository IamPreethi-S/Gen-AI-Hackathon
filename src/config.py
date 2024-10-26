# # configjj.py
# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Load .env file
# load_dotenv()

# # Access API keys and DB connection
# ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
# MONGO_URI = os.getenv("MONGO_URI")
# ROOT_PATH = Path(__file__).parent.parent
# DATABASE_INFO = {
#   'db_username': 'genai',
#   'db_password': 'genai12345'
# }


# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Database Configuration
DATABASE_INFO = {
    'username': os.getenv('MONGODB_USERNAME', 'genaihackathon'),
    'password': os.getenv('MONGODB_PASSWORD', 'genai12345'),
    'cluster': 'leadgencluster.sanup.mongodb.net',
    'database': 'lead_generation'
}

# Root path
from pathlib import Path
ROOT_PATH = Path(__file__).parent
