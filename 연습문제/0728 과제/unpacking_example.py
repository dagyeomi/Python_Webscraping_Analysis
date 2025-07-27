# unpacking_example.py

# 튜플 언패킹
x, y = (10, 20)
print(f"좌표: x={x}, y={y}")

# 리스트 언패킹
a, b, c = [1, 2, 3]
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args 사용
def sum_all(*args):
    return sum(args)

print("가변 인수의 합:", sum_all(10, 20, 30))

# **kwargs 사용
def print_info(**kwargs):
    print("키워드 인수들:", ", ".join(f"{k}={v}" for k, v in kwargs.items()))

print_info(name="김철수", age=25, city="서울")
