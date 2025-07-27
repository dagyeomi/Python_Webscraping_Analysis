# system_info.py

import os
import sys

# 현재 작업 디렉토리
cwd = os.getcwd()
print("현재 작업 디렉토리:", cwd)

# Python 버전
print("Python 버전:", sys.version)

# 운영체제
print("운영체제:", os.name)

# 환경변수 PATH 일부
path_env = os.environ.get("PATH", "")
print("환경 변수 PATH 일부:", ":".join(path_env.split(":")[:4]))

# 파일 경로 정보
file_path = "/Users/username/documents/report.txt"
dir_name = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
file_ext = os.path.splitext(file_path)[1]

print("파일 경로 정보:")
print(f"- 디렉토리: {dir_name}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {file_ext}")

# 파일 존재 여부
print("파일 존재 여부:", os.path.exists(file_path))
