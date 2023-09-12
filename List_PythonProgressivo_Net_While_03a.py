nome = input("Digite o seu nome?(Mínimo de 3 caracteres):\n")
idade = int(input("Digite a sua idade:\n"))
salario = float(input("Digite seu sálario:\n"))
sexo = input("Digite seu sexo: (f) para feminino e (m) para masculino:\n")
estado_civil = input("Informe seu estado civil 's','c','v','d':\n")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais de 3 caracteres, digite novamente:\n")

while idade <= 0 or idade > 150:
    idade = int(input("Sua idade deve ser entre 0 e 150 anos, digite sua idade novamente:\n"))

while salario <=0:
    salario = float(input("Seu salário deve ser maior que o valor 0, digite novamente:\n"))

while sexo != 'f' and sexo != 'm':
    sexo = input("Erro nos dados, favor informar seu sexo novamente 'f' ou 'm':\n")
    
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("Erro na digitação, por favor informe seu estado civil novamente, 's', 'c', 'v' ou 'd':\n")

print(f"Os dados digitados foram:\nNOME: {nome}\nIDADE: {idade}\nSALÁRIO: R${salario:.2f}\nSEXO: {sexo}\nESTADO CIVIL: {estado_civil}.")