#colocando um valor na variavel
num = 1

#Pedindo ao usuario o valor que sera o limite do while
max = int(input(f"Digite um número inteiro maior que 1:\n"))

#Imprimindo mensagem
print(f"Números pares de 1 ao {max}:")

#loping para mostrar os numeros pares
while num <= max:
    
    if num %2==0:#Conta para encontrar o valor par
        print(num, end=", ")#"end ="" coloca um espaço entre as variaveis"

    num +=1 #Soma 1 na variavel num 