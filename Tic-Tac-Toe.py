# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:06:22 2019

@author: OLUKARE DANIEL
"""

from random import randrange, randint
TURN=0
WIN=False
Num_Moves=0
turnchecker=False
turnchooser=randrange(0,2)
if turnchooser<=0.5:
    TURN=0
else:
    TURN=1
def freespot(Board):
    freerow=0
    freecol=0
    lists1 = []
    for i in range(0,3):
        for j in range(0,3):
            if(Board[i][j]=='-' and Board[i][j]!='X' and Board[i][j]!='O'):
                lists1.append([i,j])
    x = int(randrange(len(lists1)))
    freerow = lists1[x][0]
    freecol = lists1[x][1]
    return freerow, freecol
def Check_WINNER(Board):
    # Check Rows
    for i in range(3):
        if Board[i][0]!='-' and Board[i][0]==Board[i][1] and Board[i][1]==Board[i][2]:
            return(True)
    # Check Columns
    for i in range(3):
        if Board[0][i]!='-' and Board[0][i]==Board[1][i] and Board[1][i]==Board[2][i]:
            return(True)
    # Check Diagonal
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and Board[1][1]==Board[2][2]:
        return(True)
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and Board[1][1]==Board[2][0]:
        return(True)    
    
    return(False)
    
def printBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j], end=" ")
        print()

Board=[["-","-","-"],["-","-","-"],["-","-","-"]]
def leftdiagonalwin(Board):
    rolx = -1
    colx = -1
    Danda = False
    for i in range(0,2):
        if Board[i][i] == Board[i+1][i+1] and TURN!=0 and Board[i][i] == "O" :
            if(Board[2][2]=="-" and Board[2][2]!="X" and i+1 == 1):
                rolx = 2
                colx = 2
                Danda = True
               
            elif( Board[2][2]=="-" and Board[2][2]!="X" and i + 1 == 2):
                rolx = 0
                colx = 0
                Danda = True
    if Board[0][0] == Board[2][2] and TURN!=0 and Board[i][i] == "O" and Board[1][1]=="-" and Board[2][2]!="X":
        rolx = 1
        colx = 1
        Danda = True
    return rolx, colx, Danda
def rowWin(Board):
    Danda = False
    rowx = -1
    colx = -1
    for i in range(0, 3):
        if Board[i][0] == Board[i][1] and Board[i][1]=='O' and Board[i][2] == '-' and TURN!=0:
            rowx = i
            colx = 2
            Danda = True
        if Board[i][1] == Board[i][2] and Board[i][1]=='O' and Board[i][0] == '-' and TURN!=0:
            rowx = i
            colx = 0
            Danda = True
        if Board[i][0] == Board[i][2] and Board[i][2]=='O' and Board[i][1] == '-' and TURN!=0:
            rowx = i
            colx = 1
            Danda = True
    return rowx, colx,Danda
def colWin(Board):
    Danda = False
    rowx = -1
    colx = -1
    for j in range(0, 3):        
        if Board[0][j] == Board[1][j] and Board[2][j]=='-' and TURN!=0 and Board[1][j]=='O':         
            rowx = 2
            colx = j
            Danda  = True
        if Board[1][j] == Board[2][j] and Board[0][j]=='-' and TURN!=0 and Board[1][j]=='O':         
            rowx = 0
            colx = j
            Danda  = True
        if Board[0][j] == Board[2][j] and Board[1][j]=='-' and TURN!=0 and Board[2][j]=='O':         
            rowx = 1
            colx = j
            Danda  = True
    return rowx, colx,Danda
def rightdiagonalwin(Board):
    rowin = -1
    cowin= -1
    Danda = False
    if(Board[0][2]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[2][0]=="-" and Board[2][0]!="X"):
            rowin=2
            cowin=0
            Danda=True
    elif(Board[2][0]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[0][2]=="-" and Board[0][2]!="X"):
            rowin=0
            cowin=2
            Danda=True
    elif(Board[0][2]==Board[2][0] and TURN!=0 and Board[2][0]=="O"):
        if(Board[1][1]=="-" and Board[1][1]!="X"):
            rowin=1
            cowin=1
            Danda=True
    return rowin,cowin,Danda

def choosepossiblewin(Board):
    leftrow, leftcol, leftdiag = leftdiagonalwin(Board)
    colrowwin, colWincol, colWinner = colWin(Board)
    rowWinrow, colrowcol, rowWinner = rowWin(Board)
    rightrow, rightcol, rightdiag = rightdiagonalwin(Board)

    if(rowWinner == True ):
        return rowWinrow, colrowcol, rowWinner
    elif(colWinner == True ):
        return colrowwin, colWincol, colWinner
    elif(rightdiag == True):
        return rightrow, rightcol, rightdiag
    elif(leftdiag == True):
        return leftrow, leftcol, leftdiag
    else:
        return -1, -1, False

def rowcheck(Board):
    rowx =-1
    colx = -1
    for i in range(0, 3):
        if Board[i][0] == Board[i][1] and Board[i][1]!='O' and Board[i][2] == '-' :
            rowx = i
            colx = 2
        elif Board[i][1] == Board[i][2] and Board[i][1]!='O' and Board[i][0] == '-' :
            rowx = i
            colx = 0
        elif Board[i][0] == Board[i][2] and Board[i][2]!='O' and Board[i][1] == '-' :
            rowx = i
            colx = 1
    return rowx, colx

def Columncheck(Board):
    rowx = -1
    colx = -1
    for j in range(0, 3):        
        if Board[0][j] == Board[1][j] and Board[2][j]=='-' and   Board[1][j]!='O':         
            rowx = 2
            colx = j

        if Board[1][j] == Board[2][j] and Board[0][j]=='-' and Board[1][j]!='O':         
            rowx = 0
            colx = j

        if Board[0][j] == Board[2][j] and Board[1][j]=='-'  and Board[2][j]!='O':         
            rowx = 1
            colx = j

    return rowx, colx
    
def leftdiagonalcheck(Board):
    randrowe=-1
    randcole=-1
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and Board[1][1]!='O':
        randrowe=2
        randcole=2
        if(Board[2][2]=="O"):
            randrowe=-1
            randcole=-1

    elif Board[1][1]==Board[2][2] and Board[1][1]!="-" and Board[1][1]!='O':
        randrowe=0
        randcole=0
        if(Board[0][0]=="O"):
            randrowe=-1
            randcole=-1

    elif Board[2][2]==Board[0][0] and Board[2][2]!="-" and Board[2][2]!='O':
        randrowe=1
        randcole=1
        if(Board[1][1]=="O"):
            randrowe=-1
            randcole=-1

    else:
        randrowe=-1
        randcole=-1
    return randrowe,randcole
def randgenerator(Board):
    rand1=0
    rand2=0
    for i in range(0,3):
        for j in range(0,3):
            if(Board[i][j]=="-" and Board!="X" and Board!="O"):
                rand1=randint(0,i)
                rand2=randint(0,j)
    return rand1,rand2
def checkers(Board):
    getrow=0
    getcol=0
    checkers=False
    getrow,getcol,checkers=choosepossiblewin(Board)
    return getrow,getcol,checkers
def rightdiagonalcheck(Board):
    randrow=-1
    randcol=-1    
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and Board[1][1]!='O':
        randrow=2
        randcol=0
        if(Board[2][0]=="O"):
            randrow=-1
            randcol=-1
            
    elif Board[1][1]==Board[2][0] and Board[2][0]!="-" and Board[2][0]!='O':
        randrow=0
        randcol=2
        
        if(Board[0][2]=="O"):
            randrow=-1
            randcol=-1

    elif Board[0][2]==Board[2][0] and Board[0][2]!="-" and Board[0][2]!='O':
        randrow=1
        randcol=1
        
        if(Board[1][1]=="O"):
            randrow=-1
            randcol=-1
    else:
        randrow=-1
        randcol=-1  
        
    return randrow,randcol  
def chooser(Board):
    x,y=freespot(Board)
    rha,a=rowcheck(Board)
    cha,b=Columncheck(Board)
    ldc,c=leftdiagonalcheck(Board)
    rdc,d=rightdiagonalcheck(Board)
    rowchoice,colchoice=freespot(Board)
    grow,gcol,gcheck=checkers(Board)
    if(gcheck==True and Num_Moves>4):
        #print("win situation",grow,gcol)
        return grow,gcol
    elif(Num_Moves>=3):
        if(rha>=0):
            rha,a=rowcheck(Board)
            return rha,a
        elif(cha>=0):
            #print("cha",cha,b)
            cha,b=Columncheck(Board)
            return cha,b
        elif(ldc>=0 ):
            #print("ldc",ldc,c)
            ldc,c=leftdiagonalcheck(Board)
            return ldc,c
        elif(rdc>=0 ):
            rdc,d=rightdiagonalcheck(Board)
            #print("rdc",rdc,d)
            return rdc,d
        else:
            return x,y
    elif(Num_Moves<3):
        return rowchoice,colchoice
print("Original Board Configuration")
printBoard(Board)
while (not WIN) and Num_Moves <= 8:
    if TURN==0:
        print("This is Your Turn:")
        Check_Move=False
        while not Check_Move:
            Row=int(input("Enter the Row:"))
            Col=int(input("Enter the Column: "))
            if(Row>3 or Col>3):
                print("Wrong choice, the position is out of index")
            elif Board[Row-1][Col-1]!='-':
                print("That position if already played. Enter the new tile position")
            else:
                Check_Move=True
            
        Board[Row-1][Col-1]='X'
        printBoard(Board)
        TURN=1
        Num_Moves += 1
        if Num_Moves > 4:
            WIN=Check_WINNER(Board)
        if WIN:
            print("CONGRATULATIONS PLAYER X:")
            print("YOU ARE THE WINNER")
    else:
        print("This is the Computer's Turn:")
        Check_Move=False
        Row,Col=chooser(Board)        
        Board[Row][Col]='O'
        printBoard(Board)
        TURN=0
        Num_Moves += 1  
        if Num_Moves > 4:
            WIN=Check_WINNER(Board)
        if WIN:
            print("THE COMPUTER WINS!!!:")
if not WIN:
    print("The Game ended as a tie")
