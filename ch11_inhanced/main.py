"""
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스)
    본문
"""



class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이(가) {food}를 먹습니다.')

    def drink(self, drink_name):
        print(f'{self.name}이(가) {drink_name}을(를) 마십니다.')

person1 = Person('김영')
person1.eat('감자')

# 서브 클래스 정의
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')

    def drink(self, drink_name):
        print(f'{self.school}에서 ' ,end='')
        super().drink(drink_name)

potter = Student(name='헤리포터', school='호그와트')
potter.study()
potter.eat('라멘')    # 부모의 메서드를 정의하는 일 없이 그대로 쓸수있음.
potter.drink('투샷아메리카노')     # overriding으로 메서드 호출

'''
1. 서브클래스의 __init__()
    Java때와 마찬가지로 서브클래스는 슈퍼클래스가 없으면 존재할수 없음. 그래서 서브클래스의 생성자를 구현할 때는 '반드시 슈퍼클래스의 생성자를 먼저 호출'하는 코드를 작성해야됨.
    
    super()는 슈퍼클래스의 생성자라고 해석할수있음.
    potter = Student()에서 보면 알수있듯, 슈퍼클래스의 객체가 .__init__(name)이라는 메서드를 호출했다고 볼수있음.
    
    Java에서는 super() -> 생성자 / super.메서드명() 으로 super 자체가 객체인 경우가 있었지만, 파이썬에선 Super()로 일원화되어있음.
   
2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 수퍼클래스의 인스턴스
    서브 클래스의 인스턴스는 서브클래스의 인스턴스이면서 동시에 슈퍼클래스의 인스턴스
    Student 클래스의 객체는 Student의 인스턴스이면서 Person의 인스턴스
    
    Java를 기준으로 instanceof 연산자 역할을 하는 것이 JS에선 Typeof 연산자가 있고 python에선 isinstance() 함수가 있음.
    
형식:
isinstance(객체명, 클래스명) -> boolean 
'''
print(isinstance(potter, Person))       # T
print(isinstance(potter, Student))      # T
print(isinstance(person1, Student))     # F
print(isinstance(person1, Person))      # T
print(issubclass(Student, Person))      # T

'''
3. 다음 지시 사항을 읽고 Hybrid 클래스를 구현하시오.

지시 사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.

3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30

'''


class Car:
    max_oil = 50    # 클래스 변수
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')


class Hybrid(Car):
    max_amount = 30
    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount
        print('하이브리드 차량이 생산되었습니다.')

    def add_oil(self, oil):
        before = self.oil
        super().add_oil(oil)
        added = self.oil - before
        if added > 0:
            print(f'기름을 {added} 주유했습니다')

    def charge(self, amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > Hybrid.max_amount:
            self.amount = Hybrid.max_amount
        print(f'전기를 {amount} 충전 했습니다.')

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전 상태 : {self.amount}')

car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. -> call3()
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 -> call3()
        (넓이 = 너비 * 높이)
3. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.

 
circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____
너비가 10, 높이가 8인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''

class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(self.name)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {self.radius}인 {self.name}이 생성되었습니다.')

    def area(self):
       return 3.14 * (self.radius ** 2)

    def draw(self):
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()}입니다')

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {self.width}, 높이가 {self.height}인 {self.name}이 생성되었습니다. ')

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()}입니다.')

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형 1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이 : {rectangle.area()}')