#Indices:    0         1        2          3
"""nomes = ["Junior", "Wyllon", "Kamilla", "Carlos"]
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])"""


#Indices:    0         1        2          3      
#nomes = ["Junior", "Wyllon", "Kamilla", "Carlos"]
#len() -> length -> Tamanho/Comprimento

#tam = len(nomes)
#for indice in range(tam):
#    print(indice, nomes[indice])

#for indice,valor in enumerate(["Junior", "Wyllon", "Kamilla", "Carlos"]):
#    print(indice,valor)

"""nomes = [] #Armazene as informações dos clientes
for i in range(2):
    nome = input("Digite o seu nome: ")
    nomes.append(nome)
    print(nomes, len(nomes))"""

#LISTAS (Alteração)
#nomes = ['Sherlon', 'Danyel', 'Kamilla', 'Wyllon', 'Igor']
#print(nomes)
#nomes[0] = "Rafael"
#print(nomes)

#TUPLAS (Imutáveis)
#nomes = ('Sherlon', 'Danyel', 'Kamilla', 'Wyllon', 'Igor')
#print(nomes)
#nomes[0] = "Rafael"
#print(nomes)

#DICIONARIOS {chave: valor}
"""cliente = {"Nome": "Sherlon", "Idade": 27, "Senha": "senha123"}

senha_digitada = "lalala"
if cliente["Senha"] == senha_digitada:
    print("Login realizado")
else:
    print("Senha inválida")
    cliente["Senha"] = input("Digite a nova senha: ")
print(cliente)"""

"""cliente = {"Nome": "Sherlon", "Idade": 27, "Senha": "senha123"}
print(cliente.keys())
print(cliente.values())
print(cliente.items())"""


"""def exemplo(cliente):
    print(cliente, type(cliente))

cliente = [1,5,8,9,6,8,5]
exemplo(cliente)"""

class Cliente:
    def __init__(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None
    
    def cadastro(self):
        self.nome  = input("Digite o nome: ")
        self.cpf   = input("Digite o CPF: ")
        self.idade = int(input("Digite o idade: "))
    
    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Idade:", self.idade)

clientes = []
for i in range(2):
    cliente = Cliente()
    cliente.cadastro()
    cliente.mostrar_dados()
    clientes.append(cliente)

    
