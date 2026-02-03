'''
딕셔너리 기반의 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름의 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름의 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름의 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.

collections + function

숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)          # call2() 유형
print(add_numbers2(last_num))   # call4() 유형

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]

예를 들어 hello = ['안', '녕', '하', '세', '요']라는 list가 있다고 가정했을 때,
add_numbers3(10, hello)를 호출하면
[1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
라는 결과값을 만드는 함수를 정의한다면 어떻게 할 수 있을지 고민해보세요.
'''

contact = {}

for i in range(1,4):
    name = input(f'{i}번째 사람의 이름을 입력하세요 >>> ')
    phone = input(f'{i}번째 사람의 전화번호를 입력하세요. >>> ')
    contact[name] = phone
print(f'입력받은 연락처는 {contact}입니다.')

num = int(input("숫자 몇 까지 입력하시겠습니까? >>> "))

number = []

def add_numbers1(n):
    for i in range(1, n + 1):
        number.append(i)
    print(number)

def add_numbers2(n):
    number = []
    for i in range(1, n + 1):
        number.append(i)
    return number

add_numbers1(num)
print(add_numbers2(num))


def add_numbers3(n, li):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    result.extend(li)
    return result

hello = ['안', '녕', '하', '세', '요']
print(add_numbers3(10, hello))