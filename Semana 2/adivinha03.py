from random import randint

numero = randint(1, 10)

chute = int(input('digite seu chute: '))

if chute == numero:
    print('Parabéns você acertou!')
elif chute < numero:
    print('Você errou, o número era maior!')
else:
    print('Você errou, o número era menor!')

print('FIM DO PROGRAMA')