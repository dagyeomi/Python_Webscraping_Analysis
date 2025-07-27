# statistics_function.py

import math

def get_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / len(numbers))
    return mean, maximum, minimum, round(std_dev, 2)

# 테스트
nums = [10, 20, 30, 40, 50]
mean, max_val, min_val, std_dev = get_statistics(nums)

print("숫자들:", nums)
print("평균:", mean)
print("최댓값:", max_val)
print("최솟값:", min_val)
print("표준편차:", std_dev)
