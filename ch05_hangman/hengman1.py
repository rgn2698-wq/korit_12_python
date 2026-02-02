import random
from mimetypes import guess_type

# numbers = [1,...,5]
# chosen_number = random.choice(numbers)
# # ramdom이라는 객체에 choice라는 메서드가 있고, 내부에
# # list 자료형을 넣으면 하나를 넣어서 저장함.
# print(chosen_number)


word_list = ['apple', 'banana', 'camel']
#Todo -1 : word_list에서 하나의 단어를 읨의로 선택하도록 random 모듈을 사용하고, 해당 단어를 chosen_word 변수에 담으시오.
chosen_word = random.choice(word_list)
#Todo -2 : 사용자에게 알파벳 하나를 추측해서 입력하라고 요청하고, 이를 guess 변수에 담으시오. 대문자로 시작하는 경우를 방지하기 위해
# .lower()를 적용하시오
guess = input('단어 입력 >>> ').lower()
#Todo -3 : guess에서 입력한 문자 하나가 chosen_word에 str 문자열 중에 하나의 문자와 일치하는지 확인할수 있도록 조건-반복문을 작성하고
# 맞으면 정답 / 틀리면 오답이라고 출력하시오.
for correct in chosen_word: # camel 이라면 c, a
    if correct == guess:
        print('정답')
    else:
        print('오답')

for i in range(len(chosen_word)):
    if chosen_word[1] == guess:
        print('2 : 정답')
    else:
        print('2 : 오답')




