a = 11
b = 12

print(a > 10)  # True
print(a == 11)  # True
print(a != 12)  # True
print(a > 0 and a < 15)  # True
print(a < 0 or a > 10)  # True
print(not (a > 10))   # False

c = 37
print(20 <= c <= 40)
print(not (20 <= c <= 40))

# Leniwe obliczanie
d = 5
print(d != 0 and 10 / d > 1)

# Instrukcja if ... else

e, f = 3, 25

# Jeżeli zachodzi warunek logiczny, wykonaj instrukcje
# które zapiszesz poniżej "we wcięciu"
# Jeżeli warunek nie jest prawdziwy, wtedy pomijasz ten
# fragment kodu
if e >= f:
    g = e + f
    print(f"Wersja 1 - Dodawanie: {g = }")

# Jeżeli warunek zachodzi, wtedy wykonaj to, co pod if.
# Jeżeli warunek nie zachodzi, wtedy wykonaj to co pod else.
if e >= f:
    g = e + f
    print(f"Wersja 2 - Dodawanie: {g = }")
else:
    g = e * f
    print(f"Wersja 2 - Mnożenie: {g = }")


# Kiedy chcesz sprawdzać wiele warunków, które są rozłączne
# Oznacza to, że jeśli zachodzi jeden warunek, to inne już nie zachodzą.
# Klasyczny przykład to sprawdzanie, do jakiego przedziału należy liczba.
# Przedział 1 - [1, 10]
# Przedział 2 - (10, 25)
# Przedział 3 - [25, 33)
# Przedział 4 - [33, 48]

h = 15

# 4 osobne if - każdy z nich jest sprawdzany osobno
# if 1 <= h <= 10:
#     print(f"Liczba {h} w przedziale 1")
# if 10 < h < 25:
#     print(f"Liczba {h} w przedziale 2")
# if 25 <= h < 33:
#     print(f"Liczba {h} w przedziale 3")
# if 33 <= h <= 48:
#     print(f"Liczba {h} w przedziale 4")

# Kiedy masz warunki rozłączne, wtedy lepiej sprawdzać je za pomocą if ... elif ... else
if 1 <= h <= 10:
    print(f"Liczba {h} w przedziale 1")
elif 10 < h < 25:
    print(f"Liczba {h} w przedziale 2")
elif 25 <= h < 33:
    print(f"Liczba {h} w przedziale 3")
elif 33 <= h <= 48:
    print(f"Liczba {h} w przedziale 4")
else:
    print("Liczba nie należy do żadnego z przedziałów")


# Wyrażenie warunkowe
i, j = 12, 40
print(i * j if i < j else i + j)
k = i * j if i < j else i + j
print(k)


# Instrukcja match

opcja = 31

match opcja:
    case 1:
        print("Opcja 1 - dodawanie")
    case 2 | 3:
        print("Opcja 2 - mnożenie lub dzielenie")
    case 6:
        print("Koniec")
    case _:
        print("Nie ma takiej opcji")


m, n, o = 12, 34, 25

najmniejsza = min(m, n, o)
print(najmniejsza)

najwieksza = max(m, n, o)
print(najwieksza)

p = -13
print(abs(p))

