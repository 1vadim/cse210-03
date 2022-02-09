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
        self._parachute_graphic = self.__set_parachute_graphic()

    def get_game_over_value(self):
        return self._game_over
    
    def get_parachute_graphic(self):
        return self._parachute_graphic
        
    def __set_parachute_graphic(self):
        return [" ___ ","/___\\","\   /"," \ /","  0"," /|\\"," / \\"] 
        #return ["  0"," /|\\"," / \\"] 

    def check_input_letter(self,letter,secretWord):
        guessed = False
        self.__set_parachute_graphic()
        for index in range(len(secretWord._secret_word)):
            if secretWord._secret_word[index] == letter:
                self.__set_letter_in_list(index,letter,secretWord)
                guessed = True
            

        if not guessed:
            if self._parachute_graphic[0] == "  0":
                self._parachute_graphic[0] = "  x"
                self._game_over = True
            else:
                del self._parachute_graphic[0]


        self.prueba_de_letras_adivinadas(secretWord)
        self.prueba_de_paracaidas()
        

    def __set_letter_in_list(self,index,letter,secretWord):
        if secretWord._hidden_word[index] == "_":
            secretWord._hidden_word[index] = letter
        
    def prueba_de_paracaidas(self):
        for i in self._parachute_graphic:
            print(i)
    def prueba_de_letras_adivinadas(self,secretWord):
        display = ""
        for i in secretWord._hidden_word:
            display += f" {i}" 
        display += "\n"    
        print(display)
