# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

alunos_aprovados = 0

for i in range(5): 
    nota = float(input(f"Digite a nota do aluno{i + 1}: "))

    if nota >= 7:
        alunos_aprovados += 1

    print(f"Total dos alunos aprovados: {alunos_aprovados}")

    