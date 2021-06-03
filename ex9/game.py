from car import *
from helper import *
import sys
import os.path
from board import Board

INPUT_MESSAGE = "Enter the name of the car (Y,B,O,W,R,G) and ',' and the " \
                "movekey: "
WRONG_INPUT = "You Have Entered A Wrong Input !!!"
COLORS='YRWBGO'
DIRECTIONS='udrl'
WON_MESSAGE="You Have Won !!!"

class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while self.board[3][7]=="E":
            print(self.board,"\n")
            playing = input(INPUT_MESSAGE)
            name=playing[0]
            movekey=playing[2]
            length=len(playing)
            if name in COLORS and movekey in DIRECTIONS\
               and playing[1]==',' and length==3:
                self.board.move_car(name,movekey)
                if self.board.cell_content(self.board.target_location())!="E":
                    print(WON_MESSAGE)
            else:
                print(WRONG_INPUT)


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    board=Board()
    json_file=sys.argv[1]
    if os.path.exists(json_file):
        cars_dict=load_json(json_file)
        for i in range(len(cars_dict)):
            name=cars_dict[i]
            information_list=cars_dict[name]
            length=information_list[0]
            location=tuple(information_list[1])
            orientation=information_list[2]
            board.add_car(Car(name,length,location,orientation))
    game=Game(board)
    game.play()


