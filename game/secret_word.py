import random
"""
This class is risponsible for choosing randomly a secret word
    1- you need to create a cunstructor 
    2- you need to create the attributes:
    3-you need to create the mothods

Author: Yami
"""

#from random_word import RandomWords
#r = RandomWords()


class Secret_word:
    """This class is risponsible OF choosing a random secret word for the game

    Attributes:
    
    random_words (word): This will store the random words created by the random_word library
    word (word): This is going to have the secret selected random word

    """
  

    def __init__(self):
        self._word = ""
        self._word_list = []
        word_characters_list = []


    def secret_word(self):  

        #return a single random word in CAPS

        #self._word = r.get_random_word() 
        #self._word_list = list(self._word)

        self._word_list = ["apple", "ability", "agency", "argue", "attack", "biscuit", "baby", "behavior", "blue", "budget",
         "camel", "campaign", "choice", "cup", "crime", "dinosaur", "design", "draw", "difference", "despite", "elegance",
         "education", "exactly", "executive", "evidence", "family", "fear", "follow", "forward", "future", "galaxy", "government",
         "guy", "green", "growth", "helicopter", "health", "hinky", "hug", "hello", "image", "isolation", "inteligence", "informal",
         "impostor", "juice", "job", "jar", "jewerly", "jellybean", "king", "kind", "koala", "knife", "kitten", "lemonade", "lion", 
         "labyrinth", "laborious", "list", "minotaur", "machine", "manufacture", "monitory", "memory", "nature", "nutrient", "network",
         "northeast","nuclear","observe", "occupancy", "octagonal", "orange", "older", "pineaple", "paradigm", "personally", "peach", 
         "painless", "queen", "quatre", "quiet", "question", "quarentine", "restored", "revelation", "richly", "ruler", "royal", "snake",
         "speed", "smartphone", "single", "silver", "tangible", "tasty", "thankful", "thirsty", "taco", "uniform", "urban", "unicorn"]
        
        self._word = random.choice(self._word_list)

        return self._word
    

    def _hidden_word(self):

        word_characters_list = list(self._word)

        for each_character in word_characters_list:
            each_character = "_ " * len(word_characters_list)

            return each_character
        

            
        