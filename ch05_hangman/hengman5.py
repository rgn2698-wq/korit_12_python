# ascii art 를 통해 hangman logo를 만들고 logo 변수에 대입

# 첫 시작시에만 print(logo)가 실행 될수 있게끔 작성

# 생성형 ai에 word_list를 400개를 만들어 달라고 해서 붙여 넣기

# 전체 hangman 만들기


# 초기 설정
import random

# 단어 리스트 설정 (400개)
word_list = ['apple', 'banana', 'camel', 'orange', 'grape', 'mango', 'peach', 'pear', 'plum', 'cherry', 'lemon',
 'lime', 'melon', 'papaya', 'guava', 'apricot', 'fig', 'date', 'kiwi', 'coconut', 'strawberry',
 'blueberry', 'raspberry', 'blackberry', 'cranberry', 'pineapple', 'pomegranate', 'watermelon',
 'cantaloupe', 'nectarine', 'car', 'truck', 'train', 'plane', 'boat', 'ship', 'bicycle',
 'motorcycle', 'scooter', 'bus', 'road', 'street', 'bridge', 'tunnel', 'station', 'airport',
 'harbor', 'garage', 'engine', 'wheel', 'house', 'home', 'room', 'kitchen', 'bathroom',
 'bedroom', 'garden', 'window', 'door', 'roof', 'table', 'chair', 'sofa', 'bed', 'pillow',
 'blanket', 'lamp', 'clock', 'mirror', 'curtain', 'book', 'paper', 'pencil', 'pen', 'eraser',
 'notebook', 'folder', 'letter', 'stamp', 'envelope', 'school', 'class', 'teacher', 'student',
 'lesson', 'homework', 'exam', 'grade', 'library', 'campus', 'music', 'song', 'guitar', 'piano',
 'violin', 'drum', 'trumpet', 'flute', 'singer', 'band', 'movie', 'film', 'actor', 'actress',
 'director', 'screen', 'camera', 'studio', 'ticket', 'theater', 'game', 'player', 'score', 'level',
 'quest', 'puzzle', 'battle', 'winner', 'loser', 'coach', 'computer', 'laptop', 'tablet', 'phone',
 'keyboard', 'mouse', 'monitor', 'printer', 'router', 'server', 'internet', 'website', 'browser',
 'email', 'message', 'password', 'account', 'profile', 'download', 'upload', 'robot', 'machine',
 'sensor', 'circuit', 'battery', 'signal', 'program', 'coding', 'python', 'variable', 'function',
 'loop', 'string', 'number', 'boolean', 'object', 'module', 'package', 'script', 'debug', 'science',
 'atom', 'molecule', 'energy', 'gravity', 'planet', 'galaxy', 'comet', 'meteor', 'telescope',
 'nature', 'forest', 'river', 'ocean', 'mountain', 'valley', 'desert', 'island', 'beach',
 'waterfall', 'weather', 'cloud', 'rain', 'storm', 'thunder', 'lightning', 'snow', 'wind', 'fog',
 'sunshine', 'animal', 'dog', 'cat', 'horse', 'cow', 'sheep', 'goat', 'pig', 'rabbit', 'mouse',
 'lion', 'tiger', 'bear', 'wolf', 'fox', 'deer', 'monkey', 'panda', 'zebra', 'giraffe', 'bird',
 'eagle', 'hawk', 'owl', 'sparrow', 'parrot', 'penguin', 'swan', 'duck', 'goose', 'fish', 'shark',
 'whale', 'dolphin', 'octopus', 'squid', 'crab', 'lobster', 'turtle', 'seal', 'insect', 'ant',
 'bee', 'butterfly', 'mosquito', 'dragonfly', 'ladybug', 'spider', 'scorpion', 'beetle', 'flower',
 'rose', 'tulip', 'lily', 'orchid', 'daisy', 'sunflower', 'violet', 'lavender', 'jasmine', 'tree',
 'oak', 'pine', 'maple', 'birch', 'cedar', 'willow', 'palm', 'bamboo', 'cactus', 'food', 'bread',
 'cheese', 'butter', 'milk', 'yogurt', 'egg', 'rice', 'pasta', 'noodle', 'soup', 'salad', 'pizza',
 'burger', 'sandwich', 'steak', 'chicken', 'beef', 'pork', 'fishcake', 'salt', 'sugar', 'pepper',
 'garlic', 'onion', 'ginger', 'cinnamon', 'vanilla', 'chocolate', 'honey', 'drink', 'water',
 'coffee', 'tea', 'juice', 'soda', 'milkshake', 'smoothie', 'cocoa', 'lemonade', 'color', 'red',
 'blue', 'green', 'yellow', 'purple', 'orangecolor', 'black', 'white', 'gray', 'silver', 'gold',
 'bronze', 'pink', 'brown', 'cyan', 'magenta', 'navy', 'teal', 'maroon', 'time', 'day', 'night',
 'morning', 'evening', 'noon', 'midnight', 'minute', 'second', 'week', 'month', 'year', 'spring',
 'summer', 'autumn', 'winter', 'holiday', 'birthday', 'festival', 'weekend', 'city', 'village',
 'country', 'capital', 'market', 'store', 'shop', 'mall', 'museum', 'park', 'hotel', 'restaurant',
 'cafe', 'office', 'factory', 'farm', 'hospital', 'clinic', 'pharmacy', 'bank', 'friend', 'family',
 'mother', 'father', 'sister', 'brother', 'uncle', 'aunt', 'cousin', 'neighbor', 'person', 'child',
 'adult', 'teen', 'baby', 'woman', 'man', 'hero', 'villain', 'leader', 'emotion', 'happy', 'sad',
 'angry', 'calm', 'brave', 'shy', 'proud', 'afraid', 'excited', 'action', 'run', 'walk', 'jump',
 'swim', 'fly', 'drive', 'read', 'write', 'draw', 'think', 'pneumonoultramicroscopicsilicovolcanoconiosis']

# 랜덤 변수 설정
chosen_word = random.choice(word_list)
print(f'테스트단어 : {chosen_word}')

# 빈 display 설정
display = []

for i in range(len(chosen_word)):
    display.append('_')

# ascii art 를 통해 hangman logo를 만들고 logo 변수에 대입
logo = """║▌│█║▌│ █║▌│█│║▌║
𝙨𝙘𝙖𝙣𝙣𝙞𝙣𝙜 𝙘𝙤𝙙𝙚..."""

# 첫 시작시에만 print(logo)가 실행 될수 있게끔 작성
print(logo)

# 전체 hangman 만들기
stages = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

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





