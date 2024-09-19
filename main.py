from adapter.grafico import plotar_grafico
from usecase.identifica_equacoes import identificar_equacao
from usecase.resolve_equacoes import resolver_linear, resolver_quadratica


def main():
    print("Bem-vindo ao sistema de resolução de equações de 1º e 2º grau!")
    print("Por favor, insira sua equação no formato padrão, por exemplo:")
    print("Para 1º grau: 2*x + 3 = 7")
    print("Para 2º grau: 1*x^2 - 5*x + 6 = 0")

    equacao = input("\nDigite a sua equação: ")
    tipo = identificar_equacao(equacao)

    if tipo == 'linear':
        solucao = resolver_linear(equacao)
        plotar_grafico(equacao, tipo, solucao)
    elif tipo == 'quadratica':
        solucao = resolver_quadratica(equacao)
        plotar_grafico(equacao, tipo, solucao)
    else:
        print("Desculpe, não consegui identificar o tipo da equação. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
