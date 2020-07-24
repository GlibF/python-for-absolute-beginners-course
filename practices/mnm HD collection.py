import random


def main():
    show_header()
    play_game()
    retry()


def show_header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def get_guess():
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    return guess


def check_guess(mm_count, guess):
    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")

    return mm_count == guess


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0

    while attempts < attempt_limit:
        guess = get_guess()
        attempts += 1

        winner = check_guess(mm_count, guess)
        if winner:
            break
        elif attempts < attempt_limit:
            continue
        else:
            print(f"Sorry, you ran out of tries, the correct amount was {mm_count}.")
            return False
    if attempts == 1:
        print(f"Bye, you're done in a single attempt!")
    else:
        print(f"Bye, you're done in {attempts} attempts!")


def retry():
    while True:
        try:
            answer = input("Try again?[y/n]")
        except ValueError:
            print("please type: 'y' or 'n'.")
            continue
        if answer == 'y':
            import os
            clear = lambda: os.system('cls')
            clear()
            main()
        elif answer == 'n':
            print("See Ya!")
            break


if __name__ == '__main__':
    main()
