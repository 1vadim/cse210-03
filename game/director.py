from game.secret_word import Secret_word
from game.player_parachute import Player_parachute
from game.terminal_service import Terminal_service
"""
    this class is going to control the sequence of the game

    Author: Vadym Chemariev, Samuel Beltran
"""
class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): A secret word.
        is_playing (boolean): Whether or not to keep playing.
        parachute (Parachute): Gussed or not a letter in a word.
        terminal_service: For getting and displaying information on the terminal.
        _letter: this will get the inputs player
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """

        self._word = Secret_word()
        self._empty_word = []
        self._is_playing = True
        self._parachute = Player_parachute()
        self._terminal_service = Terminal_service()
        self._letter = ""

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self._word.secret_word()
        self._terminal_service.display_empty_word(self._word._empty_word)
        self._terminal_service.display_parachute_graphic(self._parachute._parachute_graphic)
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """The player guesses the letter.

        Args:
            self (Director): An instance of Director.
        """
        
        self._terminal_service.ask_players_input()
        self._letter = self._terminal_service.get_players_input()

    def _do_updates(self):
        """Evaluates if the player input is or not in the secret word

        Args:
            self (Director): An instance of Director.
        """
        self._parachute.check_input_letter(self._letter,self._word)

    def _do_outputs(self):
        """Provides a graphical output and a hint for the player to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.display_empty_word(self._word._empty_word)
        self._terminal_service.display_parachute_graphic(self._parachute._parachute_graphic)

        if self._parachute.check_empty_word_is_full(self._word._empty_word):
            self._terminal_service.display_win_message()
            self._is_playing = False

        if self._parachute._game_over:
            self._terminal_service.display_game_over()
            self._is_playing = False
