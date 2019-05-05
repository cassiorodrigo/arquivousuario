import json
from random import randint
ident = randint(10000, 99999)
dicionario1 = {}
a = {ident: {}}
'''


def usuario(nome, sobrenome, dia, sexo):
    with open('teste.json','w') as f:
        dicionario1["Nome"] = nome
        dicionario1["Sobrenome"] = sobrenome
        dicionario1["Dia"] = dia
        dicionario1["Sexo"] = sexo
        a[ident] = dicionario1
        b.update(a)
        json.dump(b, f)
        print(a)
        return a

nome = str(input('Nome: '))
sobrenome = str(input('Sobrenome: '))
dia = str(input('Nascimento: '))
sexo = str(input('Sexo: '))

usuario(nome, sobrenome, dia, sexo)
'''

with open("usuario.json", "r") as f:
    usr = json.load(f)
    for keys, values in usr.items():
        print(keys, values)