#importing Tkinter library.....
from tkinter import *
#initialiaze function to make a board with nested
#dictionaries like rows,columns,NW diagonal,SE diagonal...
#SE and NW diagonals and row and column will be unique to one queen...
def initialiaze(board):
    L=['queen','row','col','diag1','diag2']
    for i in L:
        board[i]={}
    for i in range(n):
        board['queen'][i]=-1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(0,2*(n)-1):
        board['diag1'][i]=0
    for i in range(-(n-1),n):
        board['diag2'][i]=0
#It checks a box is empty or not by checking the given row,column,and both diagonals...
#returns the boolean value True or False....
#(i,j) will come from the main function place_queens...
def is_free(i,j,board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['diag1'][j+i]==0 and board['diag2'][j-i]==0)
#This function will change the row,column,both diagonals to 1 which were 0 initially...
#and changes the key value of queen dictionary to the column of queen placed...
def place_queen(i,j,board):
    board['queen'][i]=j
    board['row'][i]=1
    board['col'][j]=1
    board['diag1'][i+j]=1
    board['diag2'][j-i]=1
#It will involve the undoing step of queen in backtracking process...
#i.e. It will change the values of row,column,and both diagonals to 0 again...
def undo_queen(i,j,board):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][j]=0
    board['diag1'][j+i]=0
    board['diag2'][j-i]=0
#This function is used to extract the rows and columns of queens placed.
#And A list L is used in this function to take the values...
#And this List is used to make GUI framework using Tkinter...
def make_board(board):
    for i in sorted(board['queen'].keys()):
        L.append([i,board['queen'][i]])

#It is the main function which starts with i=0...
#It continuosly runs a loop on different columns and check the output of function is_free...
#If is_free returns True then place_queen function will run...
#And we will extend the solution by recursion for further rows...
#If at any time is_free returns False then we will run undo_queen function....
#if we reaches at last row and place_queens runs successfully then make_board will run and place_queen terminates...
#If board is completed successfully then it will returns True otherwise false...
def place_queens(i,board):
    for j in range(n):
        if is_free(i,j,board):
            place_queen(i,j,board)
            if i==n-1:
                return(True)
            else:
                extend_soln=place_queens(i+1,board)
            if extend_soln:
                return(True)
            else:
                undo_queen(i,j,board)
    return(False)

n=int(input('No. of queens you want to place : '))
board={}
L=[]
initialiaze(board)
place_queens(0,board)
#If place_queen returns True then make_board will run...
if __name__=="__main__":
    if place_queens:
        make_board(board)
    else:
        print('False')

#root will give the blank windows of our GUI...
#Canvas will give the box size and background...
#I have used the queen of 60x60.
#if n queens to be placed then board will be of n*60 in length and in breath also...
#We will acess the coordinates of our queen from the list L...
#To acess the position of image of queen left top corner we will multiply the row and coumns accordingly with 60...
#at last root.mainloop() will show the window of GUI for infinite time until we do not quit it...
root=Tk()
canvas=Canvas(root,width=n*60,height=n*60,bg='blue')
canvas.pack()
for i in range(0,n*60,60):
    count=1
    for j in range(0,n*60,60):
        if count==1:
            canvas.create_rectangle(i, j, 60+i, 60+j, fill='black')
            count=2
        if count==2:
            canvas.create_rectangle(i, j, 60+i, 60+j, fill='white')
            count=1
photo = PhotoImage(file='queen.png')
for i in L:
    x=i[0]
    y=i[1]
    canvas.create_image(x*60,y*60,image=photo,anchor=NW)
root.mainloop()

