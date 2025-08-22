#int representa numeros inteiros.
#input para inserir a mensagem.

distancia = int(input("digite a sua distância percorrida em km: "))

#float numeros quebrados.

combustivel = float(input("digite o total de combustível gasto em litros: "))

consumo = distancia / combustivel
print(f"{consumo:.3f}")

#print inserir a mensagem na tela.
#O f é uma string, permite que você insira valores de variáveis ou resultados de expressões diretamente na string, usando chaves {} para delimitá-las.