# module_usage.py

import datetime
import random

# 현재 날짜와 시간
now = datetime.datetime.now()
print("현재 날짜와 시간:", now)

# 포맷된 날짜
formatted = now.strftime("%Y년 %m월 %d일 %A")
print("포맷된 날짜:", formatted)

# 임의의 숫자/실수/리스트 요소
print("임의의 숫자:", random.randint(1, 10))
print("임의의 실수:", round(random.uniform(1.0, 10.0), 2))

fruits = ['사과', '바나나', '오렌지', '딸기', '포도']
print("임의의 리스트 요소:", random.choice(fruits))

# 리스트 섞기
random.shuffle(fruits)
print("섞인 리스트:", fruits)
