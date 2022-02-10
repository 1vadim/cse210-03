from .secret_word import Secret_word
"""
    this class is going to control the sequence of the game

    1- you need to create a cunstructor 
    2- you need to create the attributes:
    3-you need to create the mothods
        start_game =
Author: Vadym Chemariev
"""
class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): A secret word.
        is_playing (boolean): Whether or not to keep playing.
        parachute (Parachute): Gussed or not a letter in a word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """

        self._word = Secret_word()
        self.random_word = ""
        self.length = 0
        self.secret_word_for_game = ""
        self._is_playing = True
        self._parachute = ""
        self._terminal_service = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()


    def rand_word (self):
        """Will store the randome word"""
        random_word = self._word
        secret_word_for_game = random_word.secret_word()
        word_length = random_word._hidden_word()
        
        return word_length

        #Following line was just to see if works:
        #print(f"Word: {secret_word_for_game} -- Length: {word_length}")

    def _get_inputs(self):
        """The player guesses the letter.

        Args:
            self (Director): An instance of Director.
        """

    def _do_updates(self):
        """Evaluates if the player input is or not in the secret word

        Args:
            self (Director): An instance of Director.
        """

    def _do_outputs(self):
        """Provides a graphical output and a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
