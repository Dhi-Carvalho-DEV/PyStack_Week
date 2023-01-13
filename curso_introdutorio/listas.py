print('LISTAS')

notas = [10, 8, 9, 2, 1]

print(notas[2])


qtd_alunos = int(input('Digite a quantidade de alunos: '))
notas_dos_alunos = []

for i in range(0, qtd_alunos):
    nota = float(input('Digite uma nota: '))
    notas_dos_alunos.append(nota)

soma = 0
quantidade_notas = 0
for i in notas_dos_alunos:
    soma = soma + i
    quantidade_notas = quantidade_notas + 1

media = soma / quantidade_notas

print(soma)
print(quantidade_notas)
print(media)