#float: é um tipo de dado que representa números de ponto flutuante, ou seja,casas decimais. float(input) = o programa pega o valor em texto e transforma em números decimais.
#Variavel: é um nome que se refere a um valor que pode ser armazenado. 
#Input: é uma função que permite receber dados diretamente do usuário durante a execução de um programa

nota1=float(input("digite a primeira nota"))
nota2=float(input("digite a segunda nota"))
nota3=float(input("digite a terceira nota"))     

#Calculo de divisão em python:  cálculo de divisão se refere à operação matemática que resulta na divisão de um número (dividendo) pelo outro (divisor). Python oferece dois tipos principais de divisão: divisão verdadeira (/) e divisão inteira (//). 
media=(nota1+nota2+nota3)/3

#print: é uma função embutida usada para exibir informações na saída padrão, geralmente o console ou terminal. 
print ("a media é: ", media)