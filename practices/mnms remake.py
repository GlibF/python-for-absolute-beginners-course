import random


def main():
    show_header()
    play_game()


def show_header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")
    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def play_game():
    mm_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0

    while attempts < attempt_limit:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)
        check_guess(mm_count, guess)
        attempts += 1
    else:
        print(f"Bye, you're done in {attempts}! The answer was {mm_count}.")


def check_guess(mm_count, guess):
    if mm_count == guess:
        print(f"You got a free lunch!.")
        return False
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")


if __name__ == '__main__':
    main()
