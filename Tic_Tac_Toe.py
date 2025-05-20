import random
import tkinter as tk
from tkinter import messagebox 

player_score = 0
ai_score = 0
def check_winner():
    global winner, player_score, ai_score
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            winner = True
            winner_text = buttons[a]["text"]
            if winner_text == "x":
                player_score += 1
                update_score()
                messagebox.showinfo("Tic-Tac-Toe", "You win!")
            elif winner_text == "o":
                ai_score += 1
                update_score()
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            return True
    if all(button["text"] != "" for button in buttons):
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        return True
    return False


def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = "x"
        if not check_winner():
            toggle_player()


def toggle_player():
    global current_player
    current_player = "o"
    label.config(text="AI is thinking...")
    root.after(500, ai_move)  # Let AI move after 0.5 sec


def ai_move():
    global current_player
    if winner:
        return
    empty_indices = [i for i, b in enumerate(buttons) if b["text"] == ""]
    if empty_indices:
        ai_choice = random.choice(empty_indices)
        buttons[ai_choice]["text"] = "o"
        if not check_winner():
            current_player = "x"
            label.config(text="Your turn")



def restart_game():
    global current_player, winner
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    current_player = "x"
    winner = False
    label.config(text="Your turn")


def update_score():
    score_label.config(text=f"Player: {player_score}   AI: {ai_score}")




root =tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text ="" , font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i //3 , column=i % 3)

current_player = "x"
winner = False
label = tk.Label(root, text=f"plyer {current_player}'s turn", font=("normal", 16)) 
label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="Player: 0   AI: 0", font=("normal", 14))
score_label.grid(row=4, column=0, columnspan=3)



restart_button = tk.Button(root, text="Restart", font=("normal", 14), command=restart_game)
restart_button.grid(row=5, column=0, columnspan=3)


root.mainloop()


                    
