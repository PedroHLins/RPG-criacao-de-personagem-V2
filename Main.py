from Aventura import Aventura
from Classe.Guerreiro import Guerreiro
from Classe.Ladrao import Ladrao
from Classe.Mago import Mago
from Personagem import Personagem
from Raca.Anao import Anao
from Raca.Elfo import Elfo
from Raca.Halfling import Halfling
from Raca.Humano import Humano

def escolher_raca():
    racas = ["Humano", "Elfo", "Anao", "Halfling"]
    print("\n<<Raças disponíveis>>\n")
    for i, v in enumerate(racas, start=1):
        print(f"{i}. {v}")

    escolha = int(input(f"\nEscolha a raça pelo número: "))

    match escolha:
        case 1: return Humano()
        case 2: return Elfo()
        case 3: return Anao()
        case 4: return Halfling()
        case _:
            print("\nopção inválida")
            return escolher_raca()

def escolher_classe():
    classes = ["Guerreiro", "Ladrao", "Mago"]
    print("\n<<Classes disponíveis>>\n")
    for i, v in enumerate(classes, start=1):
        print(f"{i}. {v}")

    escolha = int(input(f"\nEscolha a classe pelo número: "))

    match escolha:
        case 1:
            return Guerreiro()
        case 2:
            return Ladrao()
        case 3:
            return Mago()
        case _:
            print("\nopção inválida")
            return escolher_classe()

def criar_personagem():
    nome = input("Nome do seu personagem: ")
    raca_escolhida = escolher_raca()
    classe_escolhida = escolher_classe()

    return Personagem(nome, raca_escolhida, classe_escolhida)

def definir_estilo_aventura(novo_personagem):
    print("Selecione estilo da aventura: ")
    print("\n1 - Estilo Clássico")
    print("2 - Estilo Aventureiro")
    print("3 - Estilo Heróico")

    aventura = input("\n")

    match aventura:
        case "1":
            Aventura.classico(novo_personagem)
        case "2":
            Aventura.aventureiro(novo_personagem)
        case "3":
            Aventura.heroico(novo_personagem)
        case _:
            print("Selecione uma aventura válida")

if __name__ == '__main__':
    personagem = criar_personagem()
    definir_estilo_aventura(personagem)
    print("\n" * 50)
    personagem.exibir_personagem()
