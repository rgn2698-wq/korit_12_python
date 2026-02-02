# '''
# python 대표 collection 종류
#     1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서있음
#     2. tuple 튜블 : 추가 / 수정 / 삭제가 불가능 / 순서있음
#     3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
#     4. dict 딕셔너리 : 키 + 값 으로 분리
# '''
#
# list_example = [30, 40, '김이',[100, '김삼']]
# print(list_example)
#
# tuple_example = (10, 20, 30, '김사')
# print(tuple_example)
#
# set_example = {1100, 200, 300, 400, '김오'}
# print(set_example)
#
# dict_example = {'이름': "김일", '나이': 20, '학교':'코리아아이티'}
# print(dict_example)
# '''
# 1. list : 여러 값을 저장할때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능. Java가준 하나의 배열에 동일한 자료형만 들어갈수 있는것과 달리 강점을 가짐.
# '''
#
# # list의 선언 및 초기화
# li1 = [1,2,3,'김사']
# '''
#     1. list의 index / slice
#     list는 str과 동일한 방식의 index / slicing을 지원
#     1) 인덱스 / 마이너스 인덱스
# '''
# print(li1)
# print(li1[0])
# print(li1[1])
# print(li1[2])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])
# '''
#     2) slicing
#     str의 slicing과 같이 '시작인덱스:종료인덱스:증감값' 으로 이루어져있음.
# '''
# li2 = [100, 3.14, 'hello']  # list 선언 밑 초기화방법 #1
# li3 = list((4,5,6,7,8,9,10))    # list 선언 및 초기화 방법 #2
# print(li3[0:4:2])               # 시작 인덱스 부터 4번지 앞까지 2씩 증가
#                                 # 이런거 해석하는게 종종 나왔었음.
# '''
#     3) list의 element 추가와 삭제
#         list에 새로운 요소를 추가할 떄는 아까 한것 처럼 .append()를 사용할수 있음. 그리고 .insert()조 존재함
#
#         .append() - 항상 마지막 인덱스에 element를 추가
#         .insert(위치,값) - 정해진 위치 (인덱스)에 값 을 추가
# '''
#
# scores = [3,4,5]
# print(scores)
# scores.append(6)
# scores.insert(7,90)
# print(scores)
# '''
#         .pop()의 경우 NoArgs라면 맨 마지막 element가 삭제됨.
#         .pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 element를 삭제함
# '''
# print(scores.pop())     # 결과값 : 맨 마지막 인덱스의 element를 삭제 후 return함
# print(scores.pop(0))
# print(scores)
# '''
#         교재에는 없지만 수업하는 삭제 메서드 : .remove(값) - list 내에 해당 값을 찾아내서 삭제함(인덱스가 아님.)
# '''
# scores.remove(90)
# # scores.remove(0)        # 추후 예외처리 형태로 넘어갈수 있음.
# print(scores)

'''
li4 리스트를 선언하고, 1부터 10까지 집어넣어 보세요.
print(li4)결과값은 [1,2,3,4,5,6,7,8,9,10]

각 list내의 element들을 뽑아내서 *2씩 하는데
일반 for문 형식으로 한번
enhanced for문 형식으로 한번 해서 첫번째 element가 4가 되어야함.
'''

li4 = []

for i in range(1, 11):
    li4.append(i)

for i in range(len(li4)):
    li4[i] = 2*li4[i]


# for num in li4:
#     num = num *2
#     print()
#   귀찮다는걸 알았음. 사실상 list내에서의 ㄷelemnet들에대해 연산을 일광적으로 적용하는 method가 따로 있음. JS에서도 해본적이 있음.
print(li4)

modified_li4 = (map(lambda num: num*2,li4))
# 이상의 경우가 극단적으로 list의 내부 각각의 element들에 동일한 함수를 적용한 결과를 적용하는 map()함수임. 그런데 JS에서 배열의 method로 사용했었음. 이상의 코드가 좀 문제가 있다면 map()함수의 결과값이 map객체의 해달하기 때문에 list()함수를 통한 형변환을 해줘야함.
print(modified_li4)

'''
    2. tuple(튜플) : 지정된 값을 변경할수 없는 list. 순서는 있기때문에 index 넘버의 사용과 slicing은 사용가능 하지만 추가 / 수정 / 삭제 불가능.
'''
tu1 = (1,2,3)           # 튜플 생성 방법 # 1
tu2 = tuple((4,5,6))    # 튜플 생성 방법 # 2
tu3 = 7,8,9             # 튜플 생성 방법 # 3

print(type(tu3))    # 결과값 : <class 'tuple'>
a, b, c = 7, 8, 9       # 복수의 변수 선언 및 초기화 방법 -> 변수 개수와 데이터 개수가 같으면 알아서 '순서대로'ㄴ나열됨

tu5 = 'hello. ', 'good morning. ', 'my name is. ', 'kim-il ', 'i am ', '20', 'years old'
for word in tu5:
    print(word.title(),end='')
    # 결과값 : Hello. Good Morning. My Name Is. Kim-Il I Am 20Years Old
print()

'''
이상의 예시를 남겨두는 이유는 우리가 배우는 콜렉션의 개념과 내부 element의 자료들이 서로 다르다는 점 때문임. tuple 자체는 추가 / 수정 / 삭제 가 불가능 했었음.
그런데 내부 element 자체는 str이니까 데이터의 가공이 가능함.

    3. set 세트
        : 수학의 집합 개념, Java와 동일
'''
set1 = {1,2,3}          # 세트 생성 방법 # 1
set2 = {4, 5, 6}  # 세트 생성 방법 # 2

# 비어있는 list / tuple / set 생성 방법
# li = []
# tu = ()
# set = {}        # 이러면 dict이 만들어짐
# se1 = set({})   # 그래서 이래야만 빈 set가 생성되기 때문에 위에서 생성한거랑은 다름
# print(type(li))
# print(type(tu))
# print(type(set))
'''
list/tuple은 index가 존재한다고 했음. 그래서 이렇게 인덱스가 존재하는 애들을 sequence로 분류하고, set/dictionary의 경우에는 인덱스가 없기 때문에 비시퀀스라는 표현을 쓰기도 함.

    set 관련 메서드'
    1. .add() - set에 새로운 element추가
    2. .remove() - 기존 element삭제 -> index가 없으니 pop()이 없음
    3. .discard() - 기존 element삭제
'''
se3 = {10,20,30}
se3.add(50)
print(se3)      # 결과값 : {10, 20, 50, 30}
se3.remove(30)  # 순서가 없기 때문에 값을 명확하게 입력해야 됨.
print(se3)

# remove() vs discard()
# se3.remove(70)
# print(se3) # 오류발생
se3.discard(70)
print(se3)  # 오류발생 안함.
'''
.remove()의 경우 argument로 set 내에있는 값을 정확하게 입력하지않으면 키에러 예외가 발생함. 반면에 discard()의 경우에는 set내에 없는 값을 입력했을 경우 해당 값이 애초에 존재하지 않기때문에 변함없는 상태로 메소드가 종료됨.
'''

# 인덱스 넘버는 없지만 향상된 for문으로 내부 element를 출력할수는 있음
for num in se3:
    print(num)      # 순서는 무작위
'''
    4. dict(ionary) - Java에서의 Map / JS 에서의 object / JSON과 비슷한 형식

'''
dict1 = {
    '이름' : '김일',
    '나이' : 20,
    '주소' : ['서울특별시','마포구','목동']
}
'''
전에 수업한것처럼 168번 라인까지 ket-value pair이 있는데 나중에 학교라는 key를 추가하려고 할 때, 168번 라인에 콤마 치고 엔터치고 '학교' : '코리아아이티' 같은 식으로 추가하기 번거로우니까 나중에 확장성을 위하여 미리 콤마 쳐두는 편임. 그러면 그냥 169번 라인에 추가 property를 넣으면 됨.

중요하게 반복적으로 말하는 부분 dict에서 반복문 돌리면 key가 나옴
'''
for key in dict1:
    print(key)

# 그렇다면 value를 확인하기 위해서는
for key in dict1:
    print(dict1[key])

# key들만 추출하는 메서드
print(type(dict1.keys()))       # 결과값: <class 'dict_keys'>
print(list(dict1.keys()))       # 결과값: ['이름','나이','주소']
# value들만 추출 하는 메서드
print(dict1.values())
print(type(dict1.values()))

# key들 혹은 value들만 추출해서 list를 만들고싶다면 list() 형변환 함수를 사용해야함.

'''
그래서 collections 수업을 할때 매우 중요한 점은 list를 배웠을때 list만 고려할 것이 아니라 set / tuple / dict로 자료형을 변경하는것이 가능한가 임

    1) dict 에서 property 추가 / 삭제
'''
dict1['직업'] = '웹 퍼블리셔'  # 기존에 없는 ket를 입력하고 = value 하면 됨.
print(dict1)
dict1['직업'] = '웹 개발자'   # key 하나당 value는 동일하기 때문에 재대입이 이루어짐.
print(dict1)

print(dict1.pop('직업'))      # 키를 알아야지 삭제 가능함. .pop()의 리턴특성이 중요함. 그러면 최종 벨류가 뽑혀져 나올테니까 결과값 : 웹 개발자

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그
list에서 2 번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40

'''

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list = li[2:7]

print(list)

print(list[1])

'''
사용자로부터 1에서 12사이의 월을 입력 받아. 해당월이 몇일까지 있는지 출력하는 프로그램을 작성하시오 (윤년은 고려 안함)

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일 까지입니다.
# 1 : dictionary를 이용하는 방법
# 2 : list를 이용하는데 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]을 이용하는 방법
# 3 : list를 이용하는데 [28, 30, 31]을 이용하는 방법
'''

# 1 번 해답
month = int(input('1 ~ 12 사이의 월을 입력하세요. >>> '))
m_days = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
print(f'{month}월은 {m_days[month]}일 까지 입니다.')

# 2 번 해답
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(f'{month}월은 {day[month-1]}일 까지 입니다.')

# 3 번 해답

days = [28, 30, 31]
if month == 2:
    print(f'{month}월은 {days[0]}일 까지 입니다.')
elif month == [4,6,9,11]:
    print(f'{month}월은 {days[1]}일 까지 입니다.')
elif month == [1,3,5,12]:
    print(f'{month}월은 {days[2]}일 까지 입니다.')
else:
    print('1 ~ 12까지의 숫자를 적어주세요.')


