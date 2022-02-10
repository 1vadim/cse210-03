"""
This class is risponsible for choosing randomly a secret word
    1- you need to create a cunstructor 
    2- you need to create the attributes:
    3-you need to create the mothods

Author: Yami
"""

from random_word import RandomWords
r = RandomWords()


class Secret_word:
    """This class is risponsible OF choosing a random secret word for the game

    Attributes:
    
    random_words (word): This will store the random words created by the random_word library
    word (word): This is going to have the secret selected random word

    """
  

    def __init__(self):
        self._word = ""
        self._word_list = []
        self._another_word = ""
        word_characters_list = []


    def secret_word(self):  

        #return a single random word in CAPS

        self._word = r.get_random_word() 
        self._word_list = list(self._word)
        
        for character in self._word_list:
            if character == "-" or character == " " or character == "'" or character == "," or character == "." or character == "_":
                self._word = "Biscuit" 
                return self._word   

            return self._word
        

    def _hidden_word(self):

        word_characters_list = list(self._word)

        for each_character in word_characters_list:
            each_character = "_ " * len(word_characters_list)

            return each_character
        

            
        