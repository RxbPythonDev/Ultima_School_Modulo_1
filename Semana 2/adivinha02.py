from random import randint

numero = randint(1, 10)

chute = int(input('digite seu chute: '))

if chute == numero:
    print('Parabéns você acertou!')
else:
    print('Você errou, o número era ', numero)

print('FIM DO PROGRAMA')