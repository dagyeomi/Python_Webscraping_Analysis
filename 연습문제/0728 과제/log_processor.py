# log_processor.py

from datetime import datetime

logs = [
    ("2025-07-20 09:15:00", "WARNING", "메모리 사용량이 높습니다"),
    ("2025-07-20 10:30:00", "ERROR", "데이터베이스 연결 실패"),
    ("2025-07-20 11:45:00", "ERROR", "파일을 찾을 수 없음"),
    ("2025-07-20 12:00:00", "WARNING", "디스크 공간 부족"),
    ("2025-07-20 13:00:00", "INFO", "시스템 정상 작동")
]

filename = "system.log"

# 로그 파일 생성
with open(filename, "w", encoding="utf-8") as f:
    for timestamp, level, message in logs:
        f.write(f"{timestamp} - {level} - {message}\n")

print("로그 파일이 생성되었습니다.\n")

# 로그 필터링
def filter_logs(level):
    print(f"{level} 레벨 로그들:")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if f" - {level} - " in line:
                print(line.strip())
    print()

filter_logs("ERROR")
filter_logs("WARNING")
