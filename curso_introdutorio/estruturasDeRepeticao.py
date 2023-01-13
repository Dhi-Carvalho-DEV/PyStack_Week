print('Estruturas de Repetições')

print('WHILE')

i = 0
while i < 10:
    print(i)
    i += 1

aluno = 'S'
while aluno != 'N':
    nome = input('Digite o nome do aluno: ')
    media = float(input('Digite a média de ' + nome + ': '))

    if media >= 6:
        print(f'O {nome} foi aprovado.')
    else:
        print(f'O {nome} foi reprovado')

    aluno = input('Gostaria de inserir mais alunos? S ou N: ')

print('FOR')

