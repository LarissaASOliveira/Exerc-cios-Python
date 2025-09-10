

class Carro:

    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está acelerando.")

    def frear(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está freando.")

carro1 = Carro("Toyota", "Corolla", "branco", "2018")
carro2 = Carro("Honda", "Civic", "preto","2000")

carro1.acelerar() 
carro1.frear()
carro2.acelerar() 
carro2.frear()