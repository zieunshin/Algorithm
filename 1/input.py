# input() 함수는 1줄의 문자열을 입력받음
# map() 함수는 리스트의 모든 원소에 각 특정 함수를 적용할 때 사용

# 공백을 기준으로 구분된 데이터를 입력받을 때
# list(map(int, input().split()))

n = int(input())
data = list(map(int, input().split()))

print(n)
print(data)


n, m, k = map(int, input().split())
print(n, m, k)