nome = input('Digite o seu nome: ')

print('Olá, mundo!')
print(f'Olá, {nome}, tudo bem?')

idade = int(input('Digite sua idade: '))
print(f'Tenho {idade} anos')

print('Operadores Aritméticos')

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
exponenciacao = numero1 ** numero2
divisao = numero1 / numero2
divisaointeira = numero1 // numero2
resto = numero1 % numero2

print(f'{soma}')
print(f'{subtracao}')
print(f'{multiplicacao}')
print(f'{exponenciacao}')
print(f'{divisao}')
print(f'{divisaointeira}')
print(f'{resto}')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'{media}')

print('Operadores Relacionais')

teste = numero1 == numero2
print(teste)
teste = numero1 < numero2
print(teste)
teste = numero1 > numero2
print(teste)
teste = numero1 <= numero2
print(teste)
teste = numero1 >= numero2
print(teste)
teste = numero1 != numero2
print(teste)

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

nota_aluno = media
nota_maxima_recuperacao = 4
media_escola = 6

teste = nota_aluno >= nota_maxima_recuperacao and nota_aluno < media_escola
print(teste)

if nota_aluno >= 6:
    print(nota_aluno)
    print('O aluno foi aprovado')
else:
    print(nota_aluno)
    print('O aluno está reprovado')

if media >= 6:
    print(media)
    print('O aluno foi aprovado')
elif media >= 4:
    print(media)
    print('O aluno está em recuperação')
else:
    print(media)
    print('O aluno está reprovado')
