# play_hangman이라는 함수를 call1() 유형으로 정의하고 호출.

import random
from hangman_arts import *
from hangman_word_list import word_list

print(logo)

chosen_word = random.choice(word_list)

display = []

def play_hangman():
    print(logo)
    chosen_word = random.choice(word_list)
    print(f'테스트 단어 : {chosen_word}')

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

play_hangman()