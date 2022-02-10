import random
"""
This class is going to evaluate if the inputs player is or not in the chosen word
    
    1- you need to create a cunstructor 
    2- you need to create the attributes:
    3-you need to create the mothods
Author: Sam and jonathon 
"""
class Player_parachute:
    
    def __init__(self):
        self._game_over = False
        self._parachute_graphic = self.__get_parachute_graphic()
        #self._game_win = False

    #This returns from the _game_over  attribute its value
    def get_game_over_value(self):
        return self._game_over
    
    #This returns from the _parachute_graphic  attribute its value
    def get_parachute_graphic(self):
        return self._parachute_graphic

    #This returns the parachute graphic        
    def __get_parachute_graphic(self):
        return ["  ___ "," /___\\"," \   /","  \ /","   0","  /|\\","  / \\","\n","^^^^^^^^^^^","\n"] 

    #This checks if the player guesses a letter by a letter input
    def check_input_letter(self,letter,secretWord):
        guessed = False
        self.__get_parachute_graphic()
        wordStr = secretWord._word
        for index in range(len(wordStr)):
            if wordStr[index] == letter:
                self.__set_letter_in_list(index,letter,secretWord)
                guessed = True

        self.__update_players_parachute(guessed)    
    #This stores a letter in a list
    def __set_letter_in_list(self,index,letter,secretWord):
        hiddenWord = secretWord._empty_word
        if hiddenWord[index] == "_":
            hiddenWord[index] = letter
    
    #This cuts a line on the player's parachute.
    def __update_players_parachute(self,guessed):
        if not guessed:
            if self._parachute_graphic[0] == "  0":
                self._parachute_graphic[0] = "  x"
                self._game_over = True
            else:
                del self._parachute_graphic[0]
    #This checks if the list of "_" is full of letters
    def check_empty_word_is_full(self,secretWord):
        count = 0
        for i in secretWord:
            if i != "_":
                count += 1
        if  len(secretWord) == count:
            return True


