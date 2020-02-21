import math
import random

def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += (2*self.width + 1) * '-'   # bottom of the board
        # and the numbers underneath here
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """Arguments: col is the column the checker is being placed in. 
            ox is the checker being added. Adds character to lowest open
            row in desired column. 
        """
        count = 0
        for i in reversed(list(range(self.height))):
            while self.data[i][col] == ' ' and count == 0:
                self.data[i][col] = ox 
                count += 1
    
    def clear(self):
        """Clears the board.
        """
        for i in range(self.height):
            for j in range(self.width):
                self.data[i][j] = ' '
        
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self,c):
        """Returns true if c is within the range of the last
            column and is not full. Returns false if column c is not a 
            part of the board or if column c is part of the 
            board, but is full. 
        """
        if c < 0 or c >= self.width:
            return False
        for i in range(self.height):
            if self.data[i][c] == ' ':
                return True
            else:
                return False

    def isFull(self):
        """Returns true if board is completely full. 
            Returns false otherwise. 
        """
        for i in range(self.width):
            if self.allowsMove(i) == True:
                return False
        return True

    def delMove(self,c):
        """Removes the top checker from the coloumn c. 
            If the coloumn c is empty, then delMove does nothing.
        """
        count = 0
        for i in range(self.height):
            while (self.data[i][c] == 'O' or self.data[i][c] == 'X') and count == 0:
                self.data[i][c] = ' ' 
                count += 1

    def winsFor(self,ox):
        """Returns true if there are four checkers in a row 
            of type ox. Returns false otherwise.
        """
        for i in range(self.width):
            for j in range(self.height):
                if inarow_Neast(ox,j,i,self.data,4):
                    return True
                elif inarow_Nsouth(ox,j,i,self.data,4):
                    return True
                elif inarow_Nnortheast(ox,j,i,self.data,4):
                    return True
                elif inarow_Nsoutheast(ox,j,i,self.data,4):
                    return True
        else:
            return False

    def colsToWin(self, ox):
        """Takes one argument: ox is either 'X' or 'O'. 
            Returns a list of columns where ox can move to
            win the game. Does not look ahead more than 
            one turn. 
        """
        answer = []
        for i in range(self.width):
            if self.allowsMove(i) == True:
                self.addMove(i, ox)
                if self.winsFor(ox) == True:
                    answer = answer + [i]
                self.delMove(i)
        return answer

    def aiMove(self,ox):
        """Accepts a single argument: ox is the checker character.
            Returns an integer that is a legal coloumn to move. If 
            there is a way for ox to win, then that coloumn is returned. 
            If there is not a way for ox to win, but there is a way to 
            block the other character from winning, that coloumn is returned. 
            If there is no way to move or block the opponent from winning
            then another coloumn is returned that is legal.
        """
        if self.colsToWin(ox) != []:
            return self.colsToWin(ox)[0]
        else:
            if ox == 'X':
                if self.colsToWin('O') != []:
                    return self.colsToWin('O')[0]
                else:
                    for i in range(self.width):
                        return self.allowsMove(i)
            elif ox == 'O':
                if self.colsToWin('X') != []:
                    return self.colsToWin('X')[0]
                else:
                    for i in range(self.width):
                        return self.allowsMove(i)

    def hostGame(self):
        """Facilitates a game of connect four. Computer plays 
        O's and the user play's X's. 
        """
        print('Welcome to Connect four!')
        print(self)
        while True:
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("Choose a coloum: "))
                print("X's choice: ", users_col)
            self.addMove(users_col,'X')
            print(self)
            if self.winsFor('X'):
                print('X wins -- Congratulations!') 
                break
            else:
                users_col = int(self.aiMove('O'))
                print("O's choice: ", users_col)
                self.addMove(users_col, 'O')
                print(self)
                if self.winsFor('O'):
                    print('O wins -- Congratulations!')
                    break
            if self.isFull():
                print("Tie game!")
                break
    
    def playGame(self, pForX, pForO, ss = False):
        """ Plays a game of Connect Four.
            p1 and p2 are objects of type Player OR
            the string 'human'.
            If ss is True, it will "show scores" each time.
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = pForX
        count = 0

        while True:

            # print the current board
            print(self)
            
            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove(col):
                    col = int(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [int(sc) for sc in scores])
                    print()
                    col = nextPlayerToMove.tiebreakMove(scores)
                else:
                    col = nextPlayerToMove.nextMove(self)

            # add the checker to the board
            # finds the 10% chance
            count = random.choice(range(10))
            if count == 1:
                possible_moves = []
                for i in range(self.width):
                    # makes a list of possible moves
                    if self.allowsMove(i):
                        possible_moves += [i]
                col = random.choice(possible_moves)
                # picks a random choice out of the possible moves
                self.addMove(col, nextCheckerToMove)
                print("Player " + nextCheckerToMove + " has randomly moved to column: " + str(col))
            else:
                self.addMove(col, nextCheckerToMove)
            
            # check if game is over
            if self.winsFor(nextCheckerToMove):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break
        
            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = pForO
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = pForX

        print('Come back 4 more!')


class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """Returns the checker piece that the opponent
            is playing with. 
        """
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'

    def scoreBoard(self, b):
        """Arguments: b is the object of type Board.
            Returns 100 is b is a win for self.
            Returns 50 if b is neither a win nor a loss for self.
            Returns 0 if it is a loss for self.
        """
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0
    
    def tiebreakMove(self, scores):
        """Arguments: nonempty list of floating point numbers representing scores of each coloumn. 
            Returns the coloumn that the user should pick based on their respective tiebreaking type. 
        """
        A = []
        newList = []
        maximum = max(scores)
        for i in range(len(scores)):
            if scores[i] == maximum:
                A += [i]
        if self.tbt == 'LEFT':
            return A[0]
        elif self.tbt == 'RIGHT':
            return A[-1]
        else:
            for i in range(len(A)):
                newList += [i]
            return A[random.choice(newList)]
    
    def scoresFor(self, b):
        """ scoresFor returns a list of scores for each column of the board
        """
        scores = [50]*b.width
        for c in range(b.width):
            if(b.allowsMove(c) == False):
                scores[c] = -1.0
            elif(self.scoreBoard(b) == 100.0):
                scores[c] = 100.0
            elif(self.scoreBoard(b) == 0.0):
                scores[c] = 0.0
            elif(self.ply == 0.0):
                scores[c] = 50.0         
            else:
                b.addMove(c, self.ox)
                op = Player(self.oppCh(), self.tbt, self.ply-1)
                scores[c] = 100 - max(op.scoresFor(b))
                b.delMove(c)
        return scores
                    
    def nextMove(self, b):
        """Accepts b, an object of type board.
            Returns an integer representing the coloumn 
            that the class (player) chooses to move.
        """
        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)

    