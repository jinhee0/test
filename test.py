import requests

url = 'https://serve-api.vessl.ai/api/v1/services/8vn5siw1fei4/api/chatbot'
token = '7vPG0BFAg8lC16iEcw8hZfwSOed6e4f3'
data = {"data": "jinjin"}  # name을 데이터에 포함

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)