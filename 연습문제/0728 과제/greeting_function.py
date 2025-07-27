# greeting_function.py

def greet(name, greeting="안녕하세요", suffix="님!"):
    print(f"{greeting}, {name}{suffix}")

# 테스트
greet("김철수")
greet("John", greeting="Hello", suffix="!")
greet("이영희", greeting="안녕하세요", suffix="님! 좋은 하루 되세요!")
