"""#VERSÃO SIMPLES
clientes = []
for i in range(5):
    nome = input()
    cpf = input()
    idade = int(input())
    cliente = {"Nome": nome, "CPF": cpf, "Idade": idade}
    clientes.append(cliente)

for cliente in clientes:
    print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])"""

#VERSÃO COM CLASSES
class Cliente:
    def __init__(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None
    
    def cadastro(self):
        self.nome = input()
        self.cpf = input()
        self.idade = int(input())
    
    def mostrar_informacoes(self):
        print("Cliente:", self.nome, "CPF:", self.cpf, "Idade:", self.idade)

clientes = []
for i in range(2):
    cliente = Cliente()
    cliente.cadastro()
    clientes.append(cliente)

for cliente in clientes:
    cliente.mostrar_informacoes()