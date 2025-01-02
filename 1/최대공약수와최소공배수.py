import math

def lcm(a, b) :
    return a*b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14))  # 최소 공배수(lcm) 계산 