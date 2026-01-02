# 다수값을 반환하는 함수
def add(a, b):
    return a + b # 1개의 값을 반환하는 함수

# 다수 값을 반환하는 함수 => 반환되는 값은 tuple 값 ()
def calc(a, b):
    tot = a + b
    gop = a * b
    minus = a - b
    divide = a / b
    return tot, gop, minus, divide

result = add(10, 20)
print(f'result={result}, type: {type(result)}')
# result=30, type: <class 'int'>

result = calc(10, 20)
print(result)
print(type(result))
# (30, 200, -10, 0.5)
# <class 'tuple'>
a, b, c, d = calc(3, 1)     #unpacking
print(a, b, c, d)