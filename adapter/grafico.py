import sympy as sp
import matplotlib.pyplot as plt


def plotar_grafico(equacao, tipo, solucoes):
    x = sp.symbols('x')
    try:
        lhs, rhs = equacao.split('=')
        expr = sp.sympify(lhs) - sp.sympify(rhs)
        func = sp.lambdify(x, expr, 'numpy')

        import numpy as np
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label='f(x) = ' + str(expr))
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, which='both')

        if tipo == 'linear' and solucoes:
            plt.plot(solucoes, [0], 'ro', label=f'Solução x = {solucoes}')
        elif tipo == 'quadratica' and solucoes:
            for sol in solucoes:
                plt.plot(sol, 0, 'ro', label=f'Solução x = {sol}' if solucoes.index(sol) == 0 else "")

        plt.title('Gráfico da Equação')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.show()
    except Exception as e:
        print("Erro ao plotar o gráfico:", e)
