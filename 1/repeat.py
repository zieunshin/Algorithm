# for문
array = [9,8,7,6,5]

for x in array :
    print(x)

# for문에서 반복적인 값을 차례대로 순회할 때는 range() 함수 사용
# range(시작 값, 끝 값+1) 형태로 사용
result = 0

for i in range(1, 31) :
    result += i

print(result)