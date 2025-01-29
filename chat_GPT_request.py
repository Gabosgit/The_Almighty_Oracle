import google.generativeai as genai


genai.configure(api_key="AIzaSyB0Zp5T1AOV9FzJ9e1MCWaPXVWYzQsJIkY")
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Explain how AI works")


def make_request(question):
	response = model.generate_content(question)
	return response.text
#print(make_request('Where is Berlin?'))