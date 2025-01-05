# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Car():
    """
    Car Class
    Author : theo
    Date : 2025.01.05
    """

    # 클래스 변수 갯수 카운트 하는방법
    car_count = 0
    # self : 인스턴스 메소드 | 각자 고유의 값을 가지고 있다.
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    # 삭제 변수 -> 카운트도 줄여야하기때문에 car_count -= 1을 해주는것.
    def __del__(self):
        Car.car_count -= 1


# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 에러
# Car.detail_info() self로 값을 받기때문에 값까지 넣어줘야한다.
Car.detail_info(car1) # car1.detail_info() 동일한 결과
Car.detail_info(car2)

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# 클래스 변수

# 접근
# 정석으로 사용할거면 class name으로 사용해야한다.
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

print()
print()


# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
del car2

print(car1.car_count)
print(Car.car_count)

# 클래스 변수는 모든 인스턴스가 공유한다. -> 공통적인 결과를 나타낼때는 클래스 변수를 사용해야한다.