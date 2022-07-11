"""
Considerando a tabela abaixo.

total de eleitores = 1000
validos = 800
brancos = 150
nulos = 50

Faça uma classe com 3 métodos que calculam....
⚫ percentual do votos válidos em relação ao total de eleitores,
⚫ percentual de branco em relação ao total de eleitores
⚫ percentual de nulos em relação ao total de eleitores

Dica: relação ao total significa que você deve dividir, por exemplo 
"nulos pelo total de etores, validos pelo total de eleitores, etc...

Utilize programação orientada a objetos"""

class Votes:
    def __init__(self, nulos, brancos, validos):
        self.nulos = 50
        self.brancos = 150
        self.validos = 800
    
    def totalvotos(self):
        return self.nulos + self.validos + self.brancos
    
    def nulos(self):
        return (self.nulos / self.total) * 100

    def validos(self):
        return (self.validos / self.total) * 100

    def brancos(self):
        return (self.brancos / self.total) * 100

    # def calcula(self):
    #     # total_eleitores = nulos + validos + brancos 
    #     return 100 * self.valor / 1000 * 0.01
percent = Votes().nulos() 

print(f"Percentual de votos brancos = {percent:.2%}")
