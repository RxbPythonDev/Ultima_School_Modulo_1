from random import randint
numero = randint(1, 100)
tentativas = 5
while tentativas > 0:
    chute = int(input('digite seu chute: '))
    diferenca = numero - chute
    if diferenca == 0:
        print('Parabéns você acertou!')
        break
    elif diferenca <= 5 and diferenca >= -5:
        print('Você errou, mas está quente!')
    elif diferenca > 0:
        print('Você errou, o número era maior!')
    else:
        print('Você errou, o número era menor!')
    tentativas = tentativas - 1
    
print('FIM DO PROGRAMA, O NÚMERO ERA: ', numero)