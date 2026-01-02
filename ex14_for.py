""" 
중첩 반복문
반복문:
    반복문:
        실행문1
    실행문2
2개이상의 반복문을 중첩해서 사용하는 경우
이 경우 바깥쪽 반복문은 행을
안쪽 반복문은 열을 반복하는데 사용한다
"""
for i in range(1, 4):   #3행
    for j in range(1, 3):   #2열
        print(f'({i}, {j})', end=' ')
    print() #줄바꿈

""" 
i = 1   j = 1
        j = 2
i = 2   j = 1
        j = 2
i = 3   j = 1
        j = 2
"""
print('-------------------------')

"""
[1]  
*****
*****
*****
별 출력하세요 3행 5열
"""

# [1]
""" a = '*'
for b in range(1, 4):
    for c in range(1, 6):
        print(a, end=' ')
    print(a)
print('-------------------------') """
# [1]
for i in range(3):
    for j in range(5):
        print('*', end='')
    print() #줄바꿈
print('-------------------------')

"""  
[2]
*
**
***
****
"""

# [2]
for x in range(1, 5):
    print('*' * x)
print('-------------------------')
# [2]
for y in range(1, 5):
    for z in range(1, 5):
        if y == z or y > z:
            print('*', end='')
    print()
print('-------------------------')

# if y == z or y > z: 이부분을 줄이게되면 y >= z

"""  
[3] 중첩 for 루프 이용해서 구구단 출력하기
2x1=2     3x1= 3  ........    9x1=9
2x2=4     3x2= 6  ........    9x2= 18
"""

# [3]
for n in range (2, 10):
    for m in range(1, 10):
        print(f'{n}x{m}=', n * m, end=' ')
    print()

# print(f'{n}x{m}=', n * m, end=' ') 이부분을 줄이게 되면 {n}x{m}={n*m}, end = ' '