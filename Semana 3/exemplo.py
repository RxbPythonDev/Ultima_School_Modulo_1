"""def minha_primeira_funcao():
    nome = "Sherlon"
    print("2)", nome)

nome = "Samuel"
print("1)", nome)
minha_primeira_funcao()
print("3)", nome)"""

#SEM RETURN
"""def soma(x, y):
    resultado = x + y
    print(resultado)

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
soma(x, y)"""

#COM RETURN
"""def soma(x, y):
    resultado = x + y
    return resultado

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
saida = soma(x, y)
print(f"A soma foi: {saida}")"""

"""def media(x, y, z):
    resultado = (x + y + z) / 3 
    return resultado

for i in range(3):
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    z = int(input("Digite o valor de z: "))
    saida = media(x, y, z)
    print(f"A soma foi: {saida}")"""

"""Descrição: retorna se uma pessoa é Adulto ou Adolescente/Criança dada uma Idade."""
"""def maior_de_idade(idade):
    if idade >= 18:
        return "Adulto"
    else:
        return "Adolescente/Criança"

saida = maior_de_idade(15)
print(saida)"""

"""for repeticao in range(4):
    #Realiza o cadastro de um usuário
    cadastro_usuario()
print("Programa finalizado!")"""

"""def cadastro_usuario():
    nome = input("Digite o seu nome: ")
    cpf =  input("Digite o seu cpf: ")
    idade = int(input("Digite a sua idade: "))
    print("Nome:", nome, "CPF:", cpf, "Idade:", idade)
    return nome, cpf, idade

def maior_de_idade(idade):
    if idade >= 18:
        return "Adulto"
    else:
        return "Adolescente/Criança"

while True:
    print("------------------ OPCOES -------------------")
    print("1) Cadastrar usuário, 2) Verificar idade, 3) Finalizar o programa:")
    opcao = int(input("O que você deseja?"))
    #Realiza o cadastro de um usuário
    if opcao == 1:
        nome, cpf, idade = cadastro_usuario()
        saida = maior_de_idade(idade)
        print(saida)

    #Finalizar o programa
    elif opcao == 3:
        print("Programa finalizado!")
        break
"""

"""def soma(*valores):
    total = 0
    for numero in valores:
        print(f"{total} + {numero} = {total + numero}")
        total += numero
    print(f"Total = {total}")
soma(5, 9, 7, 4)"""

"""import math
raiz = math.sqrt(16)
print(raiz)"""

"""import random
for i in range(5):
    numero = random.randint(0,6)
    print(numero)"""

"""pypi.org"""