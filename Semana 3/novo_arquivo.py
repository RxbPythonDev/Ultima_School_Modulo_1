def fatorial(numero):
    print('Chamada com parâmetro ', numero)
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)

#principal => fatorial(3) - 3 * ()
#fatorial(2) - 3 * 2 *
#fatorial(1) - 3 * 2 * 1

retorno = fatorial(3)

print(retorno)