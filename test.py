# print("hello wordd")

# from nltk.downloader import Downloader ;
# # from nltk.downloader import Downloader
# a = Downloader()
# a.download("all")
from openai import OpenAI 
client = OpenAI(api_key="sk-proj-T8Hg1IJeUrsf7TnvteqST3BlbkFJOuL7NCP0kHerGOdQC0mu")
message= client.chat.completions.create(
   model="gpt-3.5-turbo",
   temperature=0.1,
    messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "tell me about mukalle"},
    ]
)

print(message.choices[0].message.content)