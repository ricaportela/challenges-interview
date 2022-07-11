class Votes:
     def __init__(self, valor):
         self.valor = valor

     def calcula(self):
         
         return 100 * self.valor / 1000 * 0.01

percent = Votes(150).calcula() 
print(f"{percent:.2%}")
