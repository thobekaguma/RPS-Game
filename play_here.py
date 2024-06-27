from cli_version import *
# from gui_version import *


def main():
    print(welcome())
    while True:
        computer_choice = generate_computer_choice()
        user_choice = get_user_choice()
        print("\nYou chose {} and computer chose {}.".format(user_choice, computer_choice))

        if user_choice == computer_choice:
            replay = input("Great minds think alike! You both choose {}. Would you like to go again ?Y/N ".format(computer_choice)).upper()
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

if __name__ == '__main__':
    main()