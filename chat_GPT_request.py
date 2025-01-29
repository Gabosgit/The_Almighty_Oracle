import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() #loads variables from the .env file into the environment
API_KEY = os.getenv('API_KEY') # os.getenv() to access the environment variables loaded from the .env file

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Explain how AI works")


def make_request(question):
	response = model.generate_content(question)
	return response.text
#print(make_request('Where is Berlin?'))