import random


word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(f'테스트단어 : {chosen_word}')

# todo - 1 : 비어있는 list인 display를 만드시오.
display = []
# list에 element를 추가하는 메서드 : .append()
# display.append('김')
# display.append('엄')
# print(display)
# display[1] = 1      # 인덱스가 생겨서 가능
# print(display)
# display[4] = 4      # 인덱스가 아직 없어서 불가능
# print(display)
guess = input('단어 입력 >>> ').lower()
# todo - 2 : 이상의 코드 라인을 참조하여 chosen_word의 각 문자 개수마다 '_'를 추가 하시오. 예를 들어 chosen_word == 'apple' 이라면 display = [ '_', '_', ... ]으로 만들어 져야함
for _ in range(len(chosen_word)):
    display.append('_')
# todo - 3 : chosen_word의 각 문자들을 반복 시켰을때 그 위치가 guess와 일치 한다면 해당 위치의 display에 문자를 공개합니다. 예를 들어 chosen_word가 apple 이고 guess == 'p'라면 display [ '_', 'p', 'p', '_', '_' ]로 바뀌어야 함.
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess
print(display)