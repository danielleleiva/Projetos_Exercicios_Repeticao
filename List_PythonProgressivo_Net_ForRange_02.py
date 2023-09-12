first = int(input("Digite o primeiro elemento da PA:\n"))
razao = int(input("Digite a razão da PA:\n"))
n = int(input("Quantos elementos você deseja exibir:\n"))

ult = first + (n-1) * razao
ult = ult + 1

for var in range(first, ult, razao):#(primeiro numero, ultimo numero, razao da lista)
    print(var)