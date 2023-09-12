numero = int(input("Fatorial de:\n"))

resultado = 1


for n in range(1, numero+1):
    resultado *= n #Resultado = resultado * n
    print(resultado)
print(f"Resultado da fatoração do número {numero}, é:{resultado}")
