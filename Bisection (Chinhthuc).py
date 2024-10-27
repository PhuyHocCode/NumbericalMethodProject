import sympy as sp
from prettytable import PrettyTable
from sympy import symbols, Eq, pi, asin, acos, atan, sqrt, exp

def bisection_method():
    # Taking user inputs for the function, interval, and number of iterations
    func_input = input("Enter the function f(x) (For example, x**2 - 4, 2*x*cos(2*x): ")
    a = float(input("Enter the lower boundary (a): "))
    b = float(input("Enter the upper boundary (b): "))
    n = int(input("Enter the number of iterations (n): "))

    # Define the symbol x for sympy
    x = sp.Symbol('x')

    # Parse the user-inputted function using sympy
    func = sp.sympify(func_input)

    # Function to evaluate the sympy expression at a given value
    def f(val):
        return float(func.subs(x, val))

    # Ensure that f(a) and f(b) have opposite signs, otherwise no root
    if f(a) * f(b) >= 0:
        print("No root found in the interval. f(a) and f(b) should have opposite signs.")
        return

    # Create a list to store iteration data
    iteration_data = []

    # Perform bisection for 'n' iterations
    for iteration in range(n):
        p = (a + b) / 2  # Midpoint

        if f(a) * f(p) < 0:
            b = p  # Root lies in the left half
        elif f(b) * f(p) < 0:
            a = p  # Root lies in the right half
        else:
            print("Something went wrong.")
            return

        # Append iteration data to the list
        iteration_data.append([iteration, a, b, p, f(p)])

    # Output the results
    print(f"The result after {n} iterations:")
    print(f"The lower boundary (a) is {a}, and the upper boundary (b) is {b}")
    print(f"The new mid-point value (p) is {(a + b)/2}")

    # Print iteration data in table format
    headers = ["Iteration", "a", "b", "p", "f(p)"]
    table = PrettyTable()
    table.field_names = headers
    table.add_rows(iteration_data)
    print(table)

# Run the function
bisection_method()