# Class = Palavra chave no python para definir uma classe.
# Carro = Nome que damos á classe. Por convenção começa com letra maiúscula se for nome composto, usamos Camel Case. EX: Minha Casa. 


class Carro:

#Def = palavra chave que define uma função ou métodos no python

#__int__ = Método construtor da classe. Ele é chamado automaticamente quando criamos a classe com um novo objeto. Serve para inicializar atributos do objeto.

#self = Uma referência ao próprio objeto que está sendo criando.

#print é usado para exibir as mensagem.

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} está a acelerando.")


# Criando dois objetos diferentes
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("Chevrolet", "Fiat")

# Chamados métodos
carro1.acelerar() # Usa os atributos do carro1
carro2.acelerar() # Usa os atributos do carro2
carro3.acelerar() # Usa os atributos do carro3