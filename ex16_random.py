# 무한루프 돌면서 랜덤한 난수(실수)를 발생시키세요
# 단, 발생된 난수값이 0.01 미만이면 반복문을 종료 시킨 후
# 그동안 발생된 난수 개수를 출력하세요
import random

# 내가 한거
""" t = 0
while True :
    r = random.random()
    print('r: ', r)
    if r < 0.01 :
        break
# print(f'총 개수: {}')
"""
t = 0
while True :
    r = random.random()
    print('r: ', r)
    t = t + 1
    if r < 0.01 :
        break
print(f'발생한 난수의 개수: {t} 개')
print('-----------------------------')

# [2] names = ['이순신', '강감찬', '이율곡', '홍길동', '권율']
#  위 사람들 중에서 랜덤하게 3명 추출해 출력하세요

names = ['이순신', '강감찬', '이율곡', '홍길동', '권율'] 
# list 자료구조 []
# choices() / sample()
n = random.choices(names, k = 3)
print(n)

m = random.sample(names, k = 3)
print(m)

# 랜덤하게 대문자 알파벳을 발생시키고자 한다면
# A : 아스키코드 65     B : 66
# Z : 아스키코드 90

num = 90
ch = chr(num) #문자로 변환하는 함수
print(ch)

# 알파벳 대문자를 랜덤하게 추출해서 아래와 같이 출력하세요
"""  
Z O P R X
A F U P O
E E C I Y
"""
# 내가한거
""" for i in range(1, 4):
    for j in range(1, 6):
        r = random.randint(65, 90)
        ch = chr(r)
        print(f'{ch}', end=' ')
    print() """

for i in range(3):
    for j in range(5):
        r = chr(random.randint(65, 90))
        print(r, end=' ')
    print()

"""  
컴퓨터가 랜덤한 정수를 1 ~ 100 사이 중 하나를 발생시킨다
이 숫자를 맞추는 게임을 작성하세요
무한루프 돌면서 사용자 입력을 받아 컴퓨터가 발생시킨 값과 같으면 
"빙고"를 출력하고 반복문 빠져나오세요
만약 사용자가 입력한 값이 작으면 "더 큰 수를 입력하세요"를 출력
크면 "더 작은 수를 입력하세요"를 출력하세요
게임 시도 횟수는 7번으로 제한합니다
7번 이내 맞추지 못하면 "실패!!" 출력 후 종료하세요
"""

# 내가 한거
""" t = 0
while True :
    r = random.seed(1, 100)
    a = int(input('숫자를 맞춰보세요 >>>'))
    t = t + 1
    if a == r :
        break
        print('빙고!!')
    elif a < r :
        print('더 큰 수를 입력하세요')
    elif a > r :
        print('더 작은 수를 입력하세요')
    elif t == 7:
        break
        print('실패!!')
    """

com = random.randint(1,100)
cnt = 0
while True:
    if cnt >= 7:
        print('실패!!')
        break
    me = int(input('1~100 사이의 정수값을 입력하세요:'))
    cnt += 1
    if com == me:
        print('빙고')
        break
    elif com > me:
        print('더 큰 수를 입력하세요')
    else:
        print('더 작은 수를 입력하세요')
print(f'총 게임 시도 회수: {cnt}')
print('-------------------')