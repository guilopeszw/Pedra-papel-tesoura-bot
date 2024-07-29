import random # tive essa ideia para testar/estudar a biblioteca random de Python.

# bem vindo:
print("Olá, seja bem vindo ao bot de pedra, papel e tesoura!")

# utilizei o def jogo() com while true pra garantir que o jogo só vai se encerrar quando o usuário decidir
def jogo():
    while True:
        jogadas = {"pedra": 0, "papel": 1, "tesoura": 2}
        jogadorBot = random.choice(list(jogadas.keys()))
        jogador = str(
            input("Você quer jogar pedra, papel ou tesoura? ")).lower().strip()
        if jogador not in jogadas:
            continuar = str(input("Jogada inválida. Você deseja tentar novamente? "))
            if continuar == "sim" or continuar == "s" or continuar == "ss":
                continue
            else:
                print("Obrigado por jogar!")
                break # foi importante fazer isso pois, novamente, garante autonomia ao usuário
# robô jogou tesoura:
        elif jogador == "pedra" and jogadorBot == "tesoura":
            print("Você venceu. O robô jogou tesoura.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
        elif jogador == "papel" and jogadorBot == "tesoura":
            print("Você perdeu. O robô jogou tesoura.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
# robô jogou papel:
        elif jogador == "pedra" and jogadorBot == "papel":
            print("Você perdeu. O robô jogou papel.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
        elif jogador == "tesoura" and jogadorBot == "papel":
            print("Você venceu. O robô jogou papel.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
# robô jogou pedra:
        elif jogador == "papel" and jogadorBot == "pedra":
            print("Você venceu. O robô jogou pedra.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
        elif jogador == "tesoura" and jogadorBot == "pedra":
            print("Você perdeu. O robô jogou pedra.")
            continuar = str(input("Você deseja continuar jogando? "))
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
# empate:
        if jogador == jogadorBot:
            print("Empate. Jogue novamente.")
            if continuar == "não" or continuar == "n" or continuar == "nn":
                print("Obrigado por jogar!")
                break
            else:
                continue 
jogo()
