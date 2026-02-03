'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개변수 : list인 numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''

def count_even_odd(numbers):
    e_cnt = 0
    o_cnt = 0
    for n in numbers:
        if n % 2 ==0:
            e_cnt += 1
        else:
            o_cnt += 1

    print(f'짝수의 개수 : {e_cnt}개')
    print(f'홀수의 개수 : {o_cnt}개')

# count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
count_even_odd(range(1,1239))
