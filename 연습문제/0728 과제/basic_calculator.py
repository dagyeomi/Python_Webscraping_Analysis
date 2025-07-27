# basic_calculator.py

# 사용자로부터 두 개의 정수를 입력받기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 수행
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# 결과 출력
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div:.2f}")  # 소수 둘째 자리까지 출력