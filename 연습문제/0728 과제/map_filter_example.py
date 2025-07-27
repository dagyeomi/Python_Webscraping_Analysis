# map_filter_example.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("원본 숫자:", numbers)

# map을 이용한 제곱
squared = list(map(lambda x: x**2, numbers))
print("모든 수의 제곱:", squared)

# filter를 이용한 5보다 큰 수 추출
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 수들:", greater_than_5)

# 5보다 큰 수의 제곱
squared_filtered = list(map(lambda x: x**2, greater_than_5))
print("5보다 큰 수들의 제곱:", squared_filtered)
