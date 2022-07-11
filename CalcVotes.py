"""
Considerando a tabela abaixo.

total de eleitores = 1000
validos = 800
votos brancos 150
nulos = 50

Faça uma classe com 3 métodos que calculam....
⚫ percentual do votos válidos em relação ao total de eleitores,
⚫ percentual de branco em relação ao total de eleitores
⚫ o percentual de nulos em relação ao total de eleitores

Dica: relação ao total significa que você deve dividir, por exemplo 
"nulos pelo total de etores, validos pelo total de eleitores, etc...

Utilize programação orientada a objetos"""

class Votes:
    def __init__(self, valor):
        self.valor = valor
    def

    def calcula(self):
         
        return 100 * self.valor / 1000 * 0.01

percent = Votes(150).calcula() 
print(f"{percent:.2%}")
