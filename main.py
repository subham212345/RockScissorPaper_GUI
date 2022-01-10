from tkinter import *
from random import randint

# Creating the window with green background and giving it the title: Rock Paper Scissor
window = Tk()
window.title("Rock Paper Scissor")
window.configure(background="green")

# Creating the image files for each image
image_rock_user = PhotoImage(file="user_rock.png")
image_paper_user = PhotoImage(file="user_paper.png")
image_scissor_user = PhotoImage(file="user_scissor.png")
image_rock_computer = PhotoImage(file="computer_rock.png")
image_paper_computer = PhotoImage(file="computer_paper.png")
image_scissor_computer = PhotoImage(file="computer_scissor.png")

# Creating the label for player and computer using scissor images of both as default
label_player = Label(window, image=image_scissor_user)
label_computer = Label(window, image=image_scissor_computer)
label_player.grid(row=1, column=0)
label_computer.grid(row=1, column=4)

# Creating the label to show player and computer score
player_score = Label(window, text=0, font=("arial", 50, "bold"), bg="green", fg="white")
computer_score = Label(window, text=0, font=("arial", 50, "bold"), bg="green", fg="white")
player_score.grid(row=1, column=1)
computer_score.grid(row=1, column=3)

# Creating the labels for player and computer
player_indicator = Label(window, font=("arial", 20, "bold"), text="Player", bg="green", fg="white")
computer_indicator = Label(window, font=("arial", 20, "bold"), text="Computer", bg="green", fg="white")
player_indicator.grid(row=0, column=1)
computer_indicator.grid(row=0, column=3)


# Crating the function to update the message at the buttom
def message_update(a):
    message_result["text"] = a


# creating a function to update the computer score
def computer_score_update():
    final = int(computer_score["text"])
    final += 1
    computer_score["text"] = str(final)


# creating a function to update the user score
def user_score_update():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)


# creating a function to check who the winner is and update the scores accordingly
def winner_check(player, computer):
    if player == computer:
        message_result.config(text="Draw")
    elif player == "rock":
        if computer == "paper":
            message_result.config(text="Computer Wins")
            computer_score_update()
        else:
            message_result.config(text="Player Wins")
            user_score_update()
    elif player == "paper":
        if computer == "scissor":
            message_result.config(text="Computer Wins")
            computer_score_update()
        else:
            message_result.config(text="Player Wins")
            user_score_update()
    elif player == "scissor":
        if computer == "rock":
            message_result.config(text="Computer Wins")
            computer_score_update()
        else:
            message_result.config(text="Player Wins")
            user_score_update()
    else:
        pass


# List for the computer to select from
to_select = ["rock", "paper", "scissor"]


# updating the player and computer choices while also updating the respective images
def choice_update(a):
    computer_choice = to_select[randint(0, 2)]
    if computer_choice == "rock":
        label_computer.configure(image=image_rock_computer)
    elif computer_choice == "paper":
        label_computer.configure(image=image_paper_computer)
    elif computer_choice == "scissor":
        label_computer.configure(image=image_scissor_computer)
    else:
        pass
    if a == "rock":
        label_player.configure(image=image_rock_user)
    elif a == "paper":
        label_player.configure(image=image_paper_user)
    elif a == "scissor":
        label_player.configure(image=image_scissor_user)
    winner_check(a, computer_choice)


# Label to show the result at the buttom of the screen
message_result = Label(window, text="Choose one", font=("arial", 20, "bold"), bg="green", fg="white")
message_result.grid(row=3, column=2)


# Creating the buttons for the user to select from
button_rock = Button(window, width=16, height=3, text="Rock", font=("arial", 20, "bold"),
                     bg="yellow", fg="red", command=lambda: choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, width=16, height=3, text="Paper", font=("arial", 20, "bold"),
                      bg="yellow", fg="red", command=lambda: choice_update("paper")).grid(row=2, column=2)
button_scissor = Button(window, width=16, height=3, text="Scissor", font=("arial", 20, "bold"),
                        bg="yellow", fg="red", command=lambda: choice_update("scissor")).grid(row=2, column=3)


window.mainloop()
