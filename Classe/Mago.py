from Classe.Classe import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__("Mago", 10, 1)
        self.armas = ["Pequenas"]
        self.armaduras = ["Nenhuma"]
        self.itens_magicos = ["Todas"]
        # habilidade : nível necessário para usar habilidade
        self.habilidades = {"Magias arcanas": 1, "Ler magias": 1, "Detectar magias": 1}

    def exibir_habilidades(self):
        super().exibir_habilidades()