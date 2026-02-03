'''
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스 마다 서로 다른 값
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 접근 방식 - 인스턴스 접근 (o) / 클래스 접근(X)
    클래스 변수 접근 방식 - 인스턴스 접근 (O) / 클래스접근 (o)
'''
from ch07_classes.constructor.main import woman

# # 클래스 변수 예시
# class Korean:
#     country = '한국'  # 클래스 변수 # 1
#     def info(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
# # 객체 생성
# korean = Korean('김일', 21 , '서울특별시 마포구')
# print(korean.name)

'''
객체명.클래스변수명을 통해서 클래스변수에 접근이 다능하긴한데, 클래스 내부 코드를 보기전까진 country라는 변수가 인스턴스 변수인지 클래스변수인지 알지못함.

이상을 이유로 클래스별수를 확인하고자 할때는 객체명.클래스변수명 보다는 클래스명.클래스변수명을 통해서 창조하는것이 권장됨.

2. 클래스 메서드
'''
class Korean2:
    country = '대한민국'    # 클래스 변수의 선언 및 초기화
    # 클래스 메서드의 정의방법
    @classmethod    # @ decorator를 달면 됨,
    def trip(cls, travelling_site):     # cnt
        if cls.country == travelling_site:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korean2.trip('대한민국')
Korean2.trip('미국')

person2 = Korean2()
person2.trip('일본')      # 객체명.클래스메서드() 호출도 가능하긴함. 마찬가지로 권장되진않음.

'''
3. 정적 메서드 (static method)
    정적 메서드 또한 self를 쓰지않음. 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미. self.속성명을 사용하여 인스턴스 변수의 값을 참조 하는데 정적 메서드는 아예 첫번째 매개변수가 고정되어있지 않습니다. - 인스턴스 변수를 참조하지 못한다는 점에서 클래스 메서드와의 공통점에 해당
    
    인스턴스를 생성하지않아도 사용할수 있음 - 클래스 메서드와의 공통점 # 2
    
    특징:
        1) 인스턴스 / 클래스로 호출가능 -> 클래ㅔ스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호ㅓ출 가능 -> 클래스 메서
        3) 데코레이터를 포기하고 작성 -< 클래스 메서드 와의 차이점 1
        3) 반드시 작성해야하는 매개변수가 없음. 클래스 메서드와의 차이점 2
        
이상을 토대로 정적 메서드는 self/cls를 둘다 사용하지 않기 때문에 인스턴스 클래스 변수를 모두 사용하지않는 메소드를 정의하는 경우에 적합

즉 자바에서의 정적 메서드 = 파이썬 클래스 메서드 +정적 메서드
'''

class Korean3:
    country = '한국'

    @staticmethod
    def slogan():
        print('imagine Your Korea')

    @staticmethod
    def slogan2():
         print(f'imagine Your Korea')

# static method 호출
Korean3.slogan()
Korean3.slogan2()

'''
기본예제
가방을 만들때마다 현재 만들어진 가방이 몇개인지 계산할수있는 bag클래스를 정의
'''
class Bag:
    cnt = 0

    def __init__(self): # 여기 내부나 인스턴스메서드 내부에서 self쓰면 속성이 선언됨.
        Bag.cnt += 1    # cls.cnt가 아니라 Bag.cnt라는데에 주목
        # 즉, 생성자는 인스턴스 메서드이기 때문에 인스턴스 메서드 내에서 클래스 변수를 참조할때는 cls.클래스변수명이 아니라 클래스명.클래스변수명으로 참조해야 된다는 점이 중요함.
        print('가방 객체가 생성되었습니다')
    # 클래스 메서드 정의
    @classmethod
    def sell(cls):
        print('가방이 팔렸습니다,')
        cls.cnt -= 1

    @classmethod
    def remain(cls):
        return cls.cnt

# 객체 생성
bag1 = Bag()
print(f'현재 가방 재고 : {Bag.cnt}')  # 인스턴스메서드를 통해 클래스 변수의 값을 바꿧음. 이 값은 모든 Bag클래스의 인스턴스 들이 공유한다는점에서 정적변수 개념과 동일함,
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 재고 : {Bag.cnt}')
bag1.sell()
print(f'현재 가방 재고 : {Bag.cnt}')

'''
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''

class Person:
    population = 0

    def __init__(self,name):
        self.name = name
        Person.population += 1
        print(f'{self.name}이(가) 태어났습니다.')

    def __del__(self):
        print(f'RIP {self.name}')
        Person.population -= 1

    @classmethod
    def get_population(cls):
        return Person.population

man = Person('김일')
woman = Person('감이')

print(f'전체 인구수 : {Person.get_population()}')

del man