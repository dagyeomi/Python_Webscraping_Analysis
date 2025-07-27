# rectangle_calculator.py

# 가로, 세로 입력받기
width = float(input("가로 길이를 입력하세요: "))
height = float(input("세로 길이를 입력하세요: "))

# 넓이와 둘레 계산
area = width * height
perimeter = 2 * (width + height)

# 출력
print(f"직사각형의 넓이: {int(area)}")
print(f"직사각형의 둘레: {int(perimeter)}")
