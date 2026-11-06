import random
import math

# imie = input("Podaj imię: ")
# print(imie)
#
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
# print(f'a + b = {a + b}')
#
# waga = float(input("Podaj wagę: "))
# print(waga + 10)


x1 = random.randint(1, 6)  # Wartość od 1 do 6
print(f"{x1 = }")

x2 = random.uniform(2, 19.3)
print(f"{x2 = } lub {round(x2, 2)}")

x3 = random.randrange(0, 100, 2)  # 0, 2, 4, ..., 98
print(f"{x3 = }")

# ---------------------------------------------------------------------------------
# Systemy liczbowe i operacje na bitach
# ---------------------------------------------------------------------------------
n = 2026
print(bin(n))
print(oct(n))
print(hex(n))

s1 = 0b10001011
s2 = 0o17
s3 = 0xff

print(int("1101", 2))
print(int("12", 3))

a = 0b1010
b = 0b1100

print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
print(bin(12 << 1))
print(bin(12 >> 1))

# ---------------------------------------------------------------------------------
# Moduł math
# ---------------------------------------------------------------------------------

print(math.sqrt(19))
print(math.isqrt(19))
print(19 ** 0.5)
print(math.pow(2, 10))
print(math.floor(19 ** 0.5))
print(math.ceil(19 ** 0.5))

# https://docs.python.org/3/library/math.html
# https://docs.python.org/3/library/random.html