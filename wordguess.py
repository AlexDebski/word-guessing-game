"""
Word Guessing Game
"""

empty_space = '_ '

all_words = 'learning community zoom health data'
all_words_converted = list(map(list, all_words.split()))
num_words = len(all_words_converted)

user_guess = ''

global guesses_remaining
guesses_remaining = 6

global guessed_letters
guessed_letters = []


def initiate_board(word: list):
    length = len(word)
    global current_board
    current_board = [empty_space] * length

def print_board(board: list):
    for spot in board:
        print(spot, end='')
    print()

def check_input(user_input: str) -> bool:
    #check if letter
    if not is_alpha(user_input):
        return False
    #check length    
    if not is_one_letter(user_input):
        return False        
    return True
  
def is_alpha(user_input: str) -> bool:
    if not user_input.isalpha():
        print('This is not a letter')
        return False
    else:
        return True

def is_one_letter(user_input: str) -> bool:
    if len(user_input) != 1:
        print('Please enter only one letter')
        return False
    else:
        return True
    
def find_letter(word: list, user_input: str) -> bool:
    global current_result
    current_result = []
    for i, letter in enumerate(word):
        if letter == user_input:
            current_result.append(i)
    if current_result:
        return True
    else:
        return False
 
def letters_guessed(user_input: str) -> bool:
    if user_input not in guessed_letters:
        guessed_letters.append(user_input)
        return False
    else:
        return True

def update_board(board: list, result: list, user_input: str):
    for r in result:
        board[r] = user_input

def quit(user_input: str) -> bool:
    if user_input.lower() == '/q':
        print('Thank you for playing')
        return True
    else:
        return False

def is_loss(guesses: int) -> bool:
    if guesses == 0:
        print (f'You have {guesses_remaining} guesses remaining. Please try again!')
        return True
    else:
        return False

def is_word_solved(board: list, spot: str) -> bool:
    if spot not in board:
        return True
    else:
        return False

def is_last_word(index: int, total_words) -> bool:
    if index + 1 == total_words:
        return True
    else:
        return False


for word_index, word in enumerate(all_words_converted):
    if quit(user_guess):
        break
    if guesses_remaining < 1:
        break
    guesses_remaining = 6
    guessed_letters = []
    current_index = word_index
    current_word = word
    initiate_board(current_word)
    print(f'Word {current_index + 1}/{num_words}')    
    while True:
        print(f'Guessed letters: {guessed_letters}')
        print_board(current_board)
        user_guess = input(f'Guess a letter or enter \"/q\" to quit. You have {guesses_remaining} guesses remaining:')
        if user_guess.lower() == '/q':
            break
        if not check_input(user_guess):
            continue
        find_letter(current_word, user_guess)
        if not letters_guessed(user_guess) and not current_result:
            guesses_remaining -= 1
            print('Letter not found')
        if is_loss(guesses_remaining):
            break
        update_board(current_board, current_result, user_guess)
        if is_word_solved(current_board, empty_space) and is_last_word(current_index, num_words):
            print_board(current_board)
            print('You win!')
            break
        if is_word_solved(current_board, empty_space):
            print_board(current_board)
            print('Next word!')
            break





