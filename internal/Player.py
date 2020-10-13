from internal.readchar.readchar import * #Module ajouté permettant de lire un caractère sans devoir appuyer sur ENTER
import os

class Player :
    #On encode chaque avancée de position pour chaque touche
    #Attribut de classe
    keyboard_key = {'z':(-1,0),
                    'q':(0,-1),
                    's':(1,0),
                    'd':(0,1)}
    
    #On construit une instance de la classe "Player"
    def __init__(self, name, game = None, points = 0, start = (0,0)):
        self.name = name
        self.points = points
        self.position = start
        self.last_position = start
        self.game = game
    
    
    def move (self) :
        print("Mouvement (z,q,s,d)")
        key = readkey()           #entrée
        while key not in Player.keyboard_key.keys() :   # On vérifie qu'il s'agit bien d'une des 4 touches
            key = readkey()
                
        move = Player.keyboard_key[key]

        if not self.last_position == (self.position[0] + move[0], self.position[1] + move[1]) :
            self.last_position = self.position
            self.position = (self.position[0] + move[0], self.position[1] + move[1])
        os.system("cls")
                

    def move_outlimits(self):

        if self.position[0] >= self.game.board_size :
            self.position = (self.position[0] - self.game.board_size, self.position[1])
        
        elif self.position[0] < 0 :
            self.position = (self.position[0] + self.game.board_size, self.position[1])

        elif self.position[1] >= self.game.board_size :
            self.position = (self.position[0], self.position[1] - self.game.board_size)

        elif self.position[1] < 0 :
            self.position = (self.position[0], self.position[1] + self.game.board_size)