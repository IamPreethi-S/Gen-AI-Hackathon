# from pymongo import MongoClient
# from config import MONGO_URI

# def test_mongodb_connection():
#     try:
#         # Create MongoDB client
#         client = MongoClient(MONGO_URI)
        
#         # Test connection
#         client.admin.command('ping')
#         print("Successfully connected to MongoDB!")
        
#         # List databases
#         print("\nAvailable databases:")
#         for db in client.list_databases():
#             print(f"- {db['name']}")
            
#     except Exception as e:
#         print(f"Error connecting to MongoDB: {str(e)}")
#     finally:
#         client.close()

# if __name__ == "__main__":
#     test_mongodb_connection()


from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://genaihackathon:genai12345@leadgencluster.sanup.mongodb.net/?retryWrites=true&w=majority&appName=LeadGenCluster"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)