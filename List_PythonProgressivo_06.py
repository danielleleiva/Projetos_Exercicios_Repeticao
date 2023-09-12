alunos = int(input("Digite o número de alunos:\n"))
num = 1
soma = 0.0

while num <= alunos:
    
    nota = float(input("Qual a nota desse aluno:\n"))
    soma += nota
    num += 1

media_sala = (soma / alunos)
print(f"A média da turma é de:{media_sala:.2f}")
