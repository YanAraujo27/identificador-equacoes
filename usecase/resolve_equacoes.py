import sympy as sp

def resolver_linear(equacao):
    print("\nResolvendo uma equação de primeiro grau:")
    x = sp.symbols('x')
    try:
        lhs, rhs = equacao.split('=')
        expr = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        solucao = sp.solve(expr, x)
        print(f"Passo 1: Transpor todos os termos para um lado da equação:\n\t{expr.lhs} - {expr.rhs} = 0")
        print(f"Passo 2: Simplificar:\n\t{sp.Eq(expr.lhs - expr.rhs, 0)}")
        print(f"Passo 3: Resolver para x:\n\tx = {solucao[0]}")
        return solucao[0]
    except Exception as e:
        print("Erro ao resolver a equação linear:", e)
        return None


def resolver_quadratica(equacao):
    print("\nResolvendo uma equação de segundo grau:")
    x = sp.symbols('x')
    try:
        lhs, rhs = equacao.split('=')
        expr = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        solucao = sp.solve(expr, x)
        print(f"Passo 1: Escrever a equação na forma padrão ax² + bx + c = 0:\n\t{expr.lhs} - {expr.rhs} = 0")
        print(f"Passo 2: Identificar os coeficientes a, b e c:")
        a = expr.lhs.as_poly(x).coeffs()[0]
        b = expr.lhs.as_poly(x).coeffs()[1] if len(expr.lhs.as_poly(x).coeffs()) > 1 else 0
        c = expr.lhs.as_poly(x).coeffs()[2] if len(expr.lhs.as_poly(x).coeffs()) > 2 else 0
        print(f"\ta = {a},\n\tb = {b},\n\tc = {c}")
        print("Passo 3: Calcular o discriminante (delta):")
        delta = b ** 2 - 4 * a * c
        print(f"\tdelta = b² - 4ac = {b}² - 4*{a}*{c} = {delta}")
        if delta > 0:
            print("Passo 4: Calcular as duas raízes reais:")
            raiz1 = (-b + sp.sqrt(delta)) / (2 * a)
            raiz2 = (-b - sp.sqrt(delta)) / (2 * a)
            print(f"\tx₁ = (-b + √delta) / (2a) = ({-b} + √{delta}) / (2*{a}) = {raiz1}")
            print(f"\tx₂ = (-b - √delta) / (2a) = ({-b} - √{delta}) / (2*{a}) = {raiz2}")
            return [raiz1, raiz2]
        elif delta == 0:
            print("Passo 4: Calcular a única raiz real (raiz dupla):")
            raiz = -b / (2 * a)
            print(f"\tx = {raiz}")
            return [raiz]
        else:
            print("A equação não possui raízes reais.")
            return []
    except Exception as e:
        print("Erro ao resolver a equação quadrática:", e)
        return None
