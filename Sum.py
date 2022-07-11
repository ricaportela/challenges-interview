def calc(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
           
           
    print(f'Os multiplos entre {number} sao {result}')

    return sum(result)

number = int(input('Digite o numero: '))
res = calc(number)
print(f'A soma é = {res:.0f}')