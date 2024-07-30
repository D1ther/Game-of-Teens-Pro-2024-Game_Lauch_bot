from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

load_dotenv()

GPT_TOKEN = getenv("GPT_TOKEN")

client = OpenAI(api_key='sk-None-6fq6yhb8LyDd1hyFFZIsT3BlbkFJTxpcz2WctfWhlZUfdq0a')


promt = input('Уведіть запит: ')

complection = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role':'system', 'content':'You are a gamer with a lot of experience, and now you run your Telegram bot and give advice to younger players'},
        {'role':'user', 'content':f'{promt}'}
    ],
    temperature=0.2,
    max_tokens=1000
)

print(complection.choices.append[0].message)
