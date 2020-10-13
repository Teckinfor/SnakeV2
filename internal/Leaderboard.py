import ast #Va me permettre de modifier une string en dictionnaire (voir classe leaderboard)

class Leaderboard:

    def __init__(self, file_address) :
        self.file_address = file_address
    
    def show_leaderboard(self) :
        with open("internal/" + self.file_address, "r") as file :     # "With" permet de fermer mon fichier dès que j'ai fini mon code
            content = file.read()
            content = ast.literal_eval(content)      # On aurait pu écrire "content = ast.literal_eval(file.read())" mais ici j'ai préféré faire comme ça car ça me paraît beaucoup plus lisible

            print("1er :", content["1er"][0])
            print("avec", content["1er"][1], "points")
            print()

            print("2ème :", content["2eme"][0])
            print("avec", content["2eme"][1], "points")
            print()

            print("3ème :", content["3eme"][0])
            print("avec", content["3eme"][1], "points")
            print()


    def edit_leaderboard(self, name, points) :
        with open("internal/" + self.file_address, "r") as file :
            content = file.read()
            content = ast.literal_eval(content)
            
            if content["1er"][1] < points :
                content["3eme"] = [content["2eme"][0], content["2eme"][1]]
                content["2eme"] = [content["1er"][0], content["1er"][1]]
                content["1er"][0] = name
                content["1er"][1] = points
            
            elif content["2eme"][1] < points :
                content["3eme"] = [content["2eme"][0], content["2eme"][1]]
                content["2eme"][0] = name
                content["2eme"][1] = points

            elif content["3eme"][1] < points :
                content["3eme"][0] = name
                content["3eme"][1] = points
        
        with open("internal/" + self.file_address, "w") as file :
            file.write('{"1er":["'+ content["1er"][0] + '",' + str(content["1er"][1]) +
             '],\n "2eme":["' + content["2eme"][0] + '",' + str(content["2eme"][1]) +
             '],\n "3eme":["' + content["3eme"][0] + '",' + str(content["3eme"][1]) + ']}')