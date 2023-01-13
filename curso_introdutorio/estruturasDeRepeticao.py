print('Estruturas de Repetições')

print('WHILE')

i = 0
while i < 10:
    print(i)
    i += 1

aluno = 'S'
while aluno != 'N':
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota de ' + nome + ': '))
    nota2 = float(input('Digite a primeira nota de ' + nome + ': '))

    media = (nota1 + nota2) / 2

    if media >= 6:
        print(f'O {nome} foi aprovado.')
    else:
        print(f'O {nome} foi reprovado')

    aluno = input('Gostaria de inserir mais alunos? S ou N: ')

print('FOR')

for i in range(0, 10):
    print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(f'O número {i} é par')
    else:
        print(f'O número {i} é ímpar')

for i in range(1, 11):
    print(f'======Tabuada do {i}======')
    for j in range(1, 11):
        print(f'{i} X {j} == {i*j}')

tabuada = int(input('Digite a tabuada desejada: '))
for i in range(1, 11):
    print(f'{tabuada} X {i} == {i*tabuada}')
