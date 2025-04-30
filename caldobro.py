def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro
if __name__ == '__main__':
    valor = int(input('Digite um valor: '))
    print('O dobro de {} é: {}'.format(valor, calcula_dobro(valor)))