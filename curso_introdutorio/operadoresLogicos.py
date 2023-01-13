print('Operadores Lógicos')

teste = True and True
print(teste)
teste = True and False
print(teste)
teste = False and False
print(teste)

teste = True or True
print(teste)
teste = True or False
print(teste)
teste = False or False
print(teste)

teste = not True
print(teste)
teste = not False
print(teste)

nota_aluno = float(input('Digite a nota do aluno: '))
nota_maxima_recuperacao = 4
media_escola = 6

teste = nota_aluno >= nota_maxima_recuperacao and nota_aluno < media_escola
print(teste)
