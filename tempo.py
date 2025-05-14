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
    total_minutos = int(input("Digite o total de minutos: "))
    print(f"Total em horas e minutos: {converte_em_horas(total_minutos)}")