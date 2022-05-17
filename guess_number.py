#! /usr/bin/env python3

def check_user_input():
    while True:
        user_input = input("Guess a three digit number: ")
        try:
            if user_input > 999 or user_input < 100:
                print("Please guess a three digit number!")
                continue
            return [int(x) for x in user_input]

        except:
            print("Please guess an integer!")
            continue

def give_hint(solution, user_input):
    if solution == user_input:
        print("You have guessed correctly!")

def ask_to_guess_again():
    pass

def main():
    while True:
        check_user_input()

if __name__ == "__main__":
    main()


