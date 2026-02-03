'''
constructor -> main
아까전에 일종의 setter같은 것을 이용하여 속성에 속성값을 대입해쭷음. 굳이 field선언을 하지 않았는데 method내에서 객체의 속성을 정의할수있다는 점이 특이함. 그런데 이렇게 메서드를 경유하게되면 기본 생성자를 통해 객체를 생성한 후 속성에 값을 대입해야하는 과정을 거쳐야하는것을 알수있음.

객체 생성시 기본생성자 호출 -> set_info() 메서드 호출해서 값 대입.

그러니까 AllArgsConstructor에 해당되는걸 python에서 정의할수 있음.

'''
# 클래스 정의
class Candy:
    def set_info(self,shape,color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')

# 객체 생성시
satang = Candy()
satang.set_info("구형",'갈색')
satang.show_info()
'''
속성 값에 대한 제한이 따로 있지 않다면 굳이 빈 객체를 만들어놓고 거기에 값 대입하는것이 비효율적임. 그래서 우린 전체생성자를 도입함.

Java/JS 에서의 생성자 명은 클래스명과 동일하거나 constructor을 쓰는데 파이썬만 또 다른거 씀. __init__() dla
'''
class Candy2:
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color
        print('사탕 객체 생성')

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')

satang2 = Candy2

'''
소멸자
'''

class Sample:
    def __init__(self):
        print('인스턴스 생성')

    #소멸자 정의
    def __del__(self):
        print('객체 소멸')

# 객체 생성
sample = Sample()

print()
del sample
print('객체 소멸이후 작성한 코드입니다. 프로그램 종료 전에 이미 객체가 삭제 되어있음ㅇ,ㄹ 확인할수있다.')

'''
지금 보니까 코드 다 돌아가면 객체가 소멸되는것 같은데 고ㅜㄷ이 소멸자를 학습하는 이유 -> 객체가 생송되면 메모리 공간을 차지하기 때문에 객체가 생성될때마다 그곳에서 불려나오게됨. 하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지않을때도 여전히 메모리를 차지하기 때문에 소멸자를 통해 경계로 객체를 억제해주게 되면 메모ㅓ리 관리가 된다고 할수있음.

1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB 
'''

class USB:
    def __init__(self,capacity):
        self.capacity = capacity
        print('USB객체가 생성되었습니다.')

    def get_info(self, capacity):
        print(f'{capacity}GB USB')

usb = USB(64)
usb.get_info(64)


class Person:
    def __init__(self,name):
        self.name = name

    def show_info(self,name):
        print(f'{name} is born \n{name} is born')


man = Person('james',)
woman = Person('emily')

del man
