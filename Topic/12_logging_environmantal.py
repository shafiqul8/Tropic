"""
Topic 12: Logging & Environment
-------------------------------
Logging helps track events in a program. Environment variables allow storing 
configuration outside the code, e.g., API keys, paths.

We will cover:
1️⃣ Logging with the logging module
2️⃣ Logging levels and formats
3️⃣ Environment variables using os
4️⃣ Using .env files with python-dotenv
"""

import logging
import os
from dotenv import load_dotenv

# 1️⃣ Basic Logging
logging.basicConfig(level=logging.INFO)  # Default level: INFO
logging.debug("This is a DEBUG message")  # Will not show
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

# 2️⃣ Logging with format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("Logging with custom format")
logging.error("Something went wrong!")

# 3️⃣ Environment Variables
# Set environment variable in OS (for example purposes, we do it in code)
os.environ["API_KEY"] = "123456789"

api_key = os.environ.get("API_KEY")  # Fetch environment variable
print("API_KEY:", api_key)

# 4️⃣ Using .env File
# Suppose we have a file named .env with content:
# DB_USER=admin
# DB_PASS=secret

# Load .env file
load_dotenv()  # Loads .env variables into environment

db_user = os.getenv("DB_USER")  # Fetch from environment
db_pass = os.getenv("DB_PASS")

print("DB_USER:", db_user)
print("DB_PASS:", db_pass)

#Excersice--------
import logging
logging.basicConfig(filename='app.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.warning("This is a warning")
logging.error("This is an error")
logging.info("This info will not be logged")

#2

import os
os.environ["SECRET_KEY"] = "mysecret123"
secret = os.getenv("SECRET_KEY")
print("SECRET_KEY:", secret)


#3


from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print("Username:", username)
print("Password:", password)

