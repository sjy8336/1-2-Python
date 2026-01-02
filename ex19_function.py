# 함수 구성시 디폴트 인자 (default argument)를 구성할 수 있다
"""  
디폴트 인자: 함수에 인자값을 넣어주는 것도 필요하지만
            좀더 유연성 있는 작업을 위해 기본값을 할당하여 사용하게 한다
"""
def foo(a, b, c):
    print(a + b + c)
foo(1, 2, 3)    #6 [o]
# foo(10, 20)    #[x]
""" 
foo() missing 1 required positional argument: 'c' 
"""
# foo(100)    #[x]
# foo()   #[x]
# [주의사항] 기본값이 없는 매게변수가 먼저 위치하고 그 다음 위치에 기본값을 갖는 매개변수가 위치해야 한다

def total(a, b = 6, c = 0):     #b=0 : 디폴트 인자
    print(a + b + c)
total(1, 2, 3)  #6 [o]
total(1,2)  #3
total(1)    #[1]
# total()    #[x]

# TypeError: foo() missing 1 required positional argument: 'c'

# def gop(a = 1, b, c = 2):
    # print(a * b * c)
# SyntaxError: parameter without a default follows parameter with a default

def gop(b, a = 1, c = 2):
    print(f'{a}x{b}x{c}={a * b * c}')
# gop()함수 호출해보기
gop(11)
gop(2, 3)
gop(1, 2, 3)

# 키워드 인자
# 함수를 호출할 때 매개변수 이름을 적어서 값을 전달하는 방식
# print('hollo', and=' ')
gop(5, c = 7, a = 3)    #3x5x7=105

"""  
[1]
이름, 나이, 주소를 매개변수로 받아
회원의 정보를 아래와 같이 출력하세요
단, 매개변수 값이 전달되지 않을 경우 기본값을 할당하세요
함수명: show_info(name, age, addr)

이름 홍길동
나이: 22 세
주소: 서울 동작구 
"""

# [1] - 내가 푼거
""" def show_info(name, age, addr):
    print(f'이름: {name}\n나이: {age} 세\n주소: {addr}')
n = input('이름을 입력해주세요 >>>')
a = input('나이를 입력해주세요 >>>')
ad = input('주소를 입력해주세요 >>>')
show_info(n, a, ad) """

def show_info(name='아무개', age='1', addr='서울'):
    s = f"""
    이름: {name}
    나이: {age} 세
    주소: {addr}
    """
    print(s)
show_info()
show_info('홍길동', 22, '부산')
show_info(age = 23, name='홍길동', addr='인천')

n = input('이름 입력:')
a = input('나이 입력:')
j = input('주소 입력:')
show_info(n, a, j)

"""  
[2] 직사각형 또는 원의 면적을 구하는 함수를 구성하세요
첫 번째 인자값이 0이면 직사각형 면적을 출력하고
1이면 원의 면적을 구해 출력하세요
디폴트값 매개변수를 구성하세요
메서드명: area(mode, width, height, radius)
area(0, 10, 20) -> 사각형 면적 출력
area(1, radius = 8) -> 원의 면적 출력
"""

# [2]-내가한거
""" def area(mode, width, height, radius):
    if mode == 0:
        print(f'직사각형의 면적은 {width * height}m2 입니다')
    else:
        print(f'원의 면적은 {width * radius / 3.14}m2 입니다')
area(0, 10, 20, 0)
area(1, radius = 8) """

def area(mode = 0, width = 1, height = 1, radius = 1):
    if mode not in [0, 1]:
        # print('mode 값은 0 또는 1 중 하나여야 합니다')
        # return None
        return 'mode 값은 0 또는 1 중 하나여야 합니다'
    if mode == 0:
        return width * height
    if mode == 1:
        return 3.14 * radius ** 2

result = area(0, 3, 6)
print('직사각형 면적:', result)
result = area(mode = 1, radius = 10)
print('원의 면적:', result)
result = area(33, 2, 3, 8)
print(result)