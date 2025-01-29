import google.generativeai as genai


genai.configure(api_key="AIzaSyB0Zp5T1AOV9FzJ9e1MCWaPXVWYzQsJIkY")
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Explain how AI works")


def make_request(question):
	prompt = (f"Provide only the macronutrient composition of {question} and specify the quantity taken to get the information."
			  f"The units have to be given in Kcal or grams as applicable"
			  f"The information have to be in the following format: "
			  f"Food (Quatity):,"
			  f"label 'calories' + quantity + unit 'KCal', "
			  f"label 'protein'  + quntity + unit 'g', "
			  f"label 'fat' + quantity + unit 'g', "
			  f"labrl 'carbohydrates'  + quantity + unit 'g' and"
			  f"label 'sugar in carbohydrates' + quentity + unit 'g'"
			  f"Do not Provide any other text information")
	response = model.generate_content(prompt)
	return response.text
#print(make_request('Where is Berlin?'))