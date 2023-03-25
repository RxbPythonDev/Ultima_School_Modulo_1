from procedural import funcao_nomeada
#def meu_nome_func():
 #   var_controle = False
  #  meu_nome = input('Digite seu nome: ')
   # if meu_nome == "Adimir" or meu_nome == 'Aquiules':
    #    var_controle = True
    #print('Olá mundo, meu nome é: ', meu_nome)
    #return var_controle

#retorno = meu_nome_func()
#if retorno:
#    print('Nome válido')
#else:
#    print('Nome inválido')

def soma_dois_numeros(x, y):
    return x + y

def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero #soma += numero
    return soma

resultado_da_soma = soma_dois_numeros(1, 2)
resultado_da_soma = soma_dois_numeros(y=1, x=2)
print(resultado_da_soma)
soma_varios_num = soma_numeros(1,2,3,4,5)
print(soma_varios_num)

def descricao_livro(titulo, autor='Desconhecido'):
    print('O livro: {} autor: {}'.format(titulo, autor))

descricao_livro(autor="Antonio", titulo='O menino maluquinho')
descricao_livro(titulo='O menino maluquinho')

def descricao_livro2(**kwargs):
    for chave in kwargs:
        print(chave + ' : ' + kwargs[chave])

descricao_livro2(titulo='Menino maluquinho', autor='Antonio', resumo='Bla bla')