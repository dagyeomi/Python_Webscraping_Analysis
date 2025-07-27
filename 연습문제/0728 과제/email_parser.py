# email_parser.py

email = input("이메일 주소를 입력하세요: ")

if "@" in email:
    user, domain = email.split("@")
    print(f"사용자명: {user}")
    print(f"도메인: {domain}")
else:
    print("올바른 이메일 형식이 아닙니다.")
