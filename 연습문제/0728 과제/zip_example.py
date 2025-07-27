# zip_example.py

students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

print("학생과 점수 매칭:")
for name, score in zip(students, scores):
    print(f"{name}: {score}점")

# 딕셔너리 생성
student_score_dict = {name: score for name, score in zip(students, scores)}
print("점수별 학생 딕셔너리:", student_score_dict)
