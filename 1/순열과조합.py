# 순열 : 서로 다른 n개에서 r개를 뽑아 일렬로 나열하는 것
from itertools import permutations

data = ['A', 'B', 'C']
# 모든 순열 구하기
result = list(permutations(data,3))
print(result)


# 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 뽑는 것
from itertools import combinations

data = ['A', 'B', 'C']
# 2개를 뽑는 모든 조합 구하기
result = list(combinations(data,2))
print(result)