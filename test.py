import google.generativeai as genai

genai.configure(api_key="AIzaSyBCwiVnS9C1oVNBv2wzA7RBtRTbpG2Q458")

model = genai.GenerativeModel("models/gemini-2.5-flash")  

response = model.generate_content("hi, how are you?")

print(response.text)
