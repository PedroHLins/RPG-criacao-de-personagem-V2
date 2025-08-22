class Raca:
    def __init__(self, nome, movimento, infra_visao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infra_visao = infra_visao
        self.alinhamento = alinhamento
        self.habilidades = []

    def exibir_habilidades(self):
        print(f"\n<<Habilidades de {self.nome}>>")
        for hablidade in self.habilidades:
            print(hablidade, " | ", end="")
        print("\n")