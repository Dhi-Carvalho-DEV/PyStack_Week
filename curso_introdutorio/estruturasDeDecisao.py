print('Estrutura de Decisão')

nota_aluno = float(input('Digite a nota do aluno: '))

if nota_aluno >= 6:
    print(nota_aluno)
    print('O aluno foi aprovado')
else:
    print(nota_aluno)
    print('O aluno está reprovado')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(media)
    print('O aluno foi aprovado')
elif media >= 4:
    print(media)
    print('O aluno está em recuperação')
else:
    print(media)
    print('O aluno está reprovado')
