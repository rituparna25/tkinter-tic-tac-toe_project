import tkinter as tk
from tkinter import ttk,messagebox

player1_name=""
player2_name=""
player1_symbol=""
player2_symbol=""
current_player=""
player1_score=0
player2_score=0
ties=0

def reset_game():
    global player1_score,player2_score,ties
    player1_score=0
    player2_score=0
    ties=0
    update_scores()
    reset_board()

def update_scores():
    score_label.config(text=f"{player1_name}:{player1_score}\n{player2_name}:{player2_score}\nTies:{ties}")

def reset_board():
    global current_player
    current_player=player1_name
    status_label.config(text=f"Current Player:{current_player}")
    for row in buttons:
        for button in row:
            button.config(text="",state="active")

def on_click(row,col):
    global current_player
    button=buttons[row][col]
    if button["text"]=="" and current_player:
        button["text"]=player1_symbol if current_player==player1_name else player2_symbol
        button["state"]="disabled"
        check_winner()
        current_player=player2_name if current_player==player1_name else player1_name
        status_label.config(text=f"Current Player: {current_player}")

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"]!="":
            declare_winner(buttons[i][0]["text"])
            return
        if buttons[0][i]["text"]== buttons[1][i]["text"] == buttons[2][i]["text"]!="":
            declare_winner(buttons[0][i]["text"])
            return
    if buttons[0][0]["text"]== buttons[1][1]["text"] == buttons[2][2]["text"]!="":
        declare_winner(buttons[0][0]["text"])
        return
    if buttons[0][2]["text"]== buttons[1][1]["text"] == buttons[2][0]["text"]!="":
        declare_winner(buttons[0][2]["text"])
        return
    if all(button["text"]!="" for row in buttons for button in row):
        declare_tie()

def declare_winner(winner):
    global player1_score,player2_score
    if winner == player1_symbol:
        player1_score +=1
    else:
        player2_score+=1
    update_scores()
    messagebox.showinfo("Winner!",f"{winner} wins the game!")
    reset_board()

def declare_tie():
    global ties
    ties +=1
    update_scores()
    messagebox.showinfo("Tie Game","Its a tie!")
    reset_board()

def start_game():
    global player1_name,player2_name,player1_symbol,player2_symbol
    player1_name=player1_entry.get()
    player2_name=player2_entry.get()
    player1_symbol=player1_symbol_entry.get().upper()
    if player1_name and player2_name and player1_symbol in ["X","O"]:
        player2_symbol="X" if player1_symbol=="O" else "O"
        status_label.config(text=f"Current Player: {player1_name}")
        start_button.config(state="disabled")
        player1_entry.config(state="disabled")
        player2_entry.config(state="disabled")
        player1_symbol_entry.config(state="disabled")
        reset_board()
    else:
        messagebox.showerror("Error","Please enter valid player names and symbols (X or O),")

def final_match():
    if player1_score > player2_score:
        winner=player1_name
    elif player2_score > player1_score:
        winner=player2_name
    else:
        winner="ITS A TIE !"
    messagebox.showinfo("Final match result",f"The winner is: {winner}")
    reset_game()

root=tk.Tk()
root.title("Tic Tac Toe")

style=ttk.Style()
style.configure('TButton',background='RED',foreground='white',font=('Helvetica',14,'bold'))
style.configure('TLabel', font=('Helvetica',14))
style.configure('Header.TLabel',font=('Helvetica',18,'bold'))
style.configure('Info.TLabel',font=('Helvetica',12,'italic'))

player1_label=ttk.Label(root, text="Player 1 Name: ")
player2_label=ttk.Label(root, text="Player 2 Name: ")
player1_entry=ttk.Entry(root)
player2_entry=ttk.Entry(root)
player1_symbol_label=ttk.Label(root, text="Player 1 Symbol (X or O):")
player1_symbol_entry=ttk.Entry(root)
start_button = ttk.Button(root, text=" Start Game", command=start_game)
reset_button= ttk.Button(root,text="Reset", command=reset_game)
final_match_button= ttk.Button(root,text="Final Match", command=final_match)
score_label= ttk.Label(root,text="")
status_label= ttk.Label(root,text="")
buttons=[[None,None,None] ,[None,None,None], [None,None,None]]


for i in range(3):
    for j in range(3):
        buttons[i][j]=tk.Button(root, text="", width=10, height=2, command=lambda row=i, col=j: on_click(row,col), font=('Helvetica',14,'bold'), bg='Yellow', fg='white')

player1_label.grid(row=0, column=0, padx=10, pady=10)
player1_entry.grid(row=0, column=1, padx=10, pady=10)
player2_label.grid(row=1, column=0, padx=10, pady=10)
player2_entry.grid(row=1, column=1, padx=10, pady=10)
player1_symbol_label.grid(row=2, column=0, padx=10, pady=10)
player1_symbol_entry.grid(row=2, column=1, padx=10, pady=10)
start_button.grid(row=3, columnspan=2, padx=10, pady=10)
reset_button.grid(row=4, column=0, padx=10, pady=10)
final_match_button.grid(row=4, column=1, padx=10, pady=10)
score_label.grid(row=5, columnspan=2,padx=10, pady=10)
status_label.grid(row=6, columnspan=2, padx=10, pady=10)

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i+7, column=j, padx=10, pady=10)

root.mainloop()
