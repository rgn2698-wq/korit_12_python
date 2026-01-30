'''
1. while 반복문
    while다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨.(조건이 Flase가 될때까지)
형식 :
while 조건식1:
    반복 실행문1

특정 시점에 while 반복문이 정료될수 있도록 지정해야됨.
중첩 while문 도 가능

기본 예제
1부터 10까지 출력하기
'''

# n = 1
# while n < 11:
#     print(n, end=' / ')
#     n += 1      # Python엔 ++가 없음.

'''
기본 예제 #2
10부터 1까지 역순으로 출력
'''
# print()
# n2 = 10
# while n2 > 0:
#     print(n2, end=' / ')
#     n2 -= 1

dan = 2
while dan <= 9:                                     # 조건문
    number = 1                                      # 반복실험문
    while number <= 10:                             # 조건문2
        print(f'{dan} x {number} = {dan*number}')   # 반복실행문
        number += 1
    dan += 1                                        # 반복실행문 1-b
    print()

print(number)           # 전역 / 지역 변수의 개념이 Java와 다름.