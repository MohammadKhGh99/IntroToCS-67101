from tkinter import *
from ex12.ai import *
from tkinter.messagebox import *

WARNING_MSG = "Warning !"


class GUI:
    def __init__(self):
        self.__root = Tk()
        # self.__title=PhotoImage(file=title)
        self.__title = PhotoImage(file="ex12\\title.png")
        self.__board = PhotoImage(file="ex12\\four in row bg.png")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(side=LEFT, anchor="sw")
        self.__canvas.configure(bg='white', height=621, width=723)
        self.__game = Game()
        self.__comp = 0
        self.__discs_id = []
        self.__buttons = []
        self.__how = 0

    def starting_the_window(self):
        """
        this method starts the window of the game
        :return: returns nothing
        """
        self.__root.configure(background='white')
        self.__root.title("Four In Row Game")
        self.__root.geometry("960x750")
        label_title = Label(self.__root, image=self.__title, bd=0)
        label_title.place(relx=1.0, rely=0.0, anchor="ne")
        self.starting_buttons()
        self.__root.mainloop()

    def start_human_human(self):
        """
        this method starts a game human vs human
        :return: returns nothing
        """
        self.whos_turn()
        self.destroy_button()
        self.human_player()

    def human_player(self):
        """
        this method makes the human player plays
        :return: returns nothing
        """
        self.__canvas.bind("<Button-1>", self.callback)

    def ai_turn(self, ai):
        """
        this method makes the computer player plays
        :param ai: the wanted computer player that wanted to play with the
        human player
        :return: returns nothing
        """
        try:
            column = ai.find_legal_move()
        except:
            if self.__game.get_winner() is not None:
                showinfo("Winning", "Player %d won" % self.__game.get_winner())
            else:
                self.ai_turn(ai)
        else:
            y = 557 - (self.calc_row(column) * 100)
            x = 60 + column * 100
            self.__discs_id.append(self.create_circle(x, y, 42))
            try:
                self.__game.make_move(column)
            except:
                showinfo(WARNING_MSG, ILLEGAL_MOVE)
            self.check_winner()
            self.whos_turn()
            self.human_player()

    def destroy_button(self):
        """
        this method destroys the buttons in the root
        :return: returns nothing
        """
        for button in self.__buttons:
            button.destroy()

    def destroy_how(self):
        """
        this method destroys how to play label
        :return: returns nothing
        """
        if self.__how == 1:
            self.__how_play.destroy()
            self.__how = 0

    def start_computer_human(self):
        """
        this method starts a game computer vs human
        :return: returns nothing
        """
        self.whos_turn()
        self.destroy_button()
        self.__comp = PLAYER_ONE
        self.__ai = AI(self.__game, PLAYER_ONE)
        won = self.__game.get_winner()
        if won is None:
            if self.__game.get_current_player() == PLAYER_ONE:
                self.ai_turn(self.__ai)
            else:
                self.human_player()

    def start_human_computer(self):
        """
        this method starts a game human vs computer
        :return: returns nothing
        """
        self.whos_turn()
        self.destroy_button()
        self.__comp = PLAYER_TWO
        self.__ai = AI(self.__game, PLAYER_TWO)
        won = self.__game.get_winner()
        if won is None:
            if self.__game.get_current_player() == PLAYER_TWO:
                self.ai_turn(self.__ai)
            else:
                self.human_player()

    def empty_the_game(self):
        """
        this method empty the board of the game
        :return: returns nothing
        """
        self.__game.empty_the_board()
        for idy in self.__discs_id:
            self.__canvas.delete(idy)

    def new_button_callback(self):
        """
        this method will be activated when the new game button clicked.
        :return: returns nothing
        """
        self.empty_the_game()
        self.destroy_how()
        self.__game.set_current_player(PLAYER_ONE)
        self.__game.set_color(ONE_COLOR)
        self.__human_vs_human = Button(self.__root, text="Human VS Human",
                                       command=self.start_human_human)
        self.__buttons.append(self.__human_vs_human)
        self.__human_vs_computer = Button(self.__root, text="Human VS "
                                "Computer",command=self.start_human_computer)
        self.__buttons.append(self.__human_vs_computer)
        self.__computer_vs_human = Button(self.__root, text="Computer VS "
                                    "Human",command=self.start_computer_human)
        self.__buttons.append(self.__computer_vs_human)
        self.__canvas.create_image(365, 623, image=self.__board, anchor="s")
        self.__human_vs_human.place(relx=0.935, rely=0.47, anchor="e")
        self.__human_vs_computer.place(relx=0.9429, rely=0.52, anchor="e")
        self.__computer_vs_human.place(relx=0.9429, rely=0.57, anchor="e")
        # computer_vs_computer=Button(self.__root,text="Computer VS Computer")
        # computer_vs_computer.place(relx=0.9492,rely=0.62,anchor="e")

    def quit_button(self):
        """
        this method do what should be when quit button clicked
        :return: returns nothing
        """
        quitting = askyesno("QUITTING !", "Are You Sure ?")
        if quitting:
            quit()
        else:
            pass

    def check_winner(self):
        """
        this method checks if there is a winner or not
        :return: returns nothing
        """
        won = self.__game.get_winner()
        if won is None:
            return
        elif won == 1:
            showinfo("Winning", "player 1 won")
        elif won == 2:
            showinfo("Winning", "player 2 won")
        else:
            showinfo("Draw", "two players draw")
        self.__canvas.unbind("<Button-1>")
        self.__game.set_current_player(PLAYER_ONE)
        self.__game.set_color(ONE_COLOR)
        self.whos_turn()

    def starting_buttons(self):
        """
        this method shows the buttons that will be appear when the window
        started
        :return: returns nothing
        """
        new_game = Button(self.__root, text="New Game",
                          command=self.new_button_callback,
                          font=("Helvetica", 20))
        new_game.place(relx=0.96, rely=0.4, anchor="e")
        how_to_play = Button(self.__root, text="How To Play", fg="green",
                             command=self.how_to_play, font=("Helvetica", 10))
        how_to_play.place(relx=0.92, rely=0.67, anchor="e")
        quit_button = Button(self.__root, text="QUIT", fg="red",
                             command=self.quit_button, height=1, width=20)
        quit_button.place(relx=0.8, rely=0.7)

    def how_to_play(self):
        """
        this method shows how to play label
        :return: returns nothing
        """
        self.__how_play = Label(self.__root, text="* click on New Game to "
                       "start a new game\n* click on the column that you want")
        self.__how_play.place(relx=0.35, rely=0.1, anchor="n")
        self.__how = 1

    def create_circle(self, x, y, r):
        """
        this method creates a circle and put it in the appropiate place
        :param x: the x coordinate of the clicked place
        :param y: the y coordinate of the clicked place
        :param r: the radius of the circle
        :return: returns the id of the circle
        """
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        if self.__game.get_current_player() == PLAYER_ONE:
            return self.__canvas.create_oval(x0, y0, x1, y1, fill="blue")
        else:
            return self.__canvas.create_oval(x0, y0, x1, y1, fill="red")

    def calc_col(self, x):
        """
        this method calculate the approppiate column of the clicked place
        :param x: the x coordinate of the clicked place
        :return: returns the apprppiate column of the clicked place
        """
        x -= 10
        if x < 10 or x >= 700:
            return -1
        return x // 100

    def calc_row(self, col):
        """
        this method gets the number of the existed circles in the chosen
        column.
        :param col: the chosen column
        :return: returns the number of the existed circles in the chosen
        column.
        """
        return self.__game.get_list_of_counters()[col]

    def whos_turn(self):
        """
        this method puts a label with the number and the color of the
        current player.
        :return: returns nothing
        """
        player = self.__game.get_current_player()
        color = self.__game.get_color()
        self.__current_player = Label(self.__root, text="player %d turn" %
                    player, bg=color,height=2, width=20,font=("Helvetica", 20))
        self.__current_player.place(relx=0.35, rely=0.0, anchor="n")

    def callback(self, event):
        """
        this method do all the work when the human player click on the board
        :param event: the clicked place
        :return: returns nothing
        """
        won = self.__game.get_winner()
        if won is None:
            x = event.x
            col = self.calc_col(x)
            row = 557 - (self.calc_row(col) * 100)
            column = 60 + col * 100
            self.__discs_id.append(self.create_circle(column, row, 42))
            try:
                self.__game.make_move(col)
            except:
                showinfo(WARNING_MSG, ILLEGAL_MOVE)
            self.check_winner()
            self.whos_turn()
            if self.__comp != 0:
                self.ai_turn(self.__ai)
        else:
            self.check_winner()


if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
