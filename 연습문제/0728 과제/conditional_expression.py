# conditional_expression.py

# 삼항 연산자 예시 1
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

# 삼항 연산자 예시 2
age = 17
status = "성인" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 조건식 안에서 max
numbers = [5, 12, 8, 23, 42]
max_num = max(numbers) if numbers else None
print("숫자들의 최대값:", max_num)

# 조건식 안에서 필터링
positives = [num for num in numbers if num > 0]
print("양수들:", positives)
