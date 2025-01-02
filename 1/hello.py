# round() : 반올림 함수
a = 0.321 + 0.987
print(round(a,2))

# 배열에서 뒤에부터 원소 출력
b = [1,2,3,4,5]
print(b)
print(b[-2])    # 뒤에서 2번째 원소 출력

# 배열에서의 슬라이싱
print(b[1:4]) # 인덱스 1~3까지, 즉 두번째부터 네번째 원소까지 출력

# 리스트 컴프리헨션 :원하는 개수의 수를 한번에 초기하하는 것 
a = [i for i in range(10)]
print(a)
# 0~19까지의 수에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)
 
# 코테에서 자주 쓰이는 파이썬 리스트 메서드
# 변수명.append() : 리스트에 원소를 하나 삽입할 때 사용함
# 변수명.sort() : 기본 정렬 기능으로 오름차순으로 정렬
# 변수명.reverse() : 리스트 원소 뒤집기
# 변수명.insert() : 특정한 인덱스에 데이터 추가
# 변수명.count() : 특정 값인 데이터 개수 세기
# 변수명.remove() : 특정 값 데이터 삭제

# 사전 자료형 함수 dict()
c = dict()
c['신지은'] = 98
c['정경난'] = 99

print(c)

d = {
    '신지은' : 98,
    '정경난' : 99
}
print(d)
print(d['정경난'])

# key만 모아서 출력
key_list = list(c.keys())
print(key_list)

# value만 모아서 출력
value_list = list(c.values())
print(value_list)