from internal.Game import Game
from internal.Player import Player
from internal.Leaderboard import Leaderboard
from internal.Credits import Credits
import internal.readchar.readchar #Module ajouté permettant de lire un caractère sans devoir appuyer sur ENTER
import os

class Launcher :

    def __init__(self, version) :
        self.nb_player = None
        self.level = None
        self.minutes = None
        self.seconds = None
        self.size = 10
        self.pop_candy = None
        self.pop_ennemies = None
        self.version = version
    
    def solo(self):

        name_p1 = input("Votre nom : ")
        while len(name_p1) > 15 :
            print("Trop de caractère !")
            name_p1 = input("Votre nom : ")
        os.system("cls")
        PlayerOne = Player(name_p1)
        GameOne = Game(PlayerOne, self, self.size)
        PlayerOne.game = GameOne
        GameOne.play()
        self.check_leaderboard(PlayerOne.name, PlayerOne.points)
        input("Appuyez sur ENTER pour continuer")

    def two_players(self):

        name_p1 = str(input("Nom du Joueur 1 : "))
        while len(name_p1) > 15 :
            print("Trop de caractère !")
            name_p1 = str(input("Nom du Joueur 1 : "))
        name_p2 = str(input("Nom du Joueur 2 : "))
        while len(name_p2) > 15 :
            print("Trop de caractère !")
            name_p2 = str(input("Nom du Joueur 1 : "))
        PlayerOne = Player(name_p1)
        PlayerTwo = Player(name_p2)
        Game_p1 = Game(PlayerOne, self, self.size)
        Game_p2 = Game(PlayerTwo, self, self.size)
        PlayerOne.game = Game_p1
        PlayerTwo.game = Game_p2
        os.system("cls")

        #Partie Joueur 1
        print(name_p1 + " vous commencez !")
        input("Appuyez sur ENTER pour continuer")
        os.system("cls")

        Game_p1.play()
        self.check_leaderboard(PlayerOne.name, PlayerOne.points)

        input("Appuyez sur ENTER pour continuer")
        os.system("cls")

        #Partie joueur 2
        print(name_p2 + ", c'est votre tour !")
        input("Appuyez sur ENTER pour continuer")
        os.system("cls")

        Game_p2.play()
        self.check_leaderboard(PlayerTwo.name, PlayerTwo.points)

        input("Appuyez sur ENTER pour continuer")
        os.system("cls")

        #Comparaison des scores
        if PlayerOne.points > PlayerTwo.points :
            print(PlayerOne.name , "A GAGNE")

        else :
            print(PlayerTwo.name , "A GAGNE")

        print()
        print("Tableau des scores : ")
        print(PlayerOne.name , ":" , str(PlayerOne.points))
        print(PlayerTwo.name , ":" , str(PlayerTwo.points))
        print()
        input("Appuyez sur ENTER pour continuer")

    def number_players(self):
        i = 0
        while i == 0:
            try :
                print("1 - Un joueur")
                print("2 - Deux joueurs")
                self.nb_player = int(input("Select : "))

                while self.nb_player != 1 and self.nb_player != 2 :
                    os.system("cls")
                    print("!!! Entrée incorrecte !!!" )
                    print("Veuillez recommencer")
                    print()
                    print("1 - Un joueur")
                    print("2 - Deux joueurs")
                    self.nb_player = int(input("Select : "))
                os.system("cls")
                i = 1
            except :
                os.system("cls")
                print("!!! Entrée incorrecte !!!" )
                            
    def choose_level(self):
        i = 0
        while i == 0:
            try:
                print("Niveau de difficulté")
                print()
                print("1 - Facile")
                print("2 - Intermédiaire")
                print("3 - Difficile")
                print("4 - Extrême")
                print("5 - Impossible")
                print("0 - Personnalisé")
                self.level = int(input("Niveau : "))
                os.system("cls")

                while self.level != 1 and self.level != 2 and self.level != 3 and self.level != 4 and self.level != 5 and self.level != 0:
                    print("!!! Entrée incorrecte !!!" )
                    print("Veuillez recommencer")
                    print()
                    print("1 - Facile")
                    print("2 - Intermédiaire")
                    print("3 - Difficile")
                    print("4 - Extrême")
                    print("5 - Impossible")
                    print("0 - Personnalisé")
                    self.level = int(input("Niveau : "))
                    os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("!!! Entrée incorrecte !!!" )

        if self.level == 0 :
            self.own_level()

    def own_level(self):
        i = 0
        while i == 0:
            try :
                print("Durée - Minimum 30 secondes & Maximum 15 minutes")
                self.minutes = int(input("Minutes : "))
                self.seconds = int(input("Secondes : "))
                os.system("cls")

                while self.minutes > 15 or (self.minutes == 0 and self.minutes < 30) or (self.minutes == 15 and self.minutes != 0) :
                    print("Vous ne respectez pas la durée minimum/maximum")
                    print("Durée - Minimum 30 secondes & Maximum 15 minutes")
                    self.minutes = int(input("Minutes : "))
                    self.seconds = int(input("Secondes : "))
                    while self.seconds > 60 :
                        print("Une minute c'est maximum 60 secondes :-/ !")
                        self.seconds = int(input("Secondes : "))
                    os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Veuillez recommencer")

        i = 0
        while i == 0:
            try:
                print("Taille de la carte (minimum 3, maximum 20)")
                self.size = int(input("Taille : "))
                while self.size < 3 or self.size > 20:
                    print("Vous ne respectez pas le nombre minimum/maximum")
                    self.size = int(input("Taille : "))
                os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Veuillez recommencer")

        i = 0
        while i == 0:
            try:        
                print("Apparitions des bonbons - Min : 1 & Max : 100")
                self.pop_candy = int(input("Une chance sur... : "))
                while self.pop_candy < 1 or self.pop_candy > 100 :
                    print("Max/Min non respecté")
                    self.pop_candy = int(input("Une chance sur... : "))
                os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Veuillez recommencer")

        i = 0
        while i == 0:
            try:
                print("Apparitions des ennemis - Min : 1 & Max : 100")
                self.pop_ennemies = int(input("Une chance sur... : "))
                while self.pop_ennemies < 1 or self.pop_ennemies > 100 :
                    print("Max/Min non respecté")
                    self.pop_ennemies = int(input("Une chance sur... : "))
                os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Veuillez recommencer")
        
    def show_leaderboard(self):
        
        i = 0
        while i == 0:
            try:
                print("De quel niveau voulez-vous voir le tableau des scores ?")
                print()
                print("1 - Facile")
                print("2 - Intermédiaire")
                print("3 - Difficile")
                print("4 - Extrême")
                print("5 - Impossible")
                
                key = int(input("Niveau : "))
                os.system("cls")

                while key != 1 and key != 2 and key != 3 and key != 4 and key != 5 :
                    print("ERREUR - Vous n'avez pas selectionné une option valide")
                    print("De quel niveau voulez-vous voir le tableau des scores ?")
                    print()
                    print("1 - Facile")
                    print("2 - Intermédiaire")
                    print("3 - Difficile")
                    print("4 - Extrême")
                    print("5 - Impossible")
                    key = int(input("Niveau : "))
                    os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Vous n'avez pas selectionné une option valide")
        
            

        if key == 1 :
            easy_leaderboard = Leaderboard("data/leaderboard_easy.txt")
            easy_leaderboard.show_leaderboard()
        
        elif key == 2 :
            normal_leaderboard = Leaderboard("data/leaderboard_normal.txt")
            normal_leaderboard.show_leaderboard()

        elif key == 3 :
            hard_leaderboard = Leaderboard("data/leaderboard_hard.txt")
            hard_leaderboard.show_leaderboard()

        elif key == 4 :
            extreme_leaderboard = Leaderboard("data/leaderboard_extreme.txt")
            extreme_leaderboard.show_leaderboard()

        elif key == 5 :
            impossible_leaderboard = Leaderboard("data/leaderboard_impossible.txt")
            impossible_leaderboard.show_leaderboard()

    def check_leaderboard(self, nom, points):
        if self.level == 1 :
            easy_leaderboard = Leaderboard("data/leaderboard_easy.txt")
            easy_leaderboard.edit_leaderboard(nom, points)

        elif self.level == 2 :
            normal_leaderboard = Leaderboard("data/leaderboard_normal.txt")
            normal_leaderboard.edit_leaderboard(nom, points)

        elif self.level == 3 :
            hard_leaderboard = Leaderboard("data/leaderboard_hard.txt")
            hard_leaderboard.edit_leaderboard(nom, points)

        elif self.level == 4 :
            extreme_leaderboard = Leaderboard("data/leaderboard_extreme.txt")
            extreme_leaderboard.edit_leaderboard(nom, points)

        elif self.level == 5 :
            impossible_leaderboard = Leaderboard("data/leaderboard_impossible.txt")
            impossible_leaderboard.edit_leaderboard(nom, points)

    def credits(self):
        Credit = Credits(self.version)

        i = 0
        while i == 0:
            try :
                print("1 - Anglais")
                print("2 - Français")
                key = int(input("Selection : "))
                os.system("cls")

                while key != 1 and key != 2:
                    print("1 - Anglais")
                    print("2 - Français")
                    key = int(input("Selection : "))
                    os.system("cls")
                i = 1
            except :
                os.system("cls")
                print("ERREUR - Vous n'avez pas selectionné une option valide")

        if key == 1 :
            Credit.show_en()
            input("Appuyez sur ENTER pour continuer")
                
        elif key == 2 :
            Credit.show_fr()
            input("Appuyez sur ENTER pour continuer")

    # Initialisation du jeu
    def initialisation(self):

        i = 0
        while i == 0 :
            try:
                print("1 - Jouer")
                print("2 - Tableaux des scores")
                print("3 - Credits")
                print()
                key = int(input("Selection : "))
                os.system("cls")
                while key != 1 :
                    if key == 2 :
                        self.show_leaderboard()
                        input("Appuyer sur ENTER pour continuer")

                    elif key == 3 :
                        self.credits()

                    os.system("cls")
                    print("1 - Jouer")
                    print("2 - Tableaux des scores")
                    print("3 - Credits")
                    print()
                    key = int(input("Selection : "))
                    os.system("cls")
                i = 1
            except:
                os.system("cls")
                print("ERREUR - Vous n'avez pas selectionné une option valide")

        os.system("cls")
        self.number_players()
        self.choose_level()