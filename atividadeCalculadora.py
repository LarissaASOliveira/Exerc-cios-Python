# int é usado apenas para numeros inteiros.

num1 = int(input("digite o 1º número: "))
op = input("digite a operação matemática:(+ , - , / , *) ")
num2 = int(input("digite o 1º número: "))

if op == "+":
    resultadoSoma = num1 + num2
    print(f"O resultado é: {resultadoSoma}")

elif op == "-":
    resultadoSubtracao = num1 - num2
    print(f"O resultado é: {resultadoSubtracao}")

elif op == "/":
    resultadoDivisao = num1 / num2
    print(f"O resultado é: {resultadoDivisao}")

elif op == "*":
    resultadoMultiplicacao = num1 * num2
    print(f"O resultado é: {resultadoMultiplicacao}")

else:
    print("Resultado inválido")