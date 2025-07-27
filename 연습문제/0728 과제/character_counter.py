# character_counter.py

text = input("문자열을 입력하세요: ")
target = input("찾을 문자를 입력하세요: ")

count = text.count(target)

print(f"문자 '{target}'이 {count}번 나타납니다.")
