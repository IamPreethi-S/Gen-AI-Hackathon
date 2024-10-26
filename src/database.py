# from pathlib import Path
# import certifi
# from pymongo import MongoClient, DESCENDING
# from config import DATABASE_INFO, ROOT_PATH

# url = f'mongodb+srv://{DATABASE_INFO["genaihackathon"]}:{DATABASE_INFO["genai12345"]}@leadgencluster.sanup.mongodb.net/?retryWrites=true&w=majority&appName=LeadGenCluster'


# class MongoDBData:
#     def __init__(self, db_name, collection_name):
#         self.prompt_file = Path(ROOT_PATH, 'config/prompt.xml')
#         client = MongoClient(url, tlsCAFile=certifi.where())
#         self.collection = self.get_collection(client, db_name, collection_name)

#     @staticmethod
#     def get_collection(client, db_name, collection_name):
#         return client[db_name][collection_name]
    
#     def set_prompt_data(self):
#         with open(self.prompt_file, 'r') as f:
#             post_prompt_data = f.read()
#             self.collection.insert_one({
#                 'prompt': post_prompt_data,
#             })

#     def get_prompt_data(self, query = {}):
#         doc_count = self.collection.count_documents(query)
#         assert doc_count > 0, "No prompt data found in the database."
#         last_doc = self.collection.find(query).sort([('_id', DESCENDING)]).limit(1)[0]
#         assert 'prompt' in last_doc.keys(), "Prompt data not found."
#         return last_doc['prompt']

# if __name__ == '__main__':
#     db = MongoDBData('prompt_db', 'input_prompt')
#     # db.set_prompt_data()
#     print(db.get_prompt_data())


# database.py
import pymongo
from config import DATABASE_INFO

class MongoDBData:
    def __init__(self, database_name=None, collection_name=None):
        try:
            # Construct the MongoDB URI using the credentials
            self.url = f'mongodb+srv://{DATABASE_INFO["username"]}:{DATABASE_INFO["password"]}@leadgencluster.sanup.mongodb.net/?retryWrites=true&w=majority&appName=LeadGenCluster'
            
            # Create MongoDB client
            self.client = pymongo.MongoClient(self.url)
            
            # Set database
            self.db_name = database_name if database_name else 'lead_generation'
            self.db = self.client[self.db_name]
            
            # Set collection
            self.collection_name = collection_name if collection_name else 'leads'
            self.collection = self.db[self.collection_name]
            
            # Test connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
            
        except Exception as e:
            print(f"Error connecting to MongoDB: {str(e)}")
            raise

    def insert_one(self, data):
        """Insert a single document"""
        try:
            return self.collection.insert_one(data)
        except Exception as e:
            print(f"Error inserting document: {str(e)}")
            return None

    def find(self, query=None):
        """Find documents matching query"""
        try:
            if query is None:
                query = {}
            return list(self.collection.find(query))
        except Exception as e:
            print(f"Error finding documents: {str(e)}")
            return []

    def update_one(self, query, update_data):
        """Update a single document"""
        try:
            return self.collection.update_one(query, {"$set": update_data})
        except Exception as e:
            print(f"Error updating document: {str(e)}")
            return None

    def delete_one(self, query):
        """Delete a single document"""
        try:
            return self.collection.delete_one(query)
        except Exception as e:
            print(f"Error deleting document: {str(e)}")
            return None

# Test the connection if run directly
if __name__ == "__main__":
    try:
        db = MongoDBData()
        print("MongoDB connection test successful!")
    except Exception as e:
        print(f"MongoDB connection test failed: {str(e)}")