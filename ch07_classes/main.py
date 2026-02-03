'''
클래스 정의 형식 :

class 클래스명(파스칼케이스):
    본문 (attribute / method)

객체 생성 형식:
객체명 = 클래스명()        # 생성자 호출은 맞지만 new가 없음

'''
# 클래스 정의 예시
class WaffleMachine:
    pass        # 클래스나 함수에 쓰면 엔터 쳤을때 오류 안남

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle)       # 결과값 : <__main__.WaffleMachine object at 0x00000206F36DB230>

'''
클래스의 구성

1. 클래스의 기본 유형
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지님 (Java때 방이 가져야할 구성요소에 대해 물었었음.) 객체를 생성하기 위해서는 객체가 가져야할 '값'과 '기능'을 지녀야함.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수(Java에서는 Static 변수라고 불렀음)
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 인스턴스 메서드
        3) 정적 메서드
        
    Java에서는 this를 썻지만( 아직 정의중인 클래스에 대한 객체가 생성될 수 없으니 임의로 this 키워드를 썻었음) python에선 self를 씀.
    
    self 키워드 : 인스턴스 변수에서 각각의 객체를 의미하기 위해 self 키워드를 붙여줌, 인스턴스 메서드에서의 첫번째 매개변수로 '항상' self를 추가해야됨.(자동생성)
'''

# 클래스 정의
class Person:
    # 메서드정의 ( 들여쓰기 주의 )
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

    def show_info2(self):
        return (f'제 이름은 {self.name}이고 {self.age}살 입니다, '
                f'\n연락처는 {self.tel}이고, {self.address}에 살고있습니다.')

# 객체 생성
person1 = Person()
# Person 클래스의 인스턴스에서 인스턴스 메서드 호출
person1.set_info(age=20, tel='010-1234-5678', address='부산광역시 부산진구', name='김일')
# 이상의 코드에서 키워드를 씀. 어떤 속성이 어떤값을 넣는지 아니까 자바의 빌더는 필요 없음
person1.show_info2()
print(person1.show_info2())

