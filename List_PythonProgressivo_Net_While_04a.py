#População A
popA = int(input("População do país A:\n"))
while popA <= 0:
    popA = int(input("População do país A deve ser maior que 0, digite novamente:\n"))
#Taxa de crecimento A
taxaA = float(input("Taxa de crescimento do país A(%):\n"))
while taxaA == 0:
    taxaA = float(input("A taxa deve ser diferente de 0, por favor digite novamente(%):\n"))

#População B
popB = int(input("População do país B:\n"))
while popB <=0:
    popB = int(input("População do país B deve ser maior que 0, digite novamente:\n"))
#Taxa de crescimento B
taxaB = float(input("Taxa de crescimento do país B(%):\n"))
while taxaB == 0:
    taxaB = float(input("A taxa deve ser diferente de 0, por favor digite novamente(%):\n"))

ano = 0
while popA < popB:
    popA = ((taxaA / 100)*popA) + (popA)
    popB = ((taxaB / 100)*popB) + (popB)
    ano += 1
    print(f"Ano: {ano}.")
    print(f"População A: {popA:.2f}.")
    print(f"População B: {popB:.2f}.")

print (f"A população A irá ultrapassar a população B no ano de {ano}")
