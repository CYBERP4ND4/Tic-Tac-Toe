import tkinter

# Mechanics
def set_tile(row, column):
    global currentPlayer

    if gameboard[row][column]["text"] != "":
        return

    if (gameOver):
        return

    gameboard[row][column]["text"] = currentPlayer

    if currentPlayer == playerTwo:
        currentPlayer = playerOne
    else:
        currentPlayer = playerTwo

    label["text"] = currentPlayer+"'s Turn"
    checkWinner()

def checkWinner():
    global turns, gameOver
    turns += 1

    for row in range(3):
        if (gameboard[row][0]["text"] == gameboard[row][1]["text"] == gameboard[row][2]["text"]
                and gameboard[row][0]["text"] != ""):
            label.config(text=gameboard[row][0]["text"] +
                         " is the winner!", foreground=colorGreen)
            for column in range(3):
                gameboard[row][column].config(
                    foreground=colorGreen, background=colorWhite)
            gameOver = True
            return

    for column in range(3):
        if (gameboard[0][column]["text"] == gameboard[1][column]["text"] == gameboard[2][column]["text"]
                and gameboard[0][column]["text"] != ""):
            label.config(text=gameboard[0][column]["text"] +" is the winner!", foreground=colorGreen)
            for row in range(3):
                gameboard[row][column].config(foreground=colorGreen, background=colorWhite)
            gameOver = True
            return

    if (gameboard[0][0]["text"] == gameboard[1][1]["text"] == gameboard[2][2]["text"]
            and gameboard[0][0]["text"] != ""):
        label.config(text=gameboard[0][0]["text"] +" is the winner!", foreground=colorGreen)
        for i in range(3):
            gameboard[i][i].config(foreground=colorGreen, background=colorWhite)
        gameOver = True
        return

    if (gameboard[0][2]["text"] == gameboard[1][1]["text"] == gameboard[2][0]["text"]
            and gameboard[0][2]["text"] != ""):
        label.config(text=gameboard[0][2]["text"] +" is the winner!", foreground=colorGreen)
        gameboard[0][2].config(foreground=colorGreen, background=colorWhite)
        gameboard[1][1].config(foreground=colorGreen, background=colorWhite)
        gameboard[2][0].config(foreground=colorGreen, background=colorWhite)
        gameOver = True
        return

    if (turns == 9):
        gameOver = True
        label.config(text="It's a Tie!", foreground=colorYellow)


def new_game():
    global turns, gameOver
    turns = 0
    gameOver = False

    label.config(text=currentPlayer+"'s Turn", foreground=colorWhite)

    for row in range(3):
        for column in range(3):
            gameboard[row][column].config(text="", foreground=colorWhite, background=colorDarkGray)

# Main Variables
playerOne = "X"
playerTwo = "O"
currentPlayer = playerOne
gameboard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
turns = 0
gameOver = False

# Colors
colorWhite = "#ffffff"
colorRed = "#b90b0b"
colorDarkGray = "#1f1f20"
colorPurple = "#9644ff"
colorGreen = "#50de0b"
colorYellow = "#fcde0b"

# Main Window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)

label = tkinter.Label(frame, text=currentPlayer + "'s Turn", font=("Dejavu Sans", 20), 
                      background=colorDarkGray, foreground=colorWhite)

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        gameboard[row][column] = tkinter.Button(frame, text="", font=("Dejavu Sans", 50, "bold"), background=colorDarkGray,
                                                foreground=colorWhite, width=4, height=1,command=lambda row=row, 
                                                column=column: set_tile(row, column))
        
        gameboard[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="RESTART", font=("Dejavu Sans", 20), background=colorPurple, 
                        foreground=colorWhite, command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()
window.mainloop()
