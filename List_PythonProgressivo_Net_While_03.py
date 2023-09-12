usu = input("Insira o nome do usúario:\n")
senha = input("Insira a senha:\n")

while senha == usu:
    print("Usuario e senha devem ser diferentes, por favor tente novamente:")
    usu = input("Insira o nome do usúario:\n")
    senha = input("Insira a senha:\n")

print("Usúario e senha corretos, entrando no sistema!")

