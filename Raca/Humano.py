from Raca.Raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", 9, 0, "Qualquer")
        self.habilidades = ["Aprendizado", "Adaptabilidade"]

    def exibir_habilidades(self):
        print(f"<<Habilidades de Humano>>")
        for hablidade in self.habilidades:
            print(hablidade)