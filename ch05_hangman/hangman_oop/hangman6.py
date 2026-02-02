import random
import hangman_arts
import hangman_word_list
# import 다음에 파일명을 썻다는것에 주목해야 됨. 이 파일 하나를 파이썬에선 module(모듈) 이라고 함.

# 외부의 hangman_word_list에 있는 word_list 변수를 참조해서 chosen_word를 만들 필요가 있음.

print(hangman_arts.logo)
# 위가 힌트, 그러면 chosen_word를 불러올수 있도록 코드를 작성
chosen_word = random.choice(hangman_word_list.word_list)
print(f'테스트 단어 : {chosen_word}')
# 나머지 부븐을 잘 복사한 다음에 오류 생기는 부분을 수정

display = []

for i in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False

while not end_of_game and lives > 0:
    print(hangman_arts.stages[lives])
    print(' '.join(display))

    guess = input('알파벳을 입력 하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1

    if '_' not in display:
        print(hangman_arts.stages[lives])
        print(' '.join(display))
        print('정답입니다')
        end_of_game = True

if lives == 0:
    print(hangman_arts.stages[lives])
    print(' '.join(display))
    print('실패!')
    print(f'정답: {chosen_word}')