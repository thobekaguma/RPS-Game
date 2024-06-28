import random
import tkinter as tk


def welcome():
    text = """
    Welcome to the classic game of Rock, Paper, Scissors implemented in Python!\n
    In this simple yet engaging game, you'll compete against the computer in a battle of wits and strategy.\n
    The rules are straightforward:\n
    1. ROCK (R) - crushes scissors
    2. SCISSORS (S) - cuts paper
    3. PAPER (P) - covers rock\n
    Your task is to outsmart your opponent by selecting the winning choice in each round.\n
    So, get ready to flex your decision-making skills and embark on an exciting journey of chance and strategy!\n
    Let's see if you can emerge victorious in this timeless showdown.
    """
    display_message = tk.Label(text=text, bg="darkgrey", fg="#301934", font=("",10, "bold"))
    display_message.pack()
    button = tk.Button(window, text="BEGIN", font=("Arial", 10, "bold"), bg="white", padx=15, pady=10, command=get_user_choice)
    button.pack()


def get_user_choice():
    for widget in window.winfo_children():
        widget.destroy()

    prompt = tk.Label(window, text="Enter either 'R', 'P' or 'S' to make your choice: ", fg="#301934", font=("",15, "bold"), pady=10)
    prompt.pack()

    user_choice_var = tk.StringVar()
    entry = tk.Entry(window, textvariable=user_choice_var)
    entry.pack(padx=20, pady=50)

    def get_choice():
        user_choice = entry.get().strip().upper()

        if user_choice in ["R", "P", "S"]:
            if user_choice == "R":
                user_choice = "ROCK"
            elif user_choice == "P":
                user_choice = "PAPER"
            else:
                user_choice = "SCISSORS"
            display_results(user_choice)
        else:
            error_label = tk.Label(window, text="INVALID CHOICE. Choose either 'R', 'P' or 'S'")
            error_label.pack()

    button = tk.Button(window, text="Submit", command=get_choice)
    button.pack()


def generate_computer_choice():
    choices = ['ROCK', 'PAPER', 'SCISSORS']
    computer_choice = random.choice(choices)
    # print(computer_choice)
    return computer_choice


def display_results(user_choice):
    for widget in window.winfo_children():
        widget.destroy()

    computer_choice = generate_computer_choice()
    result = f"You chose {user_choice} and computer chose {computer_choice}\n"

    if user_choice == computer_choice:
        result = f"Great minds think alike! You both choose {computer_choice}."

    elif user_choice == 'ROCK' and computer_choice == 'PAPER':
        result +='Paper covers rock. COMPUTER WINS!'

    elif user_choice == 'SCISSORS' and computer_choice == 'ROCK':
        result +='Rock smashes scissors. COMPUTER WINS!'

    elif user_choice == 'PAPER' and computer_choice == 'SCISSORS':
        result +='Scissors cuts paper. COMPUTER WINS!'

    elif user_choice == 'PAPER' and computer_choice == 'ROCK':
        result +='Paper covers rock. YOU WIN!'

    elif user_choice == 'ROCK' and computer_choice == 'SCISSORS':
        result +='Rock smashes scissors. YOU WIN!'

    elif user_choice == 'SCISSORS' and computer_choice == 'PAPER':
        result +='Scissors cuts paper. YOU WIN!'

    result_label = tk.Label(window, text=result)
    result_label.pack()

    exit_button = tk.Button(window, text="REPLAY", command=get_user_choice)
    exit_button.pack()
    exit_button = tk.Button(window, text="EXIT", command=window.destroy)
    exit_button.pack()



window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("700x400")
window.configure(bg='darkgrey')
welcome()

window.mainloop()