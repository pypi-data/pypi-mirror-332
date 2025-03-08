'''
**DO NOT MODIFY THIS CLASS - FOR REFERENCE ONLY**

You will be inheriting from this class - so all of these methods will
be available to you in your new class.
'''

class Board:
    '''
    A generic 2D game board of a given dimension.
    At each square in the game board, a piece can be placed onto the board
    The piece can be ANY type of item - strings, numbers, new GamePiece types...
    The board is initialized to None at the very beginning

    Args:
        rsize (int): row size
        csize (int): col size
    '''

    ###### DO NOT EDIT ANYTHING IN THIS CLASS ######
    def __init__(self, rsize, csize):
        '''
        Initializes a Board with a given dimension
        
        Args:
            rsize (int): row size
            csize (int): col size
        '''
        self.board = [ [ None for _ in range(csize) ] for _ in range(rsize) ]

    def getBoard(self):
        '''
        Get the board
        
        Returns:
            List[List[any]]: The board
        '''
        return self.board

    def setBoard(self, board):
        '''
        Set the board to a given board. 

        **Note**: This could be helpful for testing purposes to set up a board 
        to a particular setup.
        
        Args:
            board (List[List[any]]): The new board
        '''
        self.board = board

    def putPiece(self, piece, r, c):
        '''
        Put a game piece on the board at (r, c)
        
        Args:
            piece (any): Any piece
            r (int): row
            c (int): col
        '''
        self.board[r][c] = piece

    def getPiece(self, r, c):
        '''
        Get a game piece on the board at (r, c)
        
        Args:
            r (int): row
            c (int): col

        Returns:
            any: The piece on the board at (r, c)
        '''
        return self.board[r][c]

    def rowSize(self):
        '''
        Get number of rows in the Board
        
        Returns:
            int: The number of rows in the Board
        '''
        return len(self.board)
    
    def colSize(self):
        '''
        Get number of columns in the Board
        
        Returns:
            int: The number of columns in the Board
        '''
        return len(self.board[0])

    def reset(self):
        '''
        Clears out the board of all pieces - replaces every location with None
        '''
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.board[r][c] = None

    def __eq__(self, other):
        '''
        Compare two Boards for equality. This could also be used for testing
        purposes to compare two boards.
        
        Args:
            other (Board): The other Board
        
        Returns:
            bool: True if the two Boards are equal, False otherwise
        '''
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] != other.board[r][c]:
                    return False
        return True

    def __str__(self):
        '''
        Print the board nicely
        '''
        s = ""
        WIDTH = 6
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                val = self.board[r][c]
                s += str(val) + " "*(WIDTH - len(str(val)))
            s += "\n"
        s += "\n"
        return s

    ###### DO NOT EDIT ANYTHING IN THIS CLASS ######
