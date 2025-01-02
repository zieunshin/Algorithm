import sys

# 사용자에게 입력을 최대한 빠르게 입력받기
# 이진탐색, 정렬, 그래프에서 잦게 사용됌
# sys 라이브러리에 있는 sys.stdin.readline() 메서드 사용
# 마지막에 엔터가 입력되므로 rstrip() 메서드 함께 사용
data = sys.stdin.readline().rstrip()
print(data)