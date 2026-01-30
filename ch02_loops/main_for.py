"""
for 반복문 :
원래 파이썬 에서의 기본 for문의 경우 향상된 for문이 기본.
하지만 index를 다루는것부터 시작했기 때문에 걔를 기준으로 먼저 설명

이때 중요한것이 range()함수
"""

# 1 ~ 10 까지 출력하는 for문
for i in range(10):
    print(i+1)
'''
이상에서 중요한것은 i가 0부터 시작한다는 점.
range() : 몇번 반복할 것인가를 지정하는 함수. -> 특히 for문과 연계되어 함께 쓰이는 편

range() 함수의 응용
range((시작값), 한계값, (증감값))

시작값 : 생략가능, 생략하면 0부터 시작
한계값 : 명시하지않으면 끝까지 진행
증감값 : 생략가능, 생략할 경우에 1씩 증가.
'''
for i in range(2, 11, 2):
    print(i, end=' / ')
print()
print(i)    # 결과값 : 10

'''
Java에서는 for(int i = 0 ...) 했던 부분에서
System.out.println(i)를 했을때 오류가 발생했음.
while에서와 마찬가지로 지역변수의 범위가 다르다는것을 알수있음.

이상까지 학습했을때 시작값 / 한계값 / 증감값을 정의하게 되는 range()함수가 필수적으로 여겨짐

하지만 기본형태의 python for-loop의 경우의 형식은
for 변수명(자유) in iterable(반복가능객체):
    반복실행문
'''
nums = [1,2,3,4,5]
for i in nums:
    print(i, end=' / ')

print()
if 5 in nums:
    print('5가 리스트에 존재합니다.')
else:
    print('5가 리스트에 존재하지않습니다.')

'''
그러면 Java를 배우는 우리는 익숙하지않지만 in 이 생각보다 엄청 중요함. 
in이 적용된 무언가의 결과값의 자료형은 boolean 형태임. (True / False가 나오는 연산자)
A in B라고 했을때 A라는 요소가 B라는 반복가능 객체 내에 존재하는지를
True / False로 뽑아주게 됨.
'''
print(5 in nums)    # 결과값 : True