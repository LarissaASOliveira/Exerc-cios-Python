soma = 0

numero = int(input("digite o numero inteiro (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("digite o numero inteiro (0 para sair): "))
print(f"a soma dos numeros é: {soma}")