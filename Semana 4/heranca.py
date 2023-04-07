class Animal:
    def __init__(self, especie, n_patas):
        self.especie = especie
        self.n_patas = n_patas
    
    def mostra_dados(self):
        print(f"O {self.especie} tem {self.n_patas} patas.")

class Gato (Animal):
    def __init__(self):
        super().__init__(n_patas = 2, especie = "Gato")

class Cachorro (Animal):
    def __init__(self):
        super().__init__(n_patas = 4, especie = "Cachorro")

gato = Gato()
gato.mostra_dados()

cachorro = Cachorro()
cachorro.mostra_dados()

