import math

def task_if11 ():
    try:
        A = int(input("A = "))
        B = int(input("B = "))
    except:
        print("A and B must be integers")
    else:
        if A == B:
            A = 0
            B = 0
        else:
            A = max(A, B)
            B = A
        print (f"A = {A} and B = {B}")
task_if11 ()

def task_geom21():
    try:
        x = list(input("Enter x "))
        y = list(input("Enter y "))
        r = float(input("radius = "))
    except ValueError:
        print("Invalid input: Radius (r) must be a number.")
        return
    except Exception:
        print("Invalid input.")
        return
    else:
        xi = []
        for char in x:
            if char.isdigit():
                n = float(char)
                xi.append(n)
        yi = []
        for char in y:
            if char.isdigit():
                n = float(char)
                yi.append(n)
        i = list(zip(xi, yi))
        if len(xi) != len(yi):
            print("Error: The number of X and Y coordinates does not match.")
            return
        print(f"Entered points {i}")
        N = len(i)
        M = 0
        R_squared = r**2
        for x0, y0 in i:
            a = x0 >= 0
            b = y0 <= 0
            c = x0**2 + y0**2 <= R_squared
            if a and b and c:
                M += 1 
        print(f"Total number of points {N}")
        print(f"Number of points in the area {M}")
task_geom21()

def task_series23(E):
    S = 0.0
    n = 1
    product_num = 10.0 
    denominator = math.factorial(4 * n + 3)
    u_n = product_num / denominator
    S += u_n
    current_u = u_n
    
    print(f"Початок обчислення, умова зупинки |u_n| < {E}")
    n += 1
    while abs(current_u) >= E:
        next_factor = 7 + 3 * (n - 1)
        product_num *= next_factor
        denominator = math.factorial(4 * n + 3)
        u_n = product_num / denominator
        current_u = u_n
        S += u_n
        if n > 50:
             print("\nПопередження: Досягнуто максимальної кількості ітерацій.")
             print(f"Кількість ітерацій (N): {n}")
             return S
        n += 1
    print(f"\nКількість ітерацій (N): {n-2}") # Віднімаємо 2, оскільки n збільшилось після останнього члена
    print(f"Останній доданий член |u_n|: {abs(current_u):.20f}")
    return S
Epsilon = 1e-8
Sum_S = task_series23(Epsilon)
print(f"Фінальна сума S при E={Epsilon}: S ≈ {Sum_S:.15f}")
