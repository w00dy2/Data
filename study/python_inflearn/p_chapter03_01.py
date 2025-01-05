# Chapter03-01
# 파이썬 심화
# 매직 메소드, 스페셜 메소드 Special Method(Magic Method)
# -> 클래스 안에 정의할 수 있는 특별한(built - in) 메소드
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 즉, special method를 이해해야, class를 이해 -> sequence 이해 -> 반복 , 함수 이해  유기적으로 연관되어있다.

# 기본형
# 모든 타입들은 클래스이다.
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))
print()
print()

n = 10 # 변수에 int형을 선언 -> 출력 결과는 <class 'int'>로 출력이 된다.

# 사용
print(n + 100) # 출력결과 110
print(n.__add__(100)) #내부적으로 __add__ 메소드가 호출된것임.
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        # 인스턴스 메소드
        self._name = name
        self._price = price
    
    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    # def __add__(self, x):
    #     return self._price + x._price
    
    # def __sub__(self, x):
    #     return self._price - x._price

    # 대소 기호
    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._price >= x._price:
            return True
        else:
            return False
    # 대소 기호
    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._price <= x._price:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._price - x._price

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직메소드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
