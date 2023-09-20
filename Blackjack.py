import random
jogada_jogador = True
jogada_casa = True

#cartas do baralho /
baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        "J", "Q", "K", "A",
        "J", "Q", "K", "A",
        "J", "Q", "K", "A",
        "J", "Q", "K", "A"]
mao_jogador = []
mao_casa = []
#distribuir cartas
def destribuir(turno):
    carta = random.choice(baralho)
    turno.append(carta)
    baralho.remove(carta)
#calcular o total de cada mão
def total(turno):
    total = 0
    mostrar = ["J", "Q", "K"]
    for carta in turno:
        if carta in range(1, 11):
            total += carta
        elif carta in mostrar:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
#checar o vencedor
def mostrar_mao_casa():
    if len(mao_casa) == 2:
        return mao_casa[0]
    elif len(mao_casa) > 2:
        return mao_casa[0], mao_casa[1]

#game Loop
for _ in range(2):
    destribuir(mao_casa)
    destribuir(mao_jogador)
while jogada_jogador or jogada_casa:
    print(f"A casa tem {mostrar_mao_casa()} e X")
    print(f"Você tem {mao_jogador} que soma um total de {total(mao_jogador)}")
    if jogada_jogador:
        manter_ou_sair = input("1: Manter\n2: Sair\n")
    if total(mao_casa) > 16:
        jogada_casa = False
    else:
        destribuir(mao_casa)
    if manter_ou_sair == "1":
        jogada_jogador = False
    else:
        destribuir(mao_jogador)
    if total(mao_jogador) >= 21:
        break
    elif total(mao_casa) >= 21:
        break

if total(mao_jogador) == 21:
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("Blackjack! Você VENCEU!")
elif total(mao_casa) == 21:
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("Blackjack! A casa DERROTOU você!")
elif total(mao_jogador) > 21:
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("Deu mais de 21! A Casa te DERROTOU!")
elif total(mao_casa) > 21:
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("A Casa somou mais de 21! Você VENCEU!")
elif 21 - total(mao_casa) < 21 - total(mao_jogador):
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("A Casa te DERROTOU!")
elif 21 - total(mao_casa) > 21 - total(mao_jogador):
    print(f"\n Você tem {mao_jogador}que soma um total de {total(mao_jogador)} e a casa tem {mao_casa} que soma um total de {total(mao_casa)}")
    print("Você VENCEU!")




