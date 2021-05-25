import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client_url = os.getenv('CLIENT')
client = MongoClient(client_url, ssl_cert_reqs=False)
db = client.RPG