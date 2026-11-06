print("Uczymy się języka Python!")

user_age = 18
user_city = "Warszawa"
height = 1.82  # 18.2 * 0.1, 0.182 * 10
is_student = False  # True
result = None

wartosc = 10
print(wartosc + 20)
wartosc = "Dziesięć"

wiek = 23
print(f"Twój wiek to {wiek:6}")

waga = 87.45
print(f"Twoja waga to {waga:.1f}")

# Operatory arytmetyczne

x, y = 10, 20
w1 = x + y
w2 = x - y
w3 = x * y
print(f"{x} + {y} = {w1:5}")
print(f"{x} - {y} = {w2:5}")
print(f"{x} * {y} = {w3:5}")

a, b = 10, 20
print(f"a = {a}, b = {b}")
a, b = b, a
print(f"{a = }, {b = }")

print("Język programowania Python", end=" | ")
print("Poznajemy zmienne")

print("Wartość w zmiennej a wynosi", a, ", a wartość w zmiennej b wynosi", b)
print("Wartość w zmiennej a wynosi", a, ", a wartość w zmiennej b wynosi", b, sep="-")

# Zamiana typów
liczba1 = int("13")
liczba2 = 10
liczba3 = liczba1 + liczba2
print(f"{liczba1} + {liczba2} = {liczba3}")
print(type(liczba1))
liczba4 = "23"
print(type(liczba4))
liczba5 = "23.45"
liczba6 = float(liczba5)
print(liczba6 + 10)


c, d = 10, 20

# Zwiększasz wartość w zmiennej c o 5
c = c + 5
print(f"{c = }")
c += 5
print(f"{c = }")
c = c - 5
print(f"{c = }")
c -= 5
print(f"{c = }")
d = d * 2
print(f"{d = }")
d *= 2
print(f"{d = }")