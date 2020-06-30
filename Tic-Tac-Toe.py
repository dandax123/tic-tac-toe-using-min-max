from random import randrange, randint
TURN=0
WIN=False
Num_Moves = 0
turnchecker=False
turnchooser=randrange(0,2)
if turnchooser<=0.5:
    TURN=0
else:
    TURN=1
def Check_WINNER(Board):
    # Check Rows
    winner = -1
    for i in range(3):
        if Board[i][0]!='-' and Board[i][0]==Board[i][1] and Board[i][1]==Board[i][2]:
            winner = Board[i][0]
    # Check Columns
    for i in range(3):
        if Board[0][i]!='-' and Board[0][i]==Board[1][i] and Board[1][i]==Board[2][i]:
            winner = Board[0][i]
    # Check Diagonal
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and Board[1][1]==Board[2][2]:
        winner = Board[0][0]
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and Board[1][1]==Board[2][0]:
        winner = Board[0][2]    
    if(noOfFreeSpots(Board) == 0 and winner == -1):
        return 'tie'
    return winner
scores = {'tie': 0, 'O' : 1, 'X' : -1}
def noOfFreeSpots(Board):
    cnt = 0
    for i in range(3):
        for j in range (3):
            if(Board[i][j] == '-'):
                cnt +=1
    return cnt

def minimax(Board, depth, isMaximizing):
    result = Check_WINNER(Board)
    if(result != -1):
        return scores[result]

    if(isMaximizing):
        csScore = float('-inf')
        for i in range (3): 
            for j in range (3):
                if(Board[i][j] == '-'):
                    Board[i][j] = 'O'
                    csScore = max(csScore, minimax(Board, depth + 1, False))
                    Board[i][j] = '-'
        return csScore 
    else:
        currentScore = float('inf')
        for i in range (3):
            for j in range (3):
                if(Board[i][j] == '-'):
                    Board[i][j] = 'X'
                    currentScore = min(currentScore, minimax(Board, depth + 1, True))
                    Board[i][j] = '-'
        return currentScore            

def chooser(Board):
    bestScore = float('-inf')
    colx  = -1
    rowx = -1
    if(Num_Moves < 2):
        return freespot(Board)
    for i in range (3):
        for j in range (3):
            if(Board[i][j] == '-'):
                Board[i][j] = 'O'
                score = minimax(Board, 0, False)
                Board[i][j] = '-'
                if(score > bestScore):
                    bestScore = score
                    rowx = i
                    colx = j
    return rowx, colx

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
def printBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j], end=" ")
        print()

Board=[["-","-","-"],["-","-","-"],["-","-","-"]]
print("Original Board Configuration")
printBoard(Board)
while  Num_Moves <= 8:
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
        if WIN !=-1 and WIN != 'tie':
            print("CONGRATULATIONS PLAYER: "  + WIN )
            break
    
if WIN == 'tie':
    print("The Game ended as a tie")
