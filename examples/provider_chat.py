"""Profile 01-openai. Cloud calls require internet and your own key."""
import argparse,os
from openai import OpenAI
p=argparse.ArgumentParser();p.add_argument('--provider',choices=['openai','deepseek','ollama'],default='openai');p.add_argument('--prompt',default='Explain tool calling in two sentences.');a=p.parse_args()
if a.provider=='deepseek':
 client=OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url='https://api.deepseek.com');model=os.environ.get('DEEPSEEK_MODEL','deepseek-flash')
elif a.provider=='ollama':
 client=OpenAI(api_key='ollama',base_url=os.environ.get('OLLAMA_BASE_URL','http://localhost:11434/v1'));model=os.environ['OLLAMA_MODEL']
else:
 client=OpenAI(api_key=os.environ['OPENAI_API_KEY']);model=os.environ['OPENAI_MODEL']
print(client.chat.completions.create(model=model,messages=[{'role':'user','content':a.prompt}]).choices[0].message.content)
