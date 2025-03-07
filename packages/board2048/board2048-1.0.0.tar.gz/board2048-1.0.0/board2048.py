import random
from board import Board
from typing import List

class Board2048(Board):
    '''
    The board that is used for 2048 - inherits from Board and addes some unique
    methods specific for the game 2048
    '''

    def __init__(self, rsize: int, csize: int, n: int):
        '''
        Initializes a 2048 Board with a given dimension and ending target number.
        The target ending number (does not really have to be 2048 - it can be any other number).
        
        Args:
            rsize (int): row size
            csize (int): col size
            n (int): target number to achieve to end game
        '''
        # just call the parent's __init__
        super().__init__(rsize, csize)
        self.target = n
        self.madeGoal = False

    def getTarget(self):
        '''
        Returns:
            int: Value of tile to achieve in game (e.g. 2048 nominally)
        '''
        return self.target

    def addRandomTile(self):
        '''
        Adds a random tile into the board as long. Makes sure there is not current tile there
        when new tile is places. A 2 is placed with a probability of 90% and a 4 is places with
        a probability of 10%
        '''
        if self.full():
            return

        if random.random() <= .9:
            value = 2
        else:
            value = 4

        # Find empty spot
        r = random.randrange(self.rowSize())
        c = random.randrange(self.colSize())
        while self.getPiece(r, c) != None:
            r = random.randrange(self.rowSize())
            c = random.randrange(self.colSize())

        self.putPiece(value, r, c)

    def shift(self, dir):
        '''
        Shifts the 2048 board up/down/left/right. If *dir* is not a legal
        value, then nothing happens. The score based on any merged tiles is
        returned.

        Args:
            dir (str): direction of shift - "u" or "d" or "l" or "r"
        
        Returns:
            int: Score from all the merging of tiles
        '''
        if dir not in "lrud":
            return 0

        # make a copy of the board to use a standard shift
        # and then copy the board back into the board

        # make a copy of the board - either copy each row or column
        copy = []
        if dir in "lr":
            for r in range(len(self.board)):
                copy.append(self.board[r])
        else:
            for c in range(len(self.board[0])):
                copy.append(self.extractCol(c))

        # reverse the copy if needed
        if dir in "dr":
            for i in range(len(copy)):
                copy[i].reverse()

        # shift each row in the copy
        score = 0
        for i in range(len(copy)):
            score += self.shiftRow(copy[i])

        # reverse the copy if needed
        if dir in "dr":
            for i in range(len(copy)):
                copy[i].reverse()

        # put the shifted rows back into the board
        if dir in "lr":
            for r in range(len(self.board)):
                self.board[r] = copy[r]
        else:
            for c in range(len(self.board[0])):
                self.replaceCol(copy[c], c)

        return score

    def achievedGoal(self):
        '''
        Check if board has reached target value

        Returns:
            boolean: Has the board achieved target value (ex. 2048)
        '''
        for r in range(self.rowSize()):
            for c in range(self.colSize()):
                if self.board[r][c] == self.target:
                    return True
        return False

    def moreMoves(self):
        '''
        Check if board is full w/o anymore moves possible

        Returns:
            boolean: Returns true if there are more possible moves/swipes

        '''
        for dir in "lrud":
            if self.legalSwipe(dir):
                return True
        return False

    def legalSwipe(self, dir):
        '''
        Can 2048 board be shifted in given direction? If no tiles move, then it is not a leval shift.

        Args:
            dir (str): direction of shift - "u" or "d" or "l" or "r"
        
        Returns:
            boolean: Returns true if at least 1 tile moves in the given direction
        '''
        if dir not in "lrud":
            return False

        # make a copy of the board - either copy each row or column
        copy = []
        if dir in "lr":
            for r in range(len(self.board)):
                copy.append(self.board[r].copy())
        else:
            for c in range(len(self.board[0])):
                copy.append(self.extractCol(c))

        # reverse the copy if needed
        if dir in "dr":
            for i in range(len(copy)):
                copy[i].reverse()

        # try shifting each row in the copy
        canShift = False
        for i in range(len(copy)):
            canShift = canShift or self.rowCanShift(copy[i])

        return canShift

    def extractCol(self, c):
        '''
        Extract the col from the given board

        Args:
            c (int): The index of the col to be extracted

        Returns:
            List[int]: the col specified by the input c
        '''
        return [self.board[r][c] for r in range(len(self.board))]

    def replaceCol(self, col: List[int], c):
        '''
        Replace the col in the given board

        Args:
            col (List[int]): The new col
            c (int): The index of the col to be replaced
        '''
        for r in range(len(self.board)):
            self.board[r][c] = col[r]

    def shiftRow(self, row: List[int]) -> int:
        '''
        Shift the given row to the left and merge tiles if needed. Return the score from merging.
        Args:
            row (List[int]): The row to be shifted
        Returns:
            int: score from merging
        '''
        score = 0
        # Move all empty spaces to end of row
        i = 0
        for _ in range(len(row)-1):
            if row[i] == None:
                val = row.pop(i)
                row.append(val)
            else:
                i += 1

        # Merge tiles starting from the left (i.e. 0)
        i = 0
        while i < len(row)-1:
            if row[i] != None and row[i] == row[i+1]:
                row[i] = row[i] * 2
                score += row[i]
                row.pop(i+1)
                row.append(None)
            i += 1

        # Move all empty spaces to end of row
        i = 0
        for _ in range(len(row)-1):
            if row[i] == None:
                val = row.pop(i)
                row.append(val)
            else:
                i += 1

        return score

    def rowCanShift(self, row: List[int]):
        '''
        Given a row, check if it is shiftable "to the left" i.e. toward 0
        Example: [None, 2, 2 , 4] is shiftable
        Example: [2, 2, None , 4] is shiftable
        Example: [2, 4, None , None] is not shiftable
        Example: [2, 2, None , None] is shiftable because the 2's can merge
        Example: [None, None, None , None] is not shiftable

        Returns:
            boolean: Is the row shiftable toward 0
        '''

        # Move all empty spaces to end of row
        rowCopy = row.copy()
        i = 0
        for _ in range(len(row)-1):
            if rowCopy[i] == None:
                val = rowCopy.pop(i)
                rowCopy.append(val)
            else:
                i += 1

        # Merge tiles starting from the left (i.e. 0)
        i = 0
        while i < len(rowCopy)-1:
            if rowCopy[i] != None and rowCopy[i] == rowCopy[i+1]:
                rowCopy[i] = rowCopy[i] * 2
                rowCopy.pop(i+1)
                rowCopy.append(None)
                i += 2
            else:
                i += 1

        # if rowCopy is different from row, then we can shift
        return rowCopy != row

        # all 
        if row.count(None) == len(row):
            return False

        # find largest index with non-None, then search for any None index smaller that it
        i = len(row)-1
        if row[i] == None:
            # look for non-None
            while i > 0 and row[i] == None:
                i -= 1
        
        # find a index j < i where row[j] is empty
        j = 0
        while j < i and row[j] != None:
            j += 1

        # if empyty spot is before a filled spot, then we can shift legeally
        if j < i:
            return True

        # from index 0 until a None, look for "mergeable" tiles (i.e. equivalent)
        i = 0 
        while i < len(row)-1 and row[i] != None:
            if row[i] == row[i+1]:
                return True
            i += 1
        return False

    def full(self):
        '''
        Check if board is full

        Returns:
            boolean: Is the board full (no empty spaces)
        '''
        for r in range(self.rowSize()):
            for c in range(self.colSize()):
                if self.board[r][c] == None:
                    return False
        return True
        

        




    
