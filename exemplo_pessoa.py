from exemplo_carro2 import Carro #importando a classe Carro.


class Pessoa:

    def __init__(self, nome, idade, cidade, exemplo_carro2:Carro):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.exemplo_carro2 = exemplo_carro2

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} tenho {self.idade} moro em {self.cidade}")

    def dirigir(self):
        print(f"{self.nome} estou dirigindo {self.exemplo_carro2.marca} modelo {self.exemplo_carro2.modelo} {self.exemplo_carro2.cor} {self.exemplo_carro2.ano}.")
        self.exemplo_carro2.acelerar()

meu_carro = Carro("honda", "Civic Type r", "preto", "2024")

#Criando uma pessoa que possui o carro.
pessoa1 = Pessoa("Cristina", 30, "pindamonhangaba", meu_carro)


pessoa1.apresentar() 
pessoa1.dirigir()
