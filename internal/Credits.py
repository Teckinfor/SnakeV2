class Credits :

    def __init__(self, version):
        self._developper = ["Julien Sénéchal"]
        self._version = version

    @property
    def developper(self):
        return self._developper

    @developper.setter
    def developper(self, new_developper):
        self._developper = new_developper

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, other_version):
        self._version = other_version

    def show_fr(self):
        print(">>>>>SNAKE<<<<<")
        print("Version : "  + str(self._version), "- VERSION CONSOLE")
        print()
        print("Developper principal : " , end="")
        for person in self.developper :
            print(person, end=", ")
        print()
        print()
        print("Plus d'informations :")
        print("Travail de fin d'année a réaliser pour le cours de Programmation pour cause de Covid-19")
        print("qui rendit l'examen en présentiel impossible pour tous les etudiants en 1er Bloc")
        print("de la filière de sécuritée des systèmes ainsi que de la filière de la technologie")
        print("de l'informatique.")
        print()
        print("Date de fin de projet :")
        print("28/05/2020")

    def show_en(self):
        print(">>>>>SNAKE<<<<<")
        print("Version : "  + str(self._version), "- VERSION CONSOLE")
        print()
        print("Main Developper : " , end="")
        for person in self.developper :
            print(person, end=", ")
        print()
        print()
        print("More informations :")
        print("Due to Covid-19, this year-end work was to return for the programming course")
        print("because the face exam was impossible for all students in 1st Block")
        print("of the systems security sector as well as the computer technology sector")
        print()
        print("Project end date :")
        print("28/05/2020")
