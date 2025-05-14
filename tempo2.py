def converte_em_minutos(horas, minutos):
    """
    Converte um horário dado em horas e minutos para o total de minutos.

    Args:
        horas (int): quantidade de horas
        minutos (int): quantidade de minutos

    Returns:
        int: total de minutos
    """
    return horas * 60 + minutos
def converte_em_horas(minutos):
    """
    Converte um total de minutos para o formato de horas e minutos.

    Args:
        minutos (int): total de minutos

    Returns:
        tuple: (horas, minutos)
    """
    horas = minutos // 60
    minutos = minutos % 60
    return (horas, minutos)
if __name__ == "__main__":
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    print(f"Total em minutos: {converte_em_minutos(horas, minutos)}")
    horas2 = int(input("Digite a segunda quantidade de horas: "))
    minutos2 = int(input("Digite a segunda quantidade de minutos: "))
    total_minutos1 = converte_em_minutos(horas, minutos)
    total_minutos2 = converte_em_minutos(horas2, minutos2)
    diferenca = abs(total_minutos1 - total_minutos2)
    print(f"A diferença entre os dois horários é de {diferenca} minutos.")