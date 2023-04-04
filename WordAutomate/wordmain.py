import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate
import openai
openai.api_key = "SECRET API KEY FIND IN https://platform.openai.com/account/api-keys"  

prompt = "Write a 450 words approximately cover letter why I want to work in Deloitte as a Senior Data Engineer without the ending of cover letter"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=500)

 


doc = DocxTemplate("templateManager.docx")
my_name = "Bohdan Kvetka"
my_phone = "48730******"
my_email = "bohdankvietka@gmail.com"
my_address = "Warsaw, Poland"
jon_position = "Senior Data Engineer"
today_date = datetime.today().strftime("%d %b, %Y")
cover_letter = response.choices[0].text
company_name = "Deloitte"
bohdan_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date, 'cover_letter': cover_letter}



doc.render(bohdan_context)
doc.save("generated_doc.docx")