# 함수(function/method)
# 일정한 작업을 수행하는 코드 집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용한다

"""  
[1] 함수 정의
    def 함수이름([매개변수])
        함수몸체 코드들
        [return 변환값]

        - 함수 내부에서 받아들이는 값 -> 값을 받는 변수를 매개변수, 인자, parameter, argument 라고 한다.
        - 반환값이 있을 경우 이 값은 함수를 호출하는 쪽에서 변수를 받을 수 있다.
-------------------------
[2] 함수 호출
    함수이름()
    함수이름(1, 2)
    y = 함수이름(2) : 반환값이 있을 경우
"""

# [1] 함수 구성
def print_star():
    for _ in range(5):
        print('*', end= '')
    print()

# [2] 함수 호출
print_star()
print_star()

# 별을 찍되 사용자가 원하는 개수를 인자로 넣어주면
# 해당 인자만큼 별을 출력하는 함수를 구성하세요
# 함수명 print_star2(num)
# 구성 후 호출하세요
def print_star2(num): 
    for _ in range(num):
        print("*", end='')
    print()
print('-----------------------------')

"""  
문자 1개 받고 숫자 1개 받아서
해당 문자를 숫자만큼 출력하는 함수를 구성하세요
print_shape(ch, num)
구성 후 호출하세요
"""

def print_shape(ch, num):
    for _ in  range(num):
        print(ch, end='')
    print()
print('------------------------------------')

# 함수 호출
print_shape('@', 6)
print_shape('$', 12)
print_shape('@', 18)

"""  
[1] 매개변수 없고 반환값 없는 함수 ex) print_star
[2] 매개벼수 있고, 반환값 없는 함수 ex) print_star2(3) print_shoape('#',3)
[3] 매개변수 없고, 반환값 있는 함수 => 호출 시 반환갓을 받아줄 변수가 필요
[4] 매개변수 있고, 반환갑소 있는 함수 => 호출 시 반환값을 받아줄 변수가 필요함
"""

# [1] 매개변수 없고, 반환값 없는 함수
def foo():
    print('foo()함수입니다')
foo()

# [2] 매개변수 있으며, 반환값 없는 경우
def bar(a, b):
    print('bar()함수 입니다.')
    print(a,b)
bar('hello', 'world')
bar(10, 30)

# [3] 매개변수 없고, 변환값이 있는 함수
# => 함수 마지막 라인에 return 분을 이용해서 값을 반환해야 함
def baz():
    print('baz()함수 ~~~')
    return 100
baz()
y = baz()
print(f'내가 받은 금액: {y}원')

# [4] 매개변수 있고, 반환값도 있는 함수
# 3개의 정수를 매게변수로 받아서 더한 결과를 반환하으
# 함수명: total(x, y, z)
# 함수 호출하기, 그 결과값 받아서 출력하기

def total(x, y, z):
    return(x + y + z)

total(1, 2, 3)
k = total(1, 2, 3)
print(k)
print(k*3)
print(total(11, 12, 13)) # 1회용

def func():
    pass # 통과
func()
print(func()) #None 을 출력함

# 함수를 구성하고 호출하기 실습

"""  
[1] 함수명 : convertInch
- 함수 안에서 '길이는? (cm)' 입력을 받자 => input()
- 사용자가 입력한 cm를 인치(in)로 변환하여 출력하는 함수
- [hint] 1인치: 0.3937 cm
"""

""" In = 0.3937
def convertInch(cm):
    return(cm / In)
    a(int(input('길이는? (cm) >>>')))
print(convertInch) """

def convertInch(): #매개변수 x, 반환값: x
    cm = int(input('길이는? (cm) :'))
    inch = cm * 0.3937
    print(f'{cm} cm는 {inch:.2f} inch입니다')
convertInch()

cm = int(input('길이는? (cm) :'))
def cvInch(num):
    inch = num * 0.3937
    return inch
cvInch(cm)
ic = cvInch(cm)
print(f'{cm} cm는 {ic:.2f} inch입니다')

"""  
[2] 2개의 정수를 매개변수로 받아서 두 숫자 중 큰 숫자를 반환하는 함수 구성하세요
함수명: myMax(a, b)
"""

# 내장함수: max(), min(), sum()
def myMax(a,b):
    if a > b:
        return a
    else:
        return b
print(myMax(99, 101))
print(myMax(-99, -101))

def myMax2(a,b):
    if a > b:
        return a
    return b #위랑 똑같은 의미 코드
print(myMax2(15, 43))
print(myMax2(-15, -43))

# 4개의 정수를 매개변수로 받아서 4개의 정수 중 가장 큰 값을 반환하는
# 함수를 구성하고 호출하세요
# 함수명 myMax4(a, b, c, d)
""" 
def myMax4(a, b, c, d):
    if a > b > c > d or a > b > d > c or a > c > b > d or a > c > d > b or a > d > b > c or a > d > c > b:
        return a
    if b > a > c > d or b > a > d > c or b > c > a > d or b > c > d > a or b > d > a > c or b > d > c > a:
        return b
    if c > a > b > d or c > a > d > b or c > b > a > d or c > b > d > a or c > d > a > b or c > d > b > a:
        return c
    return d
print(myMax4(32, 43, 12, 65)) """

def myMax4(a, b, c, d):
    mx = a
    if mx < b:
        mx = b
    if mx < c:
        mx = c
    if mx < d:
        mx = d
    return mx
y = myMax4(45, 23, 65, 24)
print(y)

def myMax4_2(a, b, c, d):
    return myMax2(d, myMax2(c, myMax2(a,b)))
x = myMax4_2(45, 23, 65, 24)
print(x)

# 0 ~ n 까지의 값을 출력하는 반복문이 들어있는 함수를 만드세요
# 한 줄에 10개씩 출력하도록 하세요
# show_num(n)
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19

def show_num(n):
    for i in range(n):
        print(f'{i:2d}', end=' ')
        if i % 10 == 9:
            print()
show_num(50)