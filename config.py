
from pathlib import Path

from dotenv import load_dotenv
import mongoengine as me
import os
import ssl
from urllib.parse import quote_plus
def load_env():
    dotenv_file = Path(f".env.dev")
    load_dotenv(dotenv_file)

def get_mongo_connection():
    username = quote_plus(os.environ['MONGODB_USERNAME'])
    password = quote_plus(os.environ['MONGODB_PASSWORD'])
    host = os.environ['MONGODB_HOST']
    db_name= os.environ['MONGODB_NAME']
    connection_uri = f"mongodb+srv://{username}:{password}@{host}/{db_name}?retryWrites=true&w=majority&appName=Chalkbooks"
    print(connection_uri)
    me.connect(host=connection_uri, tls=True, tlsAllowInvalidCertificates=True)
    try:
        assert me.connection.get_connection()
        print("Connected to mongodb successfully!")
    except AssertionError:
        print("Failed to establish a connection!")

load_env()
get_mongo_connection()