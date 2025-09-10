'''
O que é Polimorfisio?

É quando um mesmo método tem compotamento diferentes dependendo da classe que o usa.

Pensa assim:

Todas as classes têm o método apresenta(),

Mas cada classe fala de um jeito próprio quando você chama esse método.
''' 

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}.")

class Cliente(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamento diferente.
        print(f"Sou cliente {self.nome}, vim comprar algo.")

class Aluno(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamentos diferentes.
        print(f"Sou aluno {self.nome}, estou estudando.")

# Criando objetos

p = Pessoa("Carlos")
c = Cliente("Maria")
a = Aluno("João")

# Chamando o MESMO método "apresentar".

p.apresentar()
c.apresentar()
a.apresentar()