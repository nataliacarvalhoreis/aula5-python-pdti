# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O
# jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na
# primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você
# tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você
# perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
# "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este
# número novamente. Você perde, no entanto, se tirar um 7 antes de tirar
# este Ponto novamente.
import random

#JOGAR DADOS
def jogar():
    jogada = random.randint(2,12)
    return jogada

#jogo
quantidade_de_jogadas = 1
termina = False
ponto = 0

while not termina:
    jogada = jogar()
    if quantidade_de_jogadas == 1:
        if jogada == 7 or jogada == 1:
            print("Parabéns! Você é um natural e você ganhou!")
            termina = True
        elif jogada == 2 or jogada == 3 or jogada == 12:
            print(" CRAPS! Você perdeu!")
            termina = True
        elif jogada >= 4 and jogada <=10:
            ponto = jogada
            print(f"{jogada}: Este é o seu ponto! Você deve tentar tirá-lo novamente, "
                  f"mas se tirar o 7 você perde!")
    else:
        if jogada == ponto:
            print("Parabéns! Você ganhou!")
            termina = True
        elif jogada == 7:
            print(f"CRAPS! Você perdeu!")
            termina = True
        else:
            print("Tente novamente!")
    quantidade_de_jogadas += 1

