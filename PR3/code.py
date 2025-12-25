import numpy as np

def Proc_11():
    try:
        A = float(input("Enter A "))
        B = float(input("Enter B "))
        C = float(input("Enter C "))
        D = float(input("Enter D "))
    except:
        return
    else:
        A = min(A, B)
        B = max(A, B)
        C = min(C, D)
        D = max(C, D)
        A = min(A, C)
        C = max(A, C)
        B = min(B, D)
        D = max(B, D)
        print(A)
        print(D)

def Matrix_1():
    try:
        M = int(input("Enter M "))
        K = int(input("Enter K "))
        N = int(input("Enter N "))
        if K < 1 or K > M:
            print(f"Error: K must be between 1 and {M}.")
            return
    except:
        return
    else:
        print("\n--- Generating Matrix A ---")
        A = np.random.randint(low=1, high=10, size=(M, N))
        print("Matrix A:")
        print(A)
        row_index = K - 1
        k_row = A[row_index, :]
        sum_k_row = np.sum(k_row)
        product_k_row = np.prod(k_row)
        print("\n--- Results for K-th Row ---")
        print(f"K-th Row ({K}): {k_row}")
        print(f"Sum of elements in K-th row: {sum_k_row}")
        print(f"Product of elements in K-th row: {product_k_row}")
    if M == N:
        I = np.eye(M, N)
        print("\n--- Identity Matrix Operations ---")
        print("Identity Matrix I:")
        print(I)
        D = A - I
        print("\nResult of Matrix Difference (D = A - I):")
        print(D)
    else:
        print("\nCannot calculate difference with the Identity Matrix (I) because Matrix A is not square (M != N).")

def start():
    print("Choose a task")
    print("1 - task num1 - Proc_11")
    print("2 - task num2 - Matrix_1")
    try:
        num = int(input("Task number: "))
        if num > 2:
            print("Error: Please enter a valid integer task number (1 or 2).")
            return
    except:
        return
    else:
        if num == 1:
            Proc_11()
        else:
            Matrix_1()
start()
