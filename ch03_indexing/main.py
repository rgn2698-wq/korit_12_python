str_example = 'hello, Python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])

print(len(str_example))     # 결과값 : 14
'''
len() : 반복가능 객체의 전체 인덱스 값을 return하는 함수
'''

# 일반 for문으로 Hello, Python!을 한줄로 출력

# for st in (len(str_example)):
#     print(st, end='')

# 향삳된 for 문으로 Hello, Python!을 한줄로 출력
for str in str_example:
    print(str, end='')

'''
마이너스 인덱스 : 문자열의 뒤에서 부터 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱 : 문자열의 인덱스를 활용하여 한 문제 이상으로 구성된 단어나 문장을 추출할때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스의 종료인덱스를 통해 그 사이문자들을 추출하는것이 가능함.
    
형식 :
변수명[시작 인덱스 : 종료인덱스 : 증감값]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략 하면 끝까지 추출
증감값 : 생략하면 1씩 증가 (인덱스 넘버가 0부터 1식 증가)
'''
print()
print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])
# 시작지점 (0)번지 부터 뒤에서 3번째 인덱스 미만 까지만 출력한다는 의미

'''
range(시 종 증)이랑 변수명[시 종 증]이랑 같아보임
이유는?

기본 예제
네 자리 숫자를 입력받아 그 자리의 맨 마지막 숫자를 출력하시오

실행예 
네자리 숫자를 입력하세요 >>> 2026
맨마지막 숫자는 6입니다.
맨 마지막 숫자는 6이며 짝수입니다.
'''

nums = input('네자리 숫자를 입력하세요 >>> ')
print(f'맨 마지막 숫자는 {nums[-1]} 입니다')

if int(nums[-1]) %2 == 0:
    print(f'맨 마지막숫자는 {nums[-1]}이며 짝수입니다.')
else:
    print(f'맨마지막 숫자는 {nums[-1]}이며 홀수입니다.')

result = (int(nums[-1]) % 2== 0 for num in nums)

'''
python 삼항 연산자
if -else 구조를 한줄로 줄여서 씀
'''

result = '짝수' if int(nums[-1]) %2 == 0 else '홀수'

print(f'맨 마지막 숫자는 {nums[-1]}이며 {result} 입니다')

# ch04_functions