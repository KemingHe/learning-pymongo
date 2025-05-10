import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load and get envs at module level for all functions once
load_dotenv()
mongodb_uri = os.environ.get("MONGODB_URI", "undefined")

# Set up MongoDB connection at module level for all functions once
client = MongoClient(
    host=mongodb_uri, 
    server_api=ServerApi('1'),
)

def pin_mongodb_server():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def main():
    
    # print("Hello from learning-pymongo!")
    # print(f'MongoDB URI: {mongodb_uri}')
    pin_mongodb_server()


if __name__ == "__main__":
    main()
