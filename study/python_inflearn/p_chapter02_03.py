# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언
class Car(object):
    '''
    Car Class
    Author : theo
    Date : 2025.01.05
    Description : Class, Static, Instance Method
    '''

    # Class Variable 모든 인스턴스가 공유
    # 과세 비율이 있다고 생각
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method 인스턴스 메소드
    # self : 클래스로 만든 객체의 고유한 속성 값 사용
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method 직접 인스턴스에 접근하는 것이 매우 좋지 않은 상황을 불러올 수 있기때문에 인스턴스 메소드로 생성을 해준다.
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method 클래스 매소드는 첫번째 인자로 cls를 받는다.
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! price increased.'

    # Static Method
    # BMW 인지 아닌지 확인하는 메소드
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not BMW.'
    
    
# 자동차 인스턴스    
car1 = Car('BMW', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 기본 정보
print(car1)
print(car2)
print()

# 전체 정보
car1.detail_info()
car2.detail_info()
print()

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.2 # 직접접근해서 변경하는 것은 좋지 않다.

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()

# 가격 정보(인상 후 : 클래스메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Bmw 여부(스테이틱 메소드 미사용)
def is_bmw(inst):
    if inst._company == 'Bmw':
        return 'OK! This car is {}.'.format(inst._company)
    return 'Sorry. This car is not Bmw.'

# 별도의 메소드 작성 후 호출
print(is_bmw(car1))
print(is_bmw(car2))
print()

# Bmw 여부(스테이틱 메소드 사용)
print('Static : ', Car.is_bmw(car1))
print('Static : ', Car.is_bmw(car2))
print()

print('Static : ', car1.is_bmw(car1))
print('Static : ', car2.is_bmw(car2))
