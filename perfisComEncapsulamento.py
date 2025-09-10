# Classe com Encapsulamento

class Perfil:
    def __init__(self):
        self.__curtidas = 0  # atributo privado

    def curtir(self):
        self.__curtidas += 1  

    def obter_curtidas(self):
         return self.__curtidas
    
# Testando no console
perfil = Perfil()
perfil.curtir()   # curtidas = 1
perfil.curtir()   # curtidas = 2
print(perfil.curtidas)  # saída: 2

# Burlando a regra:
perfil.curtidas = 1000  # alterando diretamente
print(perfil.curtidas)  # saída: 1000