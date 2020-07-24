import random


def main():
    show_header()
    play_game("You", "Computer")


def show_header():
    print("----------------------")
    print("rock-paper-scissors V1")
    print("----------------------")


def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper', 'scissors']

    while wins_p1 < rounds and wins_p2 < rounds:

        roll1 = get_roll(player_1, rolls)
        roll2 = random.choice(rolls)
        # roll2 = get_roll(player_2, rolls)
        if not roll1:
            print("Try again!")
            continue

        print(f"{player_1} rolled {roll1}")
        print(f"{player_2} rolled {roll2}")

        winner = check_for_winner(player_1, player_2, roll1, roll2)

        print("The round is over.")
        if winner is None:
            print("This round was a tie!")
        else:
            print(f"{winner} takes the round!")
            if winner == player_1:
                wins_p1 += 1
            if winner == player_2:
                wins_p2 += 1
        print(f"current score is {player_1}:{wins_p1} - {player_2}:{wins_p2}")
        print()

    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2
    print(f"{overall_winner} wins the game!")


def check_for_winner(player_1, player_2, roll1, roll2):
    # Test for a winner
    winner = None
    if roll1 is roll2:
        print("Play tied.")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    print("available values:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}.{r}")

    roll_text = input("What is your roll?")
    selected_index = int(roll_text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"sorry, {player_name}, {selected_index + 1} is not a valid play.")
        return None

    return rolls[selected_index]


if __name__ == '__main__':
    main()
