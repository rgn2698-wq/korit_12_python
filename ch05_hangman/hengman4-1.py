#   랜덤 설정
import random


#   기초 설정
word_list = ['apple', 'banana', 'pineapple', 'orange', 'grape', 'mango']
chosen_word = random.choice(word_list)
print(f'테스트 단어:{chosen_word}')
display = []

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화
lives = 6
#todo - 2 : while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될수있도록 조건을 작성


end_of_game = False
while not end_of_game:
    guess = input('알파벳을 입력 하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display.append('_')
        print(' '.join(display))
        if '_' not in display:
            break
if guess not in chosen_word:
    lives -= 1
    print(stages[lives])
    print(f'기회가 {lives}번 남았습니다.')
# lives == 0 일때 게임 종료를 표시해야함
# 정답을 맞췄을때 정답! 을 출력해야됨.
# 맞추거나 틀렸을 경우에 _ p p _ _ 와 같이 안내를 출력해야됨.








# for i, live in enumerate(chosen_word):
#     if live == guess:
#         end_of_game = True
#     lives -= 1
#
# if '_' not in chosen_word:
#     print('성공!')
# else:
#     print('실패!')
# 라고 작성하면 문자 하나 당 일치여부를 확인하기 때문에 예상했던 것과 다르게 맞추더라도 나머지 문자에 대해서 live -=1이 누적적으로 적용됨. 그런데 각 element에 대한 반복 때문에 누적적으로 값이 빠진다면, 반복문 바깥에 따로 작성해주면 됨,