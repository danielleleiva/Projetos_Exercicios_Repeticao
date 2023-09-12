repetir = "s"
resultado = 1
fat = 1

while repetir != "n":
    
    fat = int(input("Digite o número que deseja fatorar:\n"))
    
    for n in range (1, fat + 1):
        resultado = resultado * n
        
    print(f"O resultado da fatoração do número {fat} é: {resultado}\n")
    resultado = 1
    repetir = input("Deseja fatorar outro valor: (n) ou (s)?\n")

        
