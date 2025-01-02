# 더하기 함수 example1.1
def add(a,b) :
    return a+b

print(add(3,7))


# 더하기 함수 example.2
def add (c, d):
    print ("함수의 결과 :", c+d)

add(3, 6)


# global 키워드 : 함수 바깥에 정의된 변수 참조 가능
num = 0
 
def func():
    global num
    num += 1

for i in range (10) :
    func()

print(num)


# 람다 표현 식 !!!
# 각 리스트의 첫번째원소끼리, 두번째원소끼리 더한 값 구하는 example
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b : a+b, list1, list2)

print(list(result))



# 자주 사용되는 내장함수 !!!!

# sum() : 더한 값
result = sum([1,2,3,4,5])
print(result)

# min(), max() : 최대, 최소
min_result = min(7,3,5,2)
print(min_result)

# sorted() : 오름차순 정렬
result = sorted([5,4,3,2,1])
print(result)