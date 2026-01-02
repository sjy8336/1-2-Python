# 가변 매개변수
"""  
함수 호출 시 몇 개의 인자값이 전달될지 알 수 없다면
매개 변수 앞에 *를 붙인다. => 가변 매개변수
이렇게 선언된 가변 매개변수는 함수가 호출될 때
전달한 모든 인수가 tuple 형태로 저장된다
"""

def addAll(*nums):
    # print(nums, type(nums))    #type : tuple
    total = 0
    for i in nums:
        total += i
    return total

def addAll2(*nums):
    return sum(nums)    #위 방식과 다르지만 같은 결과

# list : [], tuple : (), dict: {}, set : {}
t1 = addAll(1)   #(1,)
t2 = addAll(1, 2, 3, 4)  #(1, 2, 3, 4)
t3 = addAll(1, 2, 3, 4, 5, 65, 7, 8, 9)  #(1, 2, 3, 4, 5, 65, 7, 8, 9)
print(t1)   #1
print(t2)   #10
print(t3)   #104

print(addAll2(1, 2, 3, 4))

# **kwargs - 여러 개의 키워드 인자 받을 때
# 매개변수 앞에 ** 를 붙이면
# 들어오는 모든 키워드 인자를 딕셔너리(dict)로 받는다
# 특징
# - 키워드 인자를 무한히 받을 수 있다
# - 내부에 dict로 저장한다
# - key는 매개변수 이름, value는 전달받은 값이 된다

def show_info(**kwargs):
    print(kwargs)

# 키워드 인자를 넘겨보자
show_info(name = '김철수', age = '22', addr = '서울', tel = '2222-2223')
# {'name': '김철수', 'age': '22', 'addr': '서울', 'tel': '2222-2223'}
# {key:value}
# show_info('홍길동', '22', '광주', '4444-5555')  #[x] 위치 기반 인자는 넘기면 에러남
# TypeError: show_info() takes 0 positional arguments but 4 were given
show_info(one = 1, two = 2, 셋 = 3)    #{'one': 1, 'two': 2, '셋': 3}