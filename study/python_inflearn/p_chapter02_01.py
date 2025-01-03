# Chapter02-01
# 파이썬 중급
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 , 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대해짐 -> 복잡
# 클래스 중심 -> 데이터중심 -> 객체로 관리
# 클래스 사용 장점

# 일반적인 코딩
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]


# 리스트 구조
# 관리하기 불편 ->인덱스로 접근해야하기 때문에
# 인덱스 접근 시 실수 가능성 증가, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower': 400, 'price': 8000},
    {'color' : 'Black', 'horsepower': 270, 'price': 5000},
    {'color' : 'Silver', 'horsepower': 300, 'price': 6000}
]

# 자동차 회사 삭제
del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제, 키 조회 예외 처리 등
# 첫번째 키 car_company / 두번째 car_detail
cars_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color' : 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower': 300, 'price': 6000}}
]

del cars_dicts[1]
print(cars_dicts)
print()
print()


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
    # 원하는대로 속성정보 출력 / 비공식적
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    # 공식적 객체를 출력하기위함.(엄격한 타입까지)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    #str이 없으면 repr로 출력을 해준다.
    

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


# __dict__를 사용하면 클래스 내부 속성정보를 다 볼수가 있다.
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 리스트 선언
car_list = []
# list를 출력하면 repr로 받아서 출력이된다.
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print()

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(repr(x))
    print(x)