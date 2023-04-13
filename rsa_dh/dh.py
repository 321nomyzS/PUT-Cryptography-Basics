class DH:
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def calculate_A_B(self, a, b):
        A = pow(self.g, a, self.p)
        B = pow(self.g, b, self.p)
        return A, B

    def calculate_S(self, a, b):
        s = pow(b, a, self.p)
        return s


# Define constants
P = 23
G = 5
a = 6
b = 15

dh = DH(P, G)
print(f"A i B uzgadniają liczbę pierwszą p={P} i podstawę g={G}")

A, B = dh.calculate_A_B(a, b)
print(f"A wybiera tajną liczbę całkowitą a={a} i wysyła B A={A}")
print(f"B wybiera tajną liczbę całkowitą b={b} i wysyła B={B}")

sA = dh.calculate_S(a, b)
sB = dh.calculate_S(b, a)
print(f"A oblicza s={sA}")
print(f"B oblicza s={sB}")


