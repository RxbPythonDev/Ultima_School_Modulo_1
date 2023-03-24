#Introdução
"""#O comando input permite pegar informações do usuário para o programa
nome = input("Digite o seu nome: ")
#Mostra na tela informações desejadas
print("Olá", nome)"""

#Variáveis (Tipos)
"""nome  = "Sherlon" # str -> string
num_r = 3.14159   # float -> com vírgula
num_i = 5         # int -> integer
print(num_i, type(num_i) )"""

#Operadores Aritméticos (+ - / * ** %)
"""x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
print("Resultado:", x ** y )"""

#pi = 3.14159
#print("O valor de PI é", pi)
#print("O valor de PI é {}".format(pi))
#print(f"O valor de PI é {pi:.2f}")
"""x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)"""

#Operadores de Comparação (> < >= <= == !=)
"""print(5 > 2)  #True
print(3 < 1)  #False
print(6 <= 6) #True
print(6 >= 6) #True
print(6 == 4) #False
print(6 != 4) #True"""

"""senha = "minha_senha123"
tentativa = "minha_senha123"
print(senha == tentativa)"""

# Operadores Lógicos (AND OR NOT)
#AND -> "E": Retorna TRUE se TODAS as entradas são TRUE.
"""print(False and False)
print(False and True)
print(True and False)
print(True and True)"""

#OR -> "OU": Retorna TRUE se PELO MENOS UMA das entradas é TRUE.
"""print(False or False)
print(False or True)
print(True or False)
print(True or True)"""

#NOT -> "NÃO": Inverte a entra.
"""print(not False)
print(not True)"""

#Estruturas Condicionais (IF ELSE ELIF)
"""chovendo = True
gasolina = False
if chovendo:
    print("Ficar em casa!")
elif gasolina:
    print("Vou à praia!")
else:
    print("Abastecer o carro!")"""

"""idade = -15
if (idade > 0) and (idade < 13):
    print("Criança")
elif (idade >= 13) and (idade < 18):
    print("Adolescente")
elif (idade >= 18) and (idade < 65):
    print("Adulto")
elif (idade >= 65):
    print("Idoso")
else:
    print("Idade inválida!")"""

#Estruturas de Repetição (FOR WHILE)
"""inicio = 0
while inicio < 1000:
    print("Entrou no WHILE", inicio)
    inicio = inicio + 1"""

#Indice  012345678.....
"""nome =  "André Ferreira"
indice = 0
while indice < 8:
    print( nome[indice] )
    indice += 1"""

"""inicio = 0
fim = 3
incremento = 1
while inicio < fim:
    print(inicio)
    inicio += incremento"""

"""for x in range(10): #(inicio, fim, incremento):
    for y in range(10):
        print(f"Resultado {x} * {y}: {x*y}")"""


#moedas_1r = 19 * 1
#moedas_50 = 15 * 0.50
#moedas_25 = 30 * 0.25
#resultado = moedas_1r + moedas_50 + moedas_25
"""Falta implementar essa parte"""
#print(resultado)

"""horas = 80
valor_inicial = 1000.00
valor_da_hora = 20.45
taxa = 0.15
parcial = (valor_inicial + horas * valor_da_hora)
percentual = parcial * taxa
resultado = parcial + percentual
print(f"{resultado:.2f}")"""

"""horas = 80
valor_inicial = 1000.00
valor_da_hora = 20.45
taxa = 0.50
resultado = (valor_inicial + horas * valor_da_hora)  * (1 + taxa)
print(f"{resultado:.2f}")"""


nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']
for nome in nomes:
    print(f'Olá, {nome}! Seja bem vindo à nave Imperial dos Siths.')




