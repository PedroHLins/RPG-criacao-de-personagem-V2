from Raca.Raca import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__("Halfling", 6, 0, "Neutro")
        self.habilidades = ["Furtivo", "Destemidos", "Bom de mira", "Pequeno", "Restricoes"]

    def exibir_habilidades(self):

        print(f"<<Habilidades de Elfo>>")
        for hablidade in self.habilidades:
            print(hablidade)