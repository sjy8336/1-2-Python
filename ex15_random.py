import random
# 랜덤 모듈을 사용하기 위해 import 한다
# help(random.random)
"""  
주요 함수
choice(seq) : 리스트같은 sequence에서 임의 요소를 선택
choices(population, k) : 모집단으로 부터 k개의 크기를 갖는 목록을 선택
randint(a, b) : [a, b] 범위에서 난수(정수)를 반환
random() : 0 <= r < 1 사이의 난수(실수)를 반환
sample(population, k) : 모집단으로 부터 k개를 임의로 추출
"""
for i in range(5):
    r = random.random()
    print('r: ', r)

# randint()함수 호출해서 5개의 임의의 정수 출력 10 ~ 50 사이의 값
for _ in range(5):
    r = random.randint(10, 50) # 10 <= r < 50
    print('r: ', r)

# choice()/choices()
fruits = ['apple', 'banana', 'orange', 'kiwi']
r = random.choice(fruits)
print('r: ', r)

r = random.choices(fruits, k = 2)
print('r: ', r) #결과 => ['apple', 'kiwi']

# 모집단에서 중복없이 k개 추출
r = random.sample(fruits, 2)
print('r: ', r)

#  seed() : 난수 생성 초기값을 지정하여 동일한 랜덤값을 추출할 수 있다
random.seed(42)
for _ in range (5):
    r = random.randint(1, 10)
    print(r)