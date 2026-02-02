# 초기 설정
import random

# 단어 리스트 설정
word_list = ['apple', 'banana', 'camel']

# 랜덤 변수 설정
chosen_word = random.choice(word_list)
print(f'테스트단어 : {chosen_word}')
# 빈 display 설정
display = []

for _ in range(len(chosen_word)):
    display.append('_')

'''
''.join(반복 가능 객체) method : '.' 앞에 있는 ㅂ문자열을 기준으로 반복가능 객체의 element들을 합펴서 str로 만들어주는 method
'''

# temp = ['s','q','l','d']
# test = ''.join(temp)
# print(test)
# test = '/'.join(temp)
# print(test)
# test = ' '.join(temp)
# print(test)

# todo - 1 : 사용자가 추축을 반복할 수 있도록 while 반복문을 작성하시오. 사용자가 chosen_word의 모든 문자열을 맞추었을때 , 즉 display에 '_'가 없을때 반복문을 중단시킬것. 반복문 종료 후 '정답입니다'를 출력하도록 작성하시오
while '_' in display:
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for _ in range(len(chosen_word)):
        if guess == chosen_word[_]:
            display[_] = chosen_word[_]
    print(' '.join(display))
    if '_' not in display:
        break
print('정답입니다.')

# todo - 2 : 정답을 보여줄때 apple이라면 a p p l e 로 출력 될수 있도록 .join() 메서드를 활용하시오.

