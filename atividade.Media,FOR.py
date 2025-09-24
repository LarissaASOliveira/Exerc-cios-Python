soma_notas = 0

# for i in range foi usado quando utiliza um numero especifico de sequencia. O in serve para especificar a sequência que o loop for irá percorrer, que neste caso é gerada pela função range(). O in conecta o for à sequência de números retornada por range(), e o i seria o contador.
for i in range(5):

    # Float é para usar tanto numeros inteiros quanto negativos ou positivos

    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma_notas += nota

media_notas = soma_notas / 5

#F e usando {chaves} para os conteúdos a serem substituídos ou formatados. Este método simplifica a criação de strings dinâmicas, tornando o código mais legível e eficiente para exibir números, datas, e combinar dados. 
print(f"A média das 5 notas é: {media_notas}")