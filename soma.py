def adicao(a, b):
    return a + b    
if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    print('A soma de {} e {} é: {}'.format(valor1, valor2, adicao(valor1, valor2)))