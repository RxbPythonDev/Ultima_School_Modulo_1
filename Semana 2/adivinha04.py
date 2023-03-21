from random import randint
numero = randint(1, 10)
tentativas = 5
while tentativas > 0:
    chute = int(input('digite seu chute: '))
    if chute == numero:
        print('Parabéns você acertou!')
        break
    elif chute < numero:
        print('Você errou, o número era maior!')
    else:
        print('Você errou, o número era menor!')
    tentativas = tentativas - 1
print('FIM DO PROGRAMA')