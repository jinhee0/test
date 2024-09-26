# 챗봇 문구 출력 함수
def print_chatbot_message(name):
    print(f"Hello, {name}! I am a chatbot.")
    print("I can assist you with various tasks.")
    print("Feel free to ask me anything!")

# 메인 실행 블록
if __name__ == "__main__":
    user_name = input("What is your name? ")
    print_chatbot_message(user_name)
