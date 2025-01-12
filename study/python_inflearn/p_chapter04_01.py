# Chapter04-01
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists
chars = '+_)(*&^%$#@!~)'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

# Comprehending Lists 리스트 컴프리핸션
code_list2 = [ord(s) for s in chars] # append를 사용하는 시간이 줄어든다.

# Comprehending Lists + Map, Filter 
# 속도 약간 우세
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
#map()은 chars의 각 문자에 대한 유니코드 값들을 순차적으로 제공하는 iterator를 생성

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


# Generator 생성 
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
# 리스트 컴프리핸션
tuple_g = [ord(s) for s in chars]
# 제네레이터 : 반환할 준비만 한 상태 <generator object <genexpr> at 0x7fc5a5da5300>
tuple_g = (ord(s) for s in chars) 

# Array
array_g = array.array('I',  (ord(s) for s in chars))

print(type(tuple_g)) # <class 'generator'>
print(next(tuple_g)) # 43 | 계속 next를 하면 다음으로 넘어간다.
print(type(array_g)) # <class 'array.array'>
print(array_g.tolist()) # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33, 126, 41]



print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))# next가 없기때문에 출력결과가 generator로만 출력된다.

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)


print()
print()

# 리스트 주의
# 보기에는 똑같이 생겼다.
marks1 = [['~'] * 5 for n in range(5)]
marks2 = [['~'] * 5] * 5

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X' # 모든인덱스의 전체 값이 수정된다.

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
# [140486868400512, 140486868400640, 140486868400704, 140486868400832, 140486868400896]
# [140486868401024, 140486868401024, 140486868401024, 140486868401024, 140486868401024]