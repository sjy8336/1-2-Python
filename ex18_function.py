# 내장함수 : int(), float(), str(), bool(), min(), max(), sum(), abs()...
print(int(12.345))  #12
print(int(-1.312367))   #-1
print(int('456')*2)    #곱셈 912
print('456'*2)  #문자열문자열

print(float(0))    #0.0
print(float(-500))  #-500.-

print(str(0.123)*2)    #0.1230.123

print(bool('False'))    #True
print(bool('True'))    #True
print(bool(0))    #False
print(bool(1))    #True
print(bool(100))    #True
print('------------------------------')
print(bool(''))    #False
print(bool(' '))    #True   공백문자 1개
print(bool('a'))
print(bool(None))   #False

lst = [90, 50, 82, 77, 65]
print(lst)
print(f'최대값: {max(lst)}, 최소값: {min(lst)}')
print(f'총합계: {sum(lst)}, 요소개수: {len(lst)}')
print(f'평균점수: {sum(lst) / len(lst)}')

# abs() : 절대값을 반환하는 함수
print(abs(512))
print(abs(-512))