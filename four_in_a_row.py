from tkinter import *
from ex12.game import *
from ex12.ai import *
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
ROWS_NUM = 6
COLS_NUM = 7
WINNING_SEQ = 4
ROW = 0
COL = 1
PLAYER_A_WON = 1
PLAYER_B_WON = 2
TIE = 0


class MenuWindow:
    """
    This class is a first window that starts to run. It includes a canvas that
    stores a cover, the title of the game and a menu with 4 buttons. Each
    button leads to a different game. The options are: Human vs. Human, Human
    vs. Computer, Computer vs. Human, Computer vs. Computer.
    """

    def __init__(self, parent):
        """
        This function initiates the canvas, boolean values for detecting the
        kind of players, the cover picture, the title of the game and all the
        menu buttons.
        :param parent: the root
        """
        self.__parent = parent
        self.__human1 = False  # True if the 1st player is human
        self.__human2 = False  # True if the 2nd player is human
        self.__canvas = Canvas(self.__parent, width=CANVAS_WIDTH,
                               height=CANVAS_HEIGHT)
        self.__canvas.pack(fill='both')

        self.__cover = PhotoImage(file='ex12/cover.png')
        self.__cover_label = Label(self.__canvas, image=self.__cover)
        self.__cover_label.pack(fill='both')

        self.__title = PhotoImage(file='ex12/title.png')
        self.__title = self.__title.subsample(2, 1)
        self.__title_label = Label(self.__canvas, image=self.__title,
                                   bg='OrangeRed4', bd=7)
        self.__title_label.place(anchor='n', relx=0.5, rely=0.04)

        self.__all_buttons_in_first_window()

    def __all_buttons_in_first_window(self):
        """
        This function is being called from the init function in order to
        initiate all the menu buttons and the quit button.
        """
        button1 = Button(self.__canvas, text='Human Vs. Human',
                         font='times 20 bold', fg='lightgoldenrod',
                         bg='OrangeRed4')
        button2 = Button(self.__canvas, text='Human Vs. Computer',
                         font='times 20 bold', fg='lightgoldenrod',
                         bg='OrangeRed4')
        button3 = Button(self.__canvas, text='Computer Vs. Human',
                         font='times 20 bold', fg='lightgoldenrod',
                         bg='OrangeRed4')
        button4 = Button(self.__canvas, text='Computer Vs. Computer',
                         font='times 20 bold', fg='lightgoldenrod',
                         bg='OrangeRed4')

        button1.bind("<Button-1>", self.__open_new_window)
        button2.bind("<Button-1>", self.__open_new_window)
        button3.bind("<Button-1>", self.__open_new_window)
        button4.bind("<Button-1>", self.__open_new_window)

        button1.place(anchor='nw', relx=0.1, rely=0.35)
        button2.place(anchor='sw', relx=0.1, rely=0.7)
        button3.place(anchor='se', relx=0.9, rely=0.7)
        button4.place(anchor='ne', relx=0.9, rely=0.35)

        quit_button = Button(self.__canvas, text="Quit", font='times 14 bold',
                             fg='white', bg='gray12', command=self.__quit_game)
        quit_button.place(anchor='se', relx=0.83, rely=0.85)

    def __open_new_window(self, event):
        """
        This function is being called if one of the menu buttons was clicked.
        It detects the exact click that was clicked upon the button's name.
        In addition, it assigns to each click a boolean value in order to
        detect the kind of players in that game. Eventually it leads to
        the next window.
        :param event: left click on the mouse
        """
        if event.widget._name == '!button':
            # Human vs. Human
            self.__human1 = True
            self.__human2 = True
        elif event.widget._name == '!button2':
            # Human vs. Computer
            self.__human1 = True
            self.__human2 = False
        elif event.widget._name == '!button3':
            # Computer vs. Human
            self.__human1 = False
            self.__human2 = True
        elif event.widget._name == '!button4':
            # Computer vs. Computer
            self.__human1 = False
            self.__human2 = False

        new_window = Toplevel(self.__parent)  # open new window on same root
        # shut down the program when exit is being clicked.
        new_window.protocol("WM_DELETE_WINDOW", on_close)
        self.__parent.withdraw()  # close previous window
        StartWindow(new_window, self)  # call the next window

    def __quit_game(self):
        """
        This function ends the game.
        """
        self.__parent.destroy()
        self.__parent.quit()

    def get_human_1(self):
        """ Getter for __human1"""
        return self.__human1

    def get_human_2(self):
        """ Getter for __human2"""
        return self.__human2

    def get_quit_game(self):
        """ Getter for __quit_game"""
        return self.__quit_game


class StartWindow:
    """
    This class is the second window that opens after clicking on one of the
    menu buttons in the previous window. It displays to the user, on a canvas,
    his choice of players, by pictures and a suitable title of the window.
    In addition it displays to the screen a button-'play', to start the game
    and a button-'go back', to come back to previous window.
    """

    def __init__(self, parent, first_window):
        """
        This function initiates the canvas, the cover picture, all the pictures
        for displaying the kind of players. It calls a function to initiate all
        the buttons and different function to display different pictures.
        :param parent: the root
        :param first_window: the previous class of previous window for using
        it's functions.
        """
        self.__parent = parent
        self.__first_window = first_window  # previous window
        self.__canvas = Canvas(self.__parent, width=CANVAS_WIDTH,
                               height=CANVAS_HEIGHT)
        self.__canvas.pack(fill='both')

        self.__cover = PhotoImage(file='ex12/cover.png')
        self.__cover_label = Label(self.__canvas, image=self.__cover)
        self.__cover_label.pack(fill='both')

        # initiates all the pictures.
        self.tyrion = PhotoImage(file='ex12/tyrion.png')
        self.tyrion = self.tyrion.subsample(3, 2)
        self.bran = PhotoImage(file='ex12/bran.png')
        self.bran = self.bran.subsample(3, 2)
        self.ai = PhotoImage(file='ex12/ai.png')
        self.ai = self.ai.subsample(3, 2)

        self.tyrion_label = Label(self.__canvas, image=self.tyrion, bd=10,
                                  bg='gold2')
        self.tyrion_label.image = self.tyrion
        self.bran_label = Label(self.__canvas, image=self.bran, bd=10,
                                bg='gold2')
        self.bran_label.image = self.bran
        self.ai_label1 = Label(self.__canvas, image=self.ai, bd=10,
                               bg='gold2')
        self.ai_label1.image = self.ai
        self.ai_label2 = Label(self.__canvas, image=self.ai, bd=10,
                               bg='gold2')
        self.ai_label2.image = self.ai

        # displays different pictures and title in each function.
        if self.__first_window.get_human_1() and \
                self.__first_window.get_human_2():
            # Human vs. Human
            self.__handle_human_human()
        elif self.__first_window.get_human_1() and \
                not self.__first_window.get_human_2():
            # Human vs. Computer
            self.__handle_human_computer()
        elif not self.__first_window.get_human_1() and \
                self.__first_window.get_human_2():
            # Computer vs. Human
            self.__handle_computer_human()
        elif not self.__first_window.get_human_1() and \
                not self.__first_window.get_human_2():
            # Computer vs. Computer
            self.__handle_computer_computer()

        self.__all_buttons_in_second_window()

    def __all_buttons_in_second_window(self):
        """
        This function initiates from the init function all the buttons in that
        window: 'go back', 'play', 'quit'. The 2 first buttons lead to '
        callback' function.
        """
        button1 = Button(self.__canvas, text='Go back', font='times 20 bold',
                         fg='lightgoldenrod', bg='OrangeRed4')
        button2 = Button(self.__canvas, text='Play', font='times 20 bold',
                         fg='lightgoldenrod', bg='OrangeRed4')
        button1.bind("<Button-1>", self.__callback_to_play_or_back)
        button2.bind("<Button-1>", self.__callback_to_play_or_back)

        button1.place(anchor='sw', relx=0.3, rely=0.88)
        button2.place(anchor='se', relx=0.7, rely=0.88)

        # This button leads to the 'quit_game' function in previous window.
        quit_button = Button(self.__canvas, text="Quit", font='times 14 bold',
                             fg='white', bg='gray12',
                             command=self.__first_window.get_quit_game())
        quit_button.place(anchor='se', relx=0.85, rely=0.9)

    def __handle_human_human(self):
        """
        This function displays a suitable title and pictures for
        Human vs. Human game.
        """
        label_text = Label(self.__canvas, text='HUMAN vs. HUMAN',
                           font='times 50 bold', fg='gold2', bg='gray12')
        label_text.place(anchor='n', relx=0.5, rely=0.05)
        self.bran_label.place(relx=0.1, rely=0.25)
        self.tyrion_label.place(relx=0.6, rely=0.25)

    def __handle_human_computer(self):
        """
        This function displays a suitable title and pictures for
        Human vs. Computer game.
        """

        label_text = Label(self.__canvas, text='HUMAN vs. COMPUTER',
                           font='times 50 bold', fg='gold2', bg='gray12')
        label_text.place(anchor='n', relx=0.5, rely=0.05)
        self.bran_label.place(relx=0.1, rely=0.25)
        self.ai_label2.place(relx=0.6, rely=0.25)

    def __handle_computer_human(self):
        """
        This function displays a suitable title and pictures for
        Computer vs. Human game.
        """
        label_text = Label(self.__canvas, text='COMPUTER vs. HUMAN',
                           font='times 50 bold', fg='gold2', bg='gray12')
        label_text.place(anchor='n', relx=0.5, rely=0.05)
        self.ai_label1.place(relx=0.1, rely=0.25)
        self.tyrion_label.place(relx=0.6, rely=0.25)

    def __handle_computer_computer(self):
        """
        This function displays a suitable title and pictures for
        Computer vs. Computer game.
        """
        label_text = Label(self.__canvas, text='COMPUTER vs. COMPUTER',
                           font='times 50 bold', fg='gold2', bg='gray12')
        label_text.place(anchor='n', relx=0.5, rely=0.05)
        self.ai_label1.place(relx=0.1, rely=0.25)
        self.ai_label2.place(relx=0.6, rely=0.25)

    def __callback_to_play_or_back(self, event):
        """
        This function is being called if the 'play' or 'go back' buttons were
        pressed. It detects each button by it's name and opens a new window.
        :param event: left click on the mouse
        """
        if event.widget._name == '!button':
            # the 'go back' button leads to the previous window.
            # opens new window on same root
            new_window = Toplevel(self.__parent)
            # shuts down the program when exit is being clicked.
            new_window.protocol("WM_DELETE_WINDOW", on_close)
            self.__parent.withdraw()  # closes previous window
            MenuWindow(new_window)  # calls the previous window
        else:
            # the 'play' button leads to the next window of the game.
            # opens new window on same root
            new_window = Toplevel(self.__parent)
            # shuts down the program when exit is being clicked.
            new_window.protocol("WM_DELETE_WINDOW", on_close)
            self.__parent.withdraw()  # closes previous window
            # calls the next window
            GameWindow(new_window, self.__first_window)


class GameWindow:
    """
    This class is the gui board and where the game occurs. It has a canvas which
    includes statement of the status of the game, pictures of the 2 players,
    and the board. The board lies on a frame that includes 42 canvases that are
    actually 42 buttons for each disc. It displays who's turn is it and weather
    there is a winner or a tie at the end. It asks the user to play again at
    the end og the game.
    """

    def __init__(self, parent, first_window):
        """
        This function initiates the canvas, all the pictures, the cover
        picture, the frame with 42 canvases and 42 buttons and 2 frames for
        each picture of the players. The gui board is represented by list of
        lists. Finally, it checks if the first player is a computer for
        handling without pressing a button.
        :param parent: the root
        :param first_window: the first class for using it's functions
        """
        self.__parent = parent
        self.__first_window = first_window
        self.__end_game = False  # boolean for detecting end of game
        self.__canvas = Canvas(self.__parent, width=CANVAS_WIDTH,
                               height=CANVAS_HEIGHT)
        self.__canvas.pack(fill='both')
        self.__board = game.get_board()  # the board from the Game class

        self.__cover = PhotoImage(file='ex12/cover.png')
        self.__cover_label = Label(self.__canvas, image=self.__cover)
        self.__cover_label.pack(fill='both')

        # the pictures of the players, the discs and the winning pictures.
        self.daenerys = PhotoImage(file='ex12/daenerys.png')
        self.daenerys = self.daenerys.subsample(8, 8)
        self.johnsnow = PhotoImage(file='ex12/johnsnow.png')
        self.johnsnow = self.johnsnow.subsample(8, 8)
        self.crown = PhotoImage(file='ex12/crown.png')
        self.crown = self.crown.subsample(4, 4)
        self.daenerys_rules = PhotoImage(file='ex12/daenerys_rules.png')
        self.daenerys_rules = self.daenerys_rules.subsample(1, 1)
        self.johnsnow_rules = PhotoImage(file='ex12/johnsnow_rules.png')
        self.johnsnow_rules = self.johnsnow_rules.subsample(1, 1)

        # a message to the user to invite to play.
        self.title_label = Label(self.__canvas, text='Play...',
                                 font='times 50 bold', fg='gold2', bg='gray12')
        self.title_label.place(anchor='n', relx=0.5, rely=0.01)

        # frame for player A with a text-'player A' and a picture.
        self.__frame_A = Frame(self.__canvas, width=300, height=300,
                               bg='gray12')
        self.__frame_A.place(anchor='w', relx=0.68, rely=0.5)
        self.__player_A_label = Label(self.__frame_A, text='PLAYER A:',
                                      font='times 24 bold', fg='OrangeRed3',
                                      bg='gray12')
        self.__player_A_label.pack(side=TOP)
        self.daenerys_rules_label = Label(self.__frame_A,
                                          image=self.daenerys_rules, bd=10,
                                          bg='gold2')
        self.daenerys_rules_label.image = self.daenerys_rules
        self.daenerys_rules_label.pack(side=BOTTOM)

        # frame for player B with a text-'player B' and a picture.
        self.__frame_B = Frame(self.__canvas, width=300, height=300,
                               bg='gray12')
        self.__frame_B.place(anchor='e', relx=0.32, rely=0.5)
        self.__player_B_label = Label(self.__frame_B, text='PLAYER B:',
                                      font='times 24 bold', fg='OrangeRed3',
                                      bg='gray12')
        self.__player_B_label.pack(side=TOP)
        self.johnsnow_rules_label = Label(self.__frame_B,
                                          image=self.johnsnow_rules, bd=10,
                                          bg='gray12')
        self.johnsnow_rules_label.image = self.johnsnow_rules
        self.johnsnow_rules_label.pack(side=BOTTOM)

        # frame for the board
        self.__frame_for_gui_board = Frame(self.__canvas, width=700,
                                           height=600)
        self.__frame_for_gui_board.place(anchor='n', relx=0.5, rely=0.2)

        self.__canvases = []
        self.__canvas_buttons = []
        # creates 42 canvases for each button.
        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                self.grid_canvas = Canvas(self.__frame_for_gui_board,
                                          width=50, height=50, bg='gray12')
                self.grid_canvas.grid(row=i, column=j % 7)
                # stores all the canvases
                self.__canvases.append(self.grid_canvas)

        # creates 42 buttons on each canvas.
        for canvas in self.__canvases:
            # each human's press on a button leads to a callback function.
            self.canvas_button = Button(canvas, bg='OrangeRed3',
                                        command=lambda some_canvas=canvas:
                    self.__intersection_for_games_including_human(some_canvas))
            self.canvas_button.place(relheight=1, relwidth=1)
            # stores all the buttons
            self.__canvas_buttons.append(self.canvas_button)

        # The gui board is represented by list of lists. Each item in the
        # inner list is a canvas from the 42 canvases.
        self.__gui_board = [self.__canvases[i:i + 7]
                            for i in range(0, len(self.__canvases), 7)]

        # checks if the game is Computer vs. Computer for different dialing.
        if not self.__first_window.get_human_1() and \
                not self.__first_window.get_human_2():
            self.__handle_ai_ai_game()

        # checks if the first player is a computer and calls a function
        # to handle the ai.
        if game.get_current_player() == 1 and \
                not self.__first_window.get_human_1() and \
                self.__first_window.get_human_2():
            self.__computer_begins()

        self.quit_button()

    def quit_button(self):
        """
        Initiate quit button
        """
        # This button leads to the 'quit_game' function in the first window.
        quit_button = Button(self.__canvas, text="Quit", font='times 14 bold',
                             fg='white', bg='gray12',
                             command=self.__first_window.get_quit_game())
        quit_button.place(anchor='se', relx=0.83, rely=0.93)

    def __intersection_for_games_including_human(self, canvas):
        """
        This function leads each kind of game that includes human player to
        different function for different game.
        :param canvas: the canvas that the button on it was clicked by a
        human player
        """
        if self.__first_window.get_human_1() and \
                self.__first_window.get_human_2():
            # Human vs. Human
            self.__handle_human_human_game(canvas)
        elif self.__first_window.get_human_1() and \
                not self.__first_window.get_human_2():
            # Human vs. Computer
            self.__handle_human_ai_game(canvas)
        elif not self.__first_window.get_human_1() and \
                self.__first_window.get_human_2():
            # Computer vs. Human
            self.__handle_ai_human_game(canvas)

    def __computer_begins(self):
        """
        This function handles the game when the computes is the first player.
        It disables all the buttons on the board to prevent from human to play,
        calls the ai function and then sets the buttons back to normal
        functionality.
        """
        for button in self.__canvas_buttons:
            button.config(state=DISABLED)
        # makes a move of ai after 0.5 sec.
        self.__parent.after(500, self.__move_ai)

    def __handle_ai_ai_game(self):
        """
        This function handles a game when only ai involves. It's not waiting
        for pressing a button so it calls itself while the game is not over.
        """
        self.__check_turn()  # displays on the screen who's turn is it.
        self.status = game.get_winner()  # checks the status of the game
        self.__handle_winning()  # displays winners or tie if there are any.

        # makes a move of ai after 0.5 sec.
        self.__parent.after(500, self.__move_ai)
        if not self.__end_game:
            # calls itself after 0.5 sec if the game isn't over
            self.__parent.after(500, self.__handle_ai_ai_game)

    def __callback_for_human_click(self, canvas):
        """
        This function runs through all the gui board, and finds the exact
        coordinate of the canvas that is given as a parameter, in all the
        canvases that are stored in the gui board as list of lists. It finds
        a match between the canvases upon it's names. Then, it puts a disc to
        the gui board by making a move on the Game class board. Finally, it
        updates the gui board according to all the discs on the Game's board
        coordinates.
        :param canvas: The canvas that the button on it was pressed.
        """
        try:  # makes a move only if the move is legal
            for i in range(ROWS_NUM):
                for j in range(COLS_NUM):
                    if canvas._name == self.__gui_board[i][j]._name:
                        game.make_move(j)
                        self.__update_gui()
        except:  # when the move isn't legal it gets an exception
            pass  # ignores human's click if it's illegal.

    def __handle_human_human_game(self, canvas):
        """
        This function handles a game of Human vs. Human.
        :param canvas: The canvas that the button on it was pressed.
        """
        if not self.__end_game:  # while the game isn't over
            self.__callback_for_human_click(canvas)  # handles human move
            self.__check_turn()   # displays on the screen who's turn is it.
            self.status = game.get_winner()  # checks the status of the game
            self.__handle_winning()  # displays winners or tie if there are any

    def __handle_human_ai_game(self, canvas):
        """
        This function handles a game of Human vs. Computer.
        :param canvas: The canvas that the button on it was pressed.
        """
        if not self.__end_game:  # while the game isn't over
            if game.get_current_player() == 1:
                for button in self.__canvas_buttons:
                    button.config(state=NORMAL)
                self.__callback_for_human_click(canvas)  # handles human move

            self.__check_turn()  # displays on the screen who's turn is it.
            self.status = game.get_winner()  # checks the status of the game
            self.__handle_winning()  # displays winners or tie if there are any

            for button in self.__canvas_buttons:  # disables buttons
                button.config(state=DISABLED)
            # makes a move of ai after 0.5 sec.
            self.__parent.after(500, self.__move_ai)

    def __handle_ai_human_game(self, canvas):
        """
        This function handles a game of Computer vs. Human.
        :param canvas: The canvas that the button on it was pressed.
        """
        if not self.__end_game:  # while the game isn't over
            # handles human move only if it's the second player's turn
            if game.get_current_player() == 2:
                for button in self.__canvas_buttons:
                    button.config(state=NORMAL)
                self.__callback_for_human_click(canvas)

            self.__check_turn()  # displays on the screen who's turn is it.
            self.status = game.get_winner()  # checks the status of the game
            self.__handle_winning()  # displays winners or tie if there are any

            for button in self.__canvas_buttons:  # disables buttons
                button.config(state=DISABLED)
            # makes a move of ai after 0.5 sec.
            self.__parent.after(500, self.__move_ai)

    def __move_ai(self):
        """
        This function handles ai move.
        """
        try:  # makes a move only if the move is legal
            self.__handle_ai()
            self.__update_gui()
            self.__check_turn()  # displays on the screen who's turn is it.
            self.status = game.get_winner()  # checks the status of the game
            self.__handle_winning()  # displays winners or tie if there are any
        except:  # when the move isn't legal it gets an exception
            # does nothing when the function is being called while there is a
            # winner or a tie
            pass
        finally:
            for button in self.__canvas_buttons:
                button.config(state=NORMAL)

    def __handle_ai(self):
        """
        This function checks which players turn is it and according to it, gets
        a random move from ai object of Ai class number 1 or 2.
        """
        if game.get_current_player() == 1:
            ai_move = ai1.find_legal_move()
            game.make_move(ai_move)

        elif game.get_current_player() == 2:
            ai_move = ai2.find_legal_move()
            game.make_move(ai_move)

    def __update_gui(self):
        """
        This function puts pictures of the suitable player in the gui board
        according to the Game board class that is being updated after each
        player's move.
        """
        # each time it is being called it puts pictures according to the
        # coordinates that are being marked in the Game board.
        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                if game.get_player_at(i, j) == 1:
                    # puts a suitable player's picture on the button that is
                    # bounded to the canvas in a specific coordinate
                    self.__gui_board[i][j].children.get('!button').\
                        config(image=self.daenerys, bg='OrangeRed3')
                elif game.get_player_at(i, j) == 2:
                    # puts a suitable player's picture on the button that is
                    # bounded to the canvas in a specific coordinate
                    self.__gui_board[i][j].children.get('!button').\
                        config(image=self.johnsnow, bg='OrangeRed3')

    def __check_turn(self):
        """
        This function sets a gold colored border around a player picture if it
        it's turn.
        """
        # checks who's turn is it
        if game.player_A_discs_num <= game.player_B_discs_num:
            self.daenerys_rules_label.config(bd=10, bg='gold2')
            self.johnsnow_rules_label.config(bd=10, bg='gray12')
        else:
            self.johnsnow_rules_label.config(bd=10, bg='gold2')
            self.daenerys_rules_label.config(bd=10, bg='gray12')

    def __handle_winning(self):
        """
        This function checks the status of the game. It displays a suitable
        massage to the gui board who is the winner or if it's a tie. In
        addition it calls a function to change the pictures of the winning
        discs. Finally, it ends the game if needed and calls the 'play again'
        function.
        """
        if self.status == PLAYER_A_WON:   # if player A won
            self.__winning_pic()  # changes for winning pictures
            # resets all the borders of the player's pictures to gray
            self.johnsnow_rules_label.config(bd=10, bg='gray12')
            winning_label1 = Label(self.__canvas, text='Player A - you Won!',
                                   font='times 50 bold', fg='gold2',
                                   bg='gray12')
            winning_label1.place(anchor='n', relx=0.5, rely=0.01)
            self.__end_game = True
            self.__play_again()

        elif self.status == PLAYER_B_WON:  # if player B won
            self.__winning_pic()  # changes for winning pictures
            # resets all the borders of the player's pictures to gray
            self.daenerys_rules_label.config(bd=10, bg='gray12')
            winning_label2 = Label(self.__canvas, text='Player B - you Won!',
                                   font='times 50 bold', fg='gold2',
                                   bg='gray12')
            winning_label2.place(anchor='n', relx=0.5, rely=0.01)
            self.__end_game = True
            self.__play_again()

        elif self.status == TIE:  # if no one won
            # resets all the borders of the player's pictures to gray
            self.daenerys_rules_label.config(bd=10, bg='gray12')
            self.johnsnow_rules_label.config(bd=10, bg='gray12')
            winning_label3 = Label(self.__canvas, text='A tie',
                                   font='times 50 bold', fg='gold2',
                                   bg='gray12')
            winning_label3.place(anchor='n', relx=0.5, rely=0.01)
            self.__end_game = True
            self.__play_again()

    def __winning_pic(self):
        """
        This function gets the last's disc entered row, col and player's
        symbol. It gets that disc from the Game class. It leads to 3 functions
        for checking the exact indices of the 4 winning discs.
        :return: exits function if the indices were found.
        """
        i = game.get_last_disc_entered()[ROW]  # the row of the last disc
        j = game.get_last_disc_entered()[COL]  # the col of the last disc
        # the players symbol of the last disc
        player = game.get_last_disc_entered()[2]
        if self.__search_winning_in_a_row(i, player):
            # searches for indices in the row that the last disc was entered.
            return
        if self.__search_winning_in_a_col(j, player):
            # searches for indices in the col that the last disc was entered.
            return
        if self.__search_winning_in_diagonals(i, j, player):
            # searches for indices in diagonal direction that the last disc
            # was entered.
            return

    def __search_winning_in_a_row(self, i, player):
        """
        This function searches for 4 same discs as the last disc that was
        entered. It searches for a sequence of 4 of the last disc's symbol.
        If found, it updates all the indices found to the winning function.
        It searches in the row that the last disc was entered.
        :param i: the row that the last disc was entered
        :param player: the players symbol of the last disc
        :return: True if found and updated in the row
        """
        joined_lst = ''.join(game.get_board()[i])
        # finds first index in the sequence if exists.
        found = joined_lst.find(player * WINNING_SEQ)
        if player * WINNING_SEQ in joined_lst:
            for index in range(found, found + WINNING_SEQ):
                # updates gui board
                self.__gui_board[i][index].children.get('!button').\
                    config(image=self.crown, bg='white')
            return True

    def __search_winning_in_a_col(self, j, player):
        """
        This function searches for 4 same discs as the last disc that was
        entered. It searches for a sequence of 4 of the last disc's symbol.
        If found, it updates all the indices found to the winning function.
        It searches in the col that the last disc was entered.
        :param j: the col that the last disc was entered
        :param player: the players symbol of the last disc
        :return: True if found and updated in the row
        """
        winning_col = [self.__board[0][j], self.__board[1][j],
                       self.__board[2][j], self.__board[3][j],
                       self.__board[4][j], self.__board[5][j]]
        joined_lst = ''.join(winning_col)
        # finds first index in the sequence if exists.
        found = joined_lst.find(player * WINNING_SEQ)
        if player * WINNING_SEQ in joined_lst:
            for index in range(found, found + WINNING_SEQ):
                # updates gui board
                self.__gui_board[index][j].children.get('!button').\
                    config(image=self.crown, bg='white')
            return True

    def __search_winning_in_diagonals(self, i, j, player):
        """
        This function searches for 4 same discs as the last disc that was
        entered. It searches for a sequence of 4 of the last disc's symbol.
        If found, it updates all the indices found to the winning function.
        It searches all the possible 4 coordinates in a diagonal direction
        that the last disc that was entered is in. It does it by calling 2
        function to do so. This function supplies the 2 functions with the
        possible list of 4 possible coordinates in diagonal direction..
        :param i: the row that the last disc was entered
        :param j: the col that the last disc was entered
        :param player: the players symbol of the last disc
        :return: True if found and updated in the row
        """
        diag1 = [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)]
        if self.__check_diagonals(diag1, player):
            self.__update_diagonals(diag1)
            return True

        diag2 = [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i + 1, j - 1)]
        if self.__check_diagonals(diag2, player):
            self.__update_diagonals(diag2)
            return True

        diag3 = [(i, j), (i - 1, j + 1), (i + 1, j - 1), (i + 2, j - 2)]
        if self.__check_diagonals(diag3, player):
            self.__update_diagonals(diag3)
            return True

        diag4 = [(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)]
        if self.__check_diagonals(diag4, player):
            self.__update_diagonals(diag4)
            return True

        diag5 = [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)]
        if self.__check_diagonals(diag5, player):
            self.__update_diagonals(diag5)
            return True

        diag6 = [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i - 1, j - 1)]
        if self.__check_diagonals(diag6, player):
            self.__update_diagonals(diag6)
            return True

        diag7 = [(i, j), (i + 1, j + 1), (i - 1, j - 1), (i - 2, j - 2)]
        if self.__check_diagonals(diag7, player):
            self.__update_diagonals(diag7)
            return True

        diag8 = [(i, j), (i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)]
        if self.__check_diagonals(diag8, player):
            self.__update_diagonals(diag8)
            return True

    def __check_diagonals(self, diag_lst, player):
        """
        This function is being called to check if the given list of indices of
        one possible diagonal is in the board and doesn't exceeds the board.
        :param diag_lst: list of 4 possible coordinates in diagonal direction.
        :param player: the players symbol of the last disc
        :return: True if the indices doesn't exceeds the board and the list
        includes exactly 4 same discs to the players symbol given.
        """
        flag = True
        # checks if all the 4 coordinates are a sequence of 4 suitable discs.
        try:
            for item in diag_lst:
                if self.__board[item[ROW]][item[COL]] != player:
                    flag = False
        except IndexError:
            flag = False
            return flag
        else:
            return flag

    def __update_diagonals(self, diag_lst):
        """
        If the list of a sequence of 4 discs in a diagonal direction returned
        True, it updates thr gui board according to all the coordinates from
        that list. It replaces the player's pictures to a winning pictures.
        :param diag_lst: list of 4 possible coordinates in diagonal direction.
        """
        for item in diag_lst:
            self.__gui_board[item[ROW]][item[COL]].children.get('!button').\
                config(image=self.crown, bg='white')

    def __play_again(self):
        """
        This function asks the user for another game after current game is
        over.
        """
        play_again_label = Label(self.__canvas, text='Play again?',
                                 font='times 26 bold', fg='white', bg='gray12')
        play_again_label.place(anchor='s', relx=0.5, rely=0.8)

        yes_button = Button(self.__canvas, text='YES', font='times 18 bold',
                            fg='OrangeRed3', bg='gray12',
                            command=self.__open_new_window)
        yes_button.place(anchor='s', relx=0.6, rely=0.9)
        no_button = Button(self.__canvas, text='NO', font='times 18 bold',
                           fg='gray60', bg='gray12',
                           command=self.__first_window.get_quit_game())
        no_button.place(anchor='s', relx=0.4, rely=0.9)

    def __open_new_window(self):
        """
        This function is being called if the user wants to play again. It
        resets the board and the number of discs each player gained from the
        previous game. Finally, it opens the first window.
        """
        # resets the board
        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                if game.get_player_at(i, j):
                    self.__board[i][j] = game.EMPTY_PLACE

        # resets the discs
        game.player_A_discs_num = 0
        game.player_B_discs_num = 0

        new_window = Toplevel(self.__parent)  # opens new window on same root
        # shuts down the program when exit is being clicked.
        new_window.protocol("WM_DELETE_WINDOW", on_close)
        self.__parent.withdraw()  # closes previous window
        MenuWindow(new_window)  # calls the first window


def on_close():
    """
    This function is called to close the program if the exit button was
    pressed.
    """
    root.destroy()


if __name__ == '__main__':
    game = Game()
    ai1 = AI(game, 1)
    ai2 = AI(game, 2)
    root = Tk()
    root.title("4 IN A ROW")
    gui = MenuWindow(root)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


