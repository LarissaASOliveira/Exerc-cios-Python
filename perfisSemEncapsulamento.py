# Classe sem encapsulamento

class Perfil:
    def __init__(self):
        self.curtidas = 0  # atributo público

    def curtir(self):
        self.curtidas += 1

# Testando no console
perfil = Perfil()
perfil.curtir()   # curtidas = 1
perfil.curtir()   # curtidas = 2
print(perfil.curtidas)  # saída: 2

# Burlando a regra:
perfil.curtidas = 1000  # alterando diretamente
print(perfil.curtidas)  # saída: 1000
