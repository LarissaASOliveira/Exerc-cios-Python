# O While cria um laço infinito que executa continuamente até que uma instrução break seja encontrada ou uma interrupção externa ocorra.

while True:

        numero = int(input("Digite um número entre 0 e 10: "))
    

        if numero > 10:
            print(f"Número invalido {numero}")
  
        else:
            print("Número invalido. Tente novamente.") 
            break

# O break serve para interromper imediatamente a execução de um loop.