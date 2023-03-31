def soma(*valores):
    total = 0
    for numero in valores:
        print(f"{total} + {numero} = {total + numero}")
        total += numero
    print(f"Total = {total}")

def cadastro_usuario():
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