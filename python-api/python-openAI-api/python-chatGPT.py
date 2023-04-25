import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="enter your prompt to send to OpenAI", type=str)
parser.add_argument("file_name", help="enter a file name for the results of the prompt", type=str)

args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

content_headers ={
    "Content-Type": "application/json",
    "Authorization": "Bearer "+ api_key
}
request_data ={
    'model': 'text-davinci-003',
    'prompt': f"write python script to {args.prompt}",
    "max_tokens": 500,
    "temperature": 0.5
}
response =  requests.post(api_endpoint,headers=content_headers,json=request_data)

print(response.status_code)
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"request fail with status code: {str(response.status_code)}")