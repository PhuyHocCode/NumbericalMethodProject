import sympy as sp
from prettytable import PrettyTable
from sympy import symbols, Eq, pi, asin, acos, atan, sqrt, exp

def newton_method(func_str, x0, n, tol=1e-6):
   
    x = symbols('x')
    func = sp.sympify(func_str) 
    func_deriv = sp.diff(func, x) 

    table = PrettyTable(["Iteration (i)", "x_i", "f(x_i)", "f'(x_i)"])
    x_i = x0
    for i in range(n):
        f_i = func.subs(x, x_i).evalf()
        df_i = func_deriv.subs(x, x_i).evalf()

        table.add_row([i + 1, x_i, f_i, df_i])

        x_i_plus_1 = x_i - f_i / df_i

        if abs(x_i_plus_1 - x_i) < tol:
            print(table)
            print(f"Root found after {i + 1} iterations: {x_i_plus_1:.6f}")
            return x_i_plus_1, i + 1 

        x_i = x_i_plus_1

    print(table)
    print(f"The method did not converge after {n} iterations.")
    return None, n


if __name__ == "__main__":
    # Example usage:
    function_str = input("Enter the function (e.g., x**3 - 2*x - 5): ")
    initial_guess = float(input("Enter the initial guess (x0): "))
    max_iterations = int(input("Enter the maximum number of iterations: "))

    root, iterations = newton_method(function_str, initial_guess, max_iterations)