import random
import datetime

class Game :
    
    #On construit l'objet "Game"
    def __init__(self, player, launcher, size):
        self.player = player
        self.board_size = size
        self.candies = []
        self.ennemies = []
        self.launcher = launcher
        self.trail = []
        self.save_position = []
        
    # Dessine le plateau
    def draw(self):
        for line in range(self.board_size):
            for col in range(self.board_size):
                if (line, col) in self.trail:
                    print("M",end=" ")
                elif (line,col) in self.candies :
                    print("*",end=" ")
                elif (line,col) == self.player.position :
                    print("O",end=" ")
                elif (line,col) in self.ennemies:
                    print("♠",end=" ")
                else : 
                    print(".",end=" ")

            print()
            
    # Fait apparaitre un bonbon
    def pop_candy(self):
        new_candy = (random.choice(range(self.board_size)),random.choice(range(self.board_size)))
        if new_candy not in self.candies and new_candy not in self.trail and new_candy is not self.player.position :
            self.candies.append(new_candy)
            
    # Regarde s'il y a un bonbon à prendre (et le prend)
    def check_candy(self):
        if self.player.position in self.candies:
            self.player.points += 1
            self.candies.remove(self.player.position)
            self.add_trail()

    #Fait apparaître les ennemis
    def pop_ennemies(self):
        new_ennemy = (random.choice(range(self.board_size)), random.choice(range(self.board_size)))
        if new_ennemy not in self.ennemies and new_ennemy != self.player.position and new_ennemy not in self.trail:
            self.ennemies.append(new_ennemy)

    #Fait bouger les ennemis en fonction d'où se trouve le joueur
    def move_ennemies(self):
        i = 0
        while i != len(self.ennemies) :
            direction = random.randint(1,2) # Une chance sur 2 (soit a la vertical soit a l'horizontal)

            if direction == 1 :
                
                if self.ennemies[i][0] > self.player.position[0]:

                    if (self.ennemies[i][0] - 1,self.ennemies[i][1]) not in self.ennemies and (self.ennemies[i][0] - 1,self.ennemies[i][1]) not in self.candies and (self.ennemies[i][0] - 1,self.ennemies[i][1]) not in self.trail :
                        self.ennemies[i] = (self.ennemies[i][0] - 1,self.ennemies[i][1])
                
                elif self.ennemies[i][0] < self.player.position[0]:

                    if (self.ennemies[i][0] + 1,self.ennemies[i][1]) not in self.ennemies and (self.ennemies[i][0] + 1,self.ennemies[i][1]) not in self.candies and (self.ennemies[i][0] + 1,self.ennemies[i][1]) not in self.trail :
                        self.ennemies[i] = (self.ennemies[i][0] + 1,self.ennemies[i][1])
            
            if direction == 2 :

                if self.ennemies[i][1] > self.player.position[1]:
                    if (self.ennemies[i][0],self.ennemies[i][1] - 1) not in self.ennemies and (self.ennemies[i][0],self.ennemies[i][1] - 1) not in self.candies and (self.ennemies[i][0],self.ennemies[i][1] - 1) not in self.trail :
                        self.ennemies[i] = (self.ennemies[i][0],self.ennemies[i][1] - 1)
                
                elif self.ennemies[i][1] < self.player.position[1]:
                    if (self.ennemies[i][0],self.ennemies[i][1] + 1) not in self.ennemies and (self.ennemies[i][0],self.ennemies[i][1] + 1) not in self.candies and (self.ennemies[i][0],self.ennemies[i][1] + 1) not in self.trail :
                        self.ennemies[i] = (self.ennemies[i][0],self.ennemies[i][1] + 1)
            i += 1


    def move_trail(self):

        #On vérifie bien que le joueur a bien bougé (sinon la trainée rattraperait le joueur)
        i = len(self.save_position)
        if self.save_position[len(self.save_position) - 1] == self.player.position :
            del self.save_position[len(self.save_position) - 1]

        else :
            i = 0
            nb_trail = len(self.trail)
            nb_position = len(self.save_position)
            while i != nb_trail :
                self.trail[i] = self.save_position[nb_position - 1 - i]
                i += 1

    
    def add_trail(self):
        i = len(self.save_position)
        ii = len(self.trail)
        i -= 1 + ii
        self.trail.append(self.save_position[i - 1])

    def save_player_position(self):                             #Me sert a garder en mémoire les anciennes position du joueur afin de pouvoir agrandir sa trainée
        self.save_position.append(self.player.position)
        
    # Joue une partie complète
    def play(self):
        print("--- Début de la partie ---")
        self.draw()

        if self.launcher.level == 1 :
             
            end = Game.end_time(1,0)
            now = datetime.datetime.today()
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()
                
                if random.randint(1,3) == 1 :
                    self.pop_candy()

                if self.player.position in self.trail :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()

        if self.launcher.level == 2 :

            end = Game.end_time(1,0)
            now = datetime.datetime.today()
            GameOver = False
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()
                
                if random.randint(1,3) == 1 :
                    self.pop_candy()

                self.move_ennemies()
                
                if random.randint(1,15) == 1 :
                    self.pop_ennemies()
                
                for ennemy in self.ennemies:
                    if ennemy == self.player.position :
                        GameOver = True
                
                if self.player.position in self.trail :
                    GameOver = True
                
                if GameOver :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()

        if self.launcher.level == 3 :

            end = Game.end_time(1,0)
            now = datetime.datetime.today()
            GameOver = False
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()
                
                if random.randint(1,3) == 1 :
                    self.pop_candy()

                self.move_ennemies()
                
                if random.randint(1,10) == 1 :
                    self.pop_ennemies()
                
                for ennemy in self.ennemies:
                    if ennemy == self.player.position :
                        GameOver = True
                
                if self.player.position in self.trail :
                    GameOver = True
                
                if GameOver :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()

        if self.launcher.level == 4 :

            end = Game.end_time(1,0)
            now = datetime.datetime.today()
            GameOver = False
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()
                
                if random.randint(1,3) == 1 :
                    self.pop_candy()
                
                self.move_ennemies()
                
                if random.randint(1,5) == 1 :
                    self.pop_ennemies()
                
                for ennemy in self.ennemies:
                    if ennemy == self.player.position :
                        GameOver = True

                if self.player.position in self.trail :
                    GameOver = True
                
                if GameOver :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()
        
        if self.launcher.level == 5 :
            
            end = Game.end_time(2,0)
            now = datetime.datetime.today()
            GameOver = False
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()
                
                if random.randint(1,5) == 1 :
                    self.pop_candy()
                
                self.move_ennemies()
                
                if random.randint(1,2) == 1 :
                    self.pop_ennemies()
                
                for ennemy in self.ennemies:
                    if ennemy == self.player.position :
                        GameOver = True

                if self.player.position in self.trail :
                    GameOver = True
                
                if GameOver :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()

        if self.launcher.level == 0 :
            
            end = Game.end_time(self.launcher.minutes,self.launcher.seconds)
            now = datetime.datetime.today()
            GameOver = False
            
            while now < end :
                self.save_player_position()
                self.player.move()
                self.player.move_outlimits()
                self.check_candy()
                self.move_trail()

                
                if random.randint(1,self.launcher.pop_candy) == 1 :
                    self.pop_candy()
                
                self.move_ennemies()
                
                if random.randint(1,self.launcher.pop_ennemies) == 1 :
                    self.pop_ennemies()
                
                for ennemy in self.ennemies:
                    if ennemy == self.player.position :
                        GameOver = True

                if self.player.position in self.trail :
                    GameOver = True
                
                if GameOver :
                    print("GAME OVER")
                    break
                
                self.draw()    
                
                now = datetime.datetime.today()
        
        
        print("----- Terminé -----")
        print("Vous avez", self.player.points, "points" )


    @staticmethod
    # retourne le moment où le jeu est censé être fini
    def end_time(delta_minute, delta_second):
        delta = datetime.timedelta(minutes=delta_minute, seconds=delta_second)
        end = datetime.datetime.today() + delta
        return end