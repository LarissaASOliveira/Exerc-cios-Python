cargo = input("digite qual é o seu cargo(gerente, analistico, estágiario): ").lower().strip()
dia = input("digite o dia da semana: ").lower().split()

dias_uteis = ["segunda", "terça", "quarta", "quinta", "sexta"]

if cargo == "gerente":
    print("Acesso permitido.")

elif cargo in "analistico, estágiario" and dia in dias_uteis:
    print("Acesso permitido.")

else:
    print("Acesso negado.")
