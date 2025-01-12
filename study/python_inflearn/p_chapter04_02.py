# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest) # 0 1 []
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest) # 1 2 [3, 4, 5]

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l)) # (15, 20, 25) 139923381840832 튜플
print(m, id(m)) # [15, 20, 25] 139923381839808 리스트

l = l * 2
m = m * 2
# 재할당했기때문에 상기 값과 id값이 변경됨.
print(id(l))
print(id(m))

l *= 2 # 불변형이기때문에 각 id값이 다르게 할당
m *= 2 # 리스트는 가변형이기 때문에 기존 id값에 재 할당

print(id(l))
print(id(m))

print()
print()

# sort vs sorted 
# reverse, key=len, key=str.lower, key=func..

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True)) # 역순정렬
print('sorted -', sorted(f_list, key=len)) # 알파벳의 길이로 정렬한다.
print('sorted -', sorted(f_list, key=lambda x: x[-1])) # 마지막글자 한글자 기준으로 정렬
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True)) # 마지막글자 한글자 기준으로 정렬
print()

print('sorted -', f_list)

print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None) 원본을 수정해버린다.
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)