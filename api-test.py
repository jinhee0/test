'''import argparse
import os

from openai import OpenAI

parser = argparse.ArgumentParser()
parser.add_argument("--base-url", default="https://api.openai.com")
parser.add_argument("--api-key", default="token-abc123")
parser.add_argument("--model-name", default="casperhansen/llama-3-8b-instruct-awq")
parser.add_argument("--prompt", default="Jinhee Lee")
args = parser.parse_args()

client = OpenAI(
    base_url=os.path.join(args.base_url, "v1"),
    api_key=args.api_key,
)

completion = client.chat.completions.create(
    model=args.model_name,
    messages=[
        {"role": "user", "content": args.prompt},
    ],
)

print(completion.choices[0].message.content)'''

# call_chatbot.py

import argparse
import main  # main.py를 임포트
import requests  # HTTP 요청을 위해 requests 라이브러리 사용

# 명령행 인자 처리를 위한 argparse 설정
parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, help="The URL to send the request to")  # 요청할 URL
parser.add_argument("--prompt", default="Jinhee Lee", help="Input prompt to send")  # 사용자가 입력할 데이터
args = parser.parse_args()

# main.py의 print_chatbot_message 함수를 호출
main.print_chatbot_message(args.prompt)

# 서버로 요청을 보내는 코드 (선택 사항)
response = requests.post(args.url, json={"content": args.prompt})  # POST 요청으로 데이터 전송

# 서버로부터 응답이 성공적으로 왔을 때 처리
if response.status_code == 200:
    print("Response from server:")
    print(response.json())  # 서버가 JSON 응답을 보냈다고 가정
else:
    print(f"Failed to get a valid response. Status code: {response.status_code}")

