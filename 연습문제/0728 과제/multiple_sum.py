# multiple_sum.py

multiples_of_3 = [n for n in range(1, 101) if n % 3 == 0]
total = sum(multiples_of_3)
count = len(multiples_of_3)

print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total}")
print(f"3의 배수의 개수: {count}개")
