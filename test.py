import requests

url = 'https://serve-api.vessl.ai/api/v1/services/8vn5siw1fei4/request/api/chatbot'
token = '7vPG0BFAg8lC16iEcw8hZfwSOed6e4f3'
data = {"name": "jinjin"}  # name을 데이터에 포함

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("Response from server:")
    print(response.json())  # JSON 응답을 출력
else:
    print(f"Failed to get a valid response. Status code: {response.status_code}")
    print("Response content:", response.text)  # 실패한 경우 응답 내용을 출력