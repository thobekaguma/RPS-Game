import random

def welcome():

    return """Welcome to the classic game of Rock, Paper, Scissors implemented in Python!\n
    In this simple yet engaging game, you'll compete against the computer in a battle of wits and strategy.\n
    The rules are straightforward:\n
    1. ROCK (R) - crushes scissors\n
    2. SCISSORS (S) - cuts paper\n
    3. PAPER (P) - covers rock\n
    Your task is to outsmart your opponent by selecting the winning choice in each round.\n
    So, get ready to flex your decision-making skills and embark on an exciting journey of chance and strategy!\n
    Let's see if you can emerge victorious in this timeless showdown.
    """


def get_user_choice():
    user_choice = input("Enter either 'R', 'P' or 'S' to make your choice: ").strip().upper()
    if user_choice == "R":
        user_choice = "ROCK"
    elif user_choice == "P":
        user_choice = "PAPER"
    elif user_choice == "S":
        user_choice = "SCISSORS"
    else:
        user_choice = input("\nINVALID CHOICE. Choose either 'R', 'P' or 'S' ")
    return user_choice

def generate_computer_choice():
    choices = ['ROCK', 'PAPER', 'SCISSORS']
    return random.choice(choices)

def main():
    print(welcome())
    while True:
        computer_choice = generate_computer_choice()
        user_choice = get_user_choice()
        print("\nYou chose {} and computer chose {}.".format(user_choice, computer_choice))

        if user_choice == computer_choice:
            replay = input("\nGreat minds think alike! You both choose {}. Would you like to go again ?Y/N ".format(computer_choice)).upper()
            if replay != 'Y':
                break
            continue

        elif user_choice == 'ROCK' and computer_choice == 'PAPER':
            print('\nPaper covers rock. COMPUTER WINS!')

        elif user_choice == 'SCISSORS' and computer_choice == 'ROCK':
            print('\nRock smashes scissors. COMPUTER WINS!')

        elif user_choice == 'PAPER' and computer_choice == 'SCISSORS':
            print('\nScissors cuts paper. COMPUTER WINS!')

        elif user_choice == 'PAPER' and computer_choice == 'ROCK':
            print('\nPaper covers rock. YOU WIN!')

        elif user_choice == 'ROCK' and computer_choice == 'SCISSORS':
            print('\nRock smashes scissors. YOU WIN!')

        elif user_choice == 'SCISSORS' and computer_choice == 'PAPER':
            print('\nScissors cuts paper. YOU WIN!')

        replay = input("\nWould you like to play again? Y/N ").upper()
        if replay != "Y":
            print("\nGoodbye!")
            break
        continue