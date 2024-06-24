import get_puzzle
from tkinter import * 
window = Tk()
window.title("SUDOKO")

BOARD = [[0 for _ in range(9)] for _ in range(9)]

def reg():
    '''
    This is a regen of a board that will transfer
    '''
    board_state = get_puzzle.fetch('easy')
    puzzle = board_state['puzzle']
    print(puzzle)
    for i in range(81):
        BOARD[i // 9][i % 9] = puzzle[i]
    update_board()

def update_board():
    for i in range(9):
        for j in range(9):
            text = StringVar()
            if BOARD[i][j] == '0':
                text.set("")
                ROWS[i][j].config(textvariable = text, state='normal')
            else:
                text.set(BOARD[i][j])
                ROWS[i][j].config(textvariable = text, state='readonly')


ROWS = []

for i in range(1,10):
    cols = []
    for j in range(1,10):
        e = Entry(window,width=3,relief="groove",justify="center")
        e.grid(row=i, column=j, sticky=NSEW,)
        cols.append(e)
    ROWS.append(cols)

l1 = Label(window,text="SUDOKU",height=3)
l1.grid(row=0,column=3,columnspan=4)

b1 = Button(window,text="New Puzzle",width=6,command=reg)
b1.grid(row=10,column=5,columnspan=5)
b2 = Button(window,text="close",width=6,command=window.destroy)
b2.grid(row=11,column=5,columnspan=3)

reg()
window.mainloop()
