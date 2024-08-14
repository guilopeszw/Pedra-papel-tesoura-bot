# tive essa ideia para testar/estudar a biblioteca random de Python.
import random

# bem vindo:
print("Olá, seja bem vindo ao bot de pedra, papel e tesoura!")

# utilizei o def jogo() com while pra garantir que o jogo só vai se encerrar quando o usuário decidir

def jogo():
    continuar = "sim"
    while continuar == "sim" or continuar == "ss" or continuar == "s":
# bot:
        jogadas = {"pedra": 0, "papel": 1, "tesoura": 2}
        jogadorBot = random.choice(list(jogadas.keys()))
# jogador:
        jogador = str(
            input("Você quer jogar pedra, papel ou tesoura? ")).lower().strip()
# checagem da jogada:
        if jogador not in jogadas:
            continuar = str(
                input("Jogada inválida. Você deseja tentar novamente? ")).lower().strip()
# robô jogou tesoura:
        if jogador == "pedra" and jogadorBot == "tesoura":
            print("Você venceu. O robô jogou tesoura.")
        elif jogador == "papel" and jogadorBot == "tesoura":
            print("Você perdeu. O robô jogou tesoura.")
# robô jogou papel:
        elif jogador == "pedra" and jogadorBot == "papel":
            print("Você perdeu. O robô jogou papel.")
        elif jogador == "tesoura" and jogadorBot == "papel":
            print("Você venceu. O robô jogou papel.")
# robô jogou pedra:
        elif jogador == "papel" and jogadorBot == "pedra":
            print("Você venceu. O robô jogou pedra.")
        elif jogador == "tesoura" and jogadorBot == "pedra":
            print("Você perdeu. O robô jogou pedra.")
# empate:
        elif jogador == jogadorBot:
            print("Empate. Jogue novamente.")
# loop do while:
        continuar = str(input("Você deseja continuar jogando? ")).lower().strip()
jogo()
# finalização do jogo
print("Obrigado por jogar!")
