# word_counter.py

sentence = input("문장을 입력하세요: ")

# 앞뒤 불필요한 공백 제거 + 중간 다중 공백은 하나로 줄임
cleaned = " ".join(sentence.strip().split())

word_count = len(cleaned.split())

print(f"공백 제거: {cleaned}")
print(f"단어 개수: {word_count}개")
