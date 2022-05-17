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

def main2():
    try:
        user_input = input()
        user_input = int(user_input)
    
    except ValueError:
        print("Some error!")


def do_continue():
    answer = input("Do you want to continue?").lower()[0]

    if answer == "y":
        pass
        # do continue
    elif answer == "n":
        pass
        # do not continue, exit program
    else:
        print("Give an answer!")

    

def main():
    user_input = input()
    user_input = int(user_input)

if __name__ == "__main__":
    main()


