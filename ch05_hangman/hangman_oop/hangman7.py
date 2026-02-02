import random
from hangman_arts import *
# arts파일의 전체 데이터를 가지고옴
from hangman_word_list import word_list
# word_list 변수만 가지고온다는 의미

print(logo)

# 위와 같이 작성한 것을 기준으로 hangman을 완성

chosen_word = random.choice(word_list)

display = []

for i in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False

while not end_of_game and lives > 0:
    print(stages[lives])
    print(' '.join(display))

    guess = input('알파벳을 입력 하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1

    if '_' not in display:
        print(stages[lives])
        print(' '.join(display))
        print('정답입니다')
        end_of_game = True

if lives == 0:
    print(stages[lives])
    print(' '.join(display))
    print('실패!')
    print(f'정답: {chosen_word}')