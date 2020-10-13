# -*- coding: utf-8 -*-

import os
from internal.Leaderboard import Leaderboard
from internal.Game import Game
from internal.Launcher import Launcher

if __name__ == "__main__" :
    os.system("cls")

    game = Launcher(2.2)   #Me permet de sortir la version

    print("♦♦♦ WELCOME ON SNAKE v"+ str(game.version) + " ♦♦♦")
    print()

    game.initialisation()

    # MutliJoueurs
    if game.nb_player == 2 :
        game.two_players()


    # Seul
    if game.nb_player == 1 :
        game.solo()

    os.system("cls")
    key = input("Voulez-vous fermer le jeu ? (o/n) : ")
    while key != "o" and key != "n":
        key = input("Voulez-vous fermer le jeu ? (o/n) : ")

    while key == "n" :
        os.system("cls")
        print("♦♦♦ WELCOME ON SNAKE v"+ str(game.version) + " ♦♦♦")
        print()

        game.initialisation()

        # MutliJoueurs
        if game.nb_player == 2 :
            game.two_players()


        # Seul
        elif game.nb_player == 1 :
            game.solo()

        os.system("cls")
        key = input("Voulez-vous fermer le jeu ? (o/n) : ")
        while key != "o" and key != "n":
            key = input("Voulez-vous fermer le jeu ? (o/n) : ")



    
    
    
