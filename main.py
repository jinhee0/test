from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 챗봇 문구 출력 함수
def print_chatbot_message(name):
    return f"Hello, {name}! I am a chatbot. I can assist you with various tasks. Feel free to ask me anything!"

# API 엔드포인트
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    # 요청으로부터 JSON 데이터 가져오기
    data = request.get_json()

    # JSON에서 name 필드 가져오기
    name = data.get('name', 'Guest')  # 기본값은 'Guest'

    # 챗봇 메시지 생성
    response_message = print_chatbot_message(name)

    # JSON 형태로 응답 반환
    return jsonify({'message': response_message})

# 메인 실행 블록
if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드로 실행

