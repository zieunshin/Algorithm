a = 1
b = 2
print(a, b)
# end = " " 로 자동 줄바꿈 방지
print(7, end=" ")
print(a)
print(b)

answer = 7
print("정답은 " + str(answer) + " 입니다.")

# f-string : 문자열 앞에 두사 'f'를 붙여 사용
# 중괄호 안에 변수명을 집어넣어 문자열과 정수를 함께 넣을 수 있음
print(f"정답은 {answer} 입니다.")
