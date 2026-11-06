a = 29
b = 3

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a ** 2 = {a ** 2}")
print(f"a / 2 = {a / 2}")
print(f"a // 2 = {a // 2}")
print(f"a % 2 = {a % 2}")

print("Parzystość liczby")
print(f"23 % 2 = {23 % 2}")
print(f"24 % 2 = {24 % 2}")
print(f"25 % 2 = {25 % 2}")
print(f"26 % 2 = {26 % 2}")

print("Podzielność")
print(f"20 % 5 = {20 % 5}")
print(f"21 % 5 = {21 % 5}")
print(f"22 % 5 = {22 % 5}")
print(f"23 % 5 = {23 % 5}")
print(f"24 % 5 = {24 % 5}")
print(f"25 % 5 = {25 % 5}")

# Operator == i pierwsze warunki logiczne
x = 21
# Chcesz sprawdzić, czy wartość w zmiennej x dzieli się przez 5
print(f"Czy {x} jest podzielne przez 5: {x % 5 == 0}")
y = 25
print(f"Czy {y} jest podzielne przez 5: {y % 5 == 0}")

# Czy lewa strona NIE jest równa prawej stronie?
# Czy wartość w zmiennej y NIE jest podzielna przez 5
print(f"Czy {y} NIE jest podzielne przez 5: {y % 5 != 0}")

# Pozostałe operatory relacji
print(f"Czy {y} jest większa od 10: {y > 10}")
print(f"Czy {y} jest większa lub równa 10: {y >= 10}")
print(f"Czy {y} jest mniejsza od 10: {y < 10}")
print(f"Czy {y} jest mniejsza lub równa 10: {y <= 10}")

# Spójniki logiczne
print(f"Czy {y} jest podzielna przez 5 i większa od 10: {y % 5 == 0 and y > 10}")
y = 5
print(f"Czy {y} jest podzielna przez 5 i większa od 10: {y % 5 == 0 and y > 10}")
y = 14
print(f"Czy {y} jest podzielna przez 7 lub większa od 20: {y % 7 == 0 or y > 20}")
print(f"Czy {y} jest podzielna przez 5 lub większa od 20: {y % 5 == 0 or y > 20}")
print(f"Czy {y} jest podzielna przez 5 lub większa od 10: {y % 5 == 0 or y > 10}")


# Cyfry liczby
n = 47218
print(f"Cyfra jedności:   {n % 10}")
print(f"Cyfra dziesiątek: {(n // 10) % 10}")
print(f"Cyfra setek:      {(n // 100) % 10}")

# Zamiana sekund na godziny, minuty i sekundy
sekundy = 7384
godziny = sekundy // 3600
reszta = sekundy % 3600
minuty = reszta // 60
pozostale_sekundy = reszta % 60
print(f"{sekundy} s = {godziny} h {minuty} min {pozostale_sekundy} s")


