import sympy as sp
from prettytable import PrettyTable
from sympy import symbols, Eq, pi, asin, acos, atan, sqrt, exp

def fixed_point_iteration(g, x0, n):

  x = sp.Symbol('x')
  table = PrettyTable(['i', 'x'])
  for i in range(n):
    x1 = g.subs(x, x0)
    table.add_row([i+1, x1])
    x0 = x1
  print(table)
  return x1

# Enter the user's value
func_g = input("Enter the function g(x): ")
x0 = float(input("Enter the value x0: "))
n = int(input("Enter the interation n: "))

# Convert the expression to sympy
g = sp.sympify(func_g)

# Run the algorithm and print the solution
result = fixed_point_iteration(g, x0, n)
if result:
  print(f"The approximate solution of the equation is: {result}")
else:
  print("The method does not converge after {n} interation.")