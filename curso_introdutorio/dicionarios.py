pessoas = {'nome': 'Diogo', 'idade': '37'}

print(pessoas)
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('=============')

for valores in pessoas.values():
    print(valores)

print('=============')

for valores in pessoas.items():
    print(valores)

print('=============')

for chave, valor in pessoas.items():
    print(chave)
    print(valor)
    print(chave, valor)
