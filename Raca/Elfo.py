from Raca.Raca import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", 9, 18, "Neutro")
        self.habilidades = ["Percepcao natural", "Gracioso", "Arma Racial", "Imunidade"]

    def exibir_habilidades(self):

        print(f"<<Habilidades de Elfo>>")
        for hablidade in self.habilidades:
            print(hablidade)