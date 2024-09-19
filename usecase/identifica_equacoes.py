def identificar_equacao(equacao):

    equacao = equacao.replace(' ', '').lower()

    if 'x^2' in equacao or 'x²' in equacao:
        return 'quadratica'
    elif 'x' in equacao:
        return 'linear'
    else:
        return 'desconhecida'
