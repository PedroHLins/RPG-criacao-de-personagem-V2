class Personagem:

    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.atributos = {
        "Forca": 0,
        "Destreza": 0,
        "Constituicao": 0,
        "Inteligencia": 0,
        "Sabedoria": 0,
        "Carisma": 0
    }

    def exibir_personagem(self):
        print("\nNível:", self.nivel)
        print("Nome:", self.nome)
        print("Raça:", self.raca.nome)
        print("Classe:", self.classe.nome)
        self.raca.exibir_habilidades()
        self.classe.exibir_habilidades()
        for atributo in self.atributos:
            print("{:<12} ".format(atributo), end="")
            for i in range(self.atributos[atributo]):
                print("■", end="")
            print(" (", self.atributos[atributo] ,")", "\n" , end="")