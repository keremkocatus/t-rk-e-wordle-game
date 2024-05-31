import random
import os

def load_word_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        words = [word.strip().lower() for word in file.readlines()]
    return words

word_list_5 = load_word_list('words_5.txt')
#word_list_6 = load_word_list('words_6.txt')
#word_list_7 = load_word_list('words_7.txt')

word_length = 5
word_list = word_list_5

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def settings():
    global word_length, word_list
    while True:
        clear_terminal()
        print("Settings:")
        print("1. 5-letter words")
        print("2. 6-letter words")
        print("3. 7-letter words")
        print("4. Return to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            word_length = 5
            word_list = word_list_5
            break
        elif choice == "2":
            word_length = 6
            #word_list = word_list_6
            break
        elif choice == "3":
            word_length = 7
            #word_list = word_list_7
            break
        elif choice == "4":
            break

def game():
    global word_length, word_list
    secret_word = random.choice(word_list)
    attempts_left = 6
    guesses = []

    clear_terminal()
    print("Welcome to the Wordle game!")
    print(f"Try to guess a {word_length}-letter word.")
    print("Correct letter and position => Green")
    print("Correct letter but wrong position => Yellow")
    print("Wrong letter => Gray")
    print("\n\n")

    while attempts_left > 0:
        guess = input("Your guess: ").lower()

        if len(guess) != word_length:
            print(f"Please enter a {word_length}-letter word.")
            continue

        if guess not in word_list:
            print("This word is not valid. Please enter a valid word.")
            continue

        if guess == secret_word:
            secret_word_colored = " ".join(["\033[1;32m" + letter + "\033[0m" for letter in secret_word])
            guesses.append(secret_word_colored)
            clear_terminal()
            print(f"Remaining attempts: {attempts_left}")
            for g in guesses:
                print(g)
            print("Congratulations! You guessed the word:", secret_word)
            break

        result = [""] * word_length
        secret_word_copy = list(secret_word)

        for i in range(word_length):
            if guess[i] == secret_word[i]:
                result[i] = "\033[1;32m" + guess[i] + "\033[0m"  # Green
                secret_word_copy[i] = None

        for i in range(word_length):
            if result[i] == "":
                if guess[i] in secret_word_copy:
                    result[i] = "\033[1;33m" + guess[i] + "\033[0m"  # Yellow
                    secret_word_copy[secret_word_copy.index(guess[i])] = None
                else:
                    result[i] = "\033[1;37m" + guess[i] + "\033[0m"  # Gray

        guesses.append(" ".join(result))
        attempts_left -= 1

        clear_terminal()
        print(f"Remaining attempts: {attempts_left}")
        for g in guesses:
            print(g)

    if attempts_left == 0:
        secret_word_colored = " ".join(["\033[1;32m" + letter + "\033[0m" for letter in secret_word])
        print(secret_word_colored)
        print("Unfortunately, you ran out of attempts. The secret word was:", secret_word)

def main_menu():
    while True:
        clear_terminal()
        print("Main Menu:")
        print("1. Play")
        print("2. Settings")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            game()
            input("Game over. Press ENTER to return to the main menu...")
        elif choice == "2":
            settings()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
