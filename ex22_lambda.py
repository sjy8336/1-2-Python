# 람다 함수 : 한 줄로 쓰는 짧은 익명함수
"""  
lambda 매개변수들 : 반환값

함수명 - lambda 매개변수 : 반환값

- 이름없는 익명함수
- 한 줄로 간단한 계산을 할 때 사용
- 여러 매개 변수 사용 가능
- return 키워드를 쓰지 않아도 자동으로 반환된다
"""

# 숫자를 매개변수로 넣으면 거듭제곱값을 반환하는 함수
def square(x):
    return x ** 2
print(square(2))    # 4
print(square(8))    # 64

sqrt = lambda x : x ** 2
print(sqrt(4))
print(sqrt(7))

# [1] 매개변수를 1개 받아서 그 값에 10을 더한 값을 반환하는
# 람다 함수 구성 후 호출

add10 = lambda a: a + 100
print(add10(45))

# [2] 매게변수 2개를 받아 두 수의 더하기 값을 반환하는 람다함수
add = lambda a, b : a + b
print(add(66, 44))  #110

print((lambda a : a ** 3)(2)) # 8
# 익명 함수 => 즉시 실행함수

# 짝수인지 판별하는 익명함수 구성하고 짝수면 True를 반환하도록
# 구성 후 호출해보세요

""" num = lambda a : a % 2
if num == 0:
    print('True')
else :
    print('False') """

print((lambda n : n % 2 == 0)(44))  #한 번 쓰고 말거는 이런식으로

isOdd = lambda n : n % 2 == 1
print(isOdd(5))
print(isOdd(10))

# 문자열을 매개변수에 넣으면 해당 문자열의 길이를 반환하는
# 함수를 람다함수로 구성 후 호출해보세요. len()함수 활용

string_len = lambda string : len(string)
print(string_len('Python'))
print(string_len('Java'))