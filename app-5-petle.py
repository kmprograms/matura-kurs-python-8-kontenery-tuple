import random

# Wypisz potęgi dwójki o wykładniku naturalnym mniejsze od wartości w zmiennej n
# 1, 2, 4, 8, ...
n = random.randint(1000, 9999)
print(f"{n=}")

print("Przykład 1: ")
p = 1
while p <= n:
    print(f"Kolejna potęga 2: {p}")
    p *= 2
print("Koniec potęg 2.")


# Dodawaj kolejne liczby naturalne dodatnie, dopóki suma nie przekroczy 50

print("Przykład 2: ")

print("Wersja 1: ")
suma_calkowita = 0
k = 1
while suma_calkowita + k <= 50:
    suma_calkowita += k
    k += 1
print(f"{k - 1}, {suma_calkowita}")

print("Wersja 2: ")
suma_calkowita = 0
k = 1
while True:
    # Określasz warunek, który musi zajść, żeby pętla się skończyła
    if suma_calkowita + k > 50:
        break  # Natychmiastowe przerwanie pętli

    suma_calkowita += k
    k += 1
print(f"{k - 1}, {suma_calkowita}")


# Dodawaj kolejne liczby naturalne dodatnie niepodzielne przez 3,
# dopóki suma nie przekroczy 50

print("Przykład 3: ")
suma_calkowita = 0
ostatnia_dodana = 0
k = 0

while True:
    k += 1  # Tutaj decydujemy się na zwiększenie zmiennej o 1, żeby
    # continue nie zablokowało pętli

    if k % 3 == 0:
        continue  # Pominięcie reszty ciała pętli i przejście do
        # kolejnego obiegu

    if suma_calkowita + k > 50:
        break  # Natychmiastowe przerwanie pętli

    suma_calkowita += k
    ostatnia_dodana = k

print(f"{ostatnia_dodana}, {suma_calkowita}")


# For + range

print("\nFor - 1:")
for i in range(5):  # range(n) dostarcza kolejne wartości od 0 do n - 1
    print(i, end=" ")

print("\n\nFor - 2:")
for _ in range(5):
    print("Wykonuje się pewna operacja")

print("\nFor - 3:")
for i in range(2, 10):
    print(i, end=" ")

print("\n\nFor - 4:")
for i in range(2, 20, 3):
    print(i, end=" ")

print("\n\nFor - 5:")
for i in range(20, 1, -2):
    print(i, end=" ")

print("\n\nFor - 6:")
liczby = [10, 32, 34, 45]
for liczba in liczby:
    print(liczba)

print("\nFor - 7:")
imie = "Krzysztof"
for znak in imie:
    print(znak)

print("\nFor - 8:")
for i in range(20):
    print(f"Przed {i=}")
    if i > 10:
        # break
        continue
    print(f"Po {i=}")

# Pętla w pętli
print("\nFor - 9:")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i=},{j=}", end="\t")
    print()
