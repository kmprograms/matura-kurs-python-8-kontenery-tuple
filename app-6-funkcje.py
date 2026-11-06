def pole_prostokata_v1() -> None:
    a = int(input("Podaj pierwszy bok prostokąta: "))
    b = int(input("Podaj drugi bok prostokąta: "))
    pole = a * b
    print(f"Pole prostokąta o bokach {a} oraz {b} wynosi {pole}")

# pole_prostokata_v1()  # Tak wywołasz funkcję pole_prostokata_v1
# pole_prostokata_v1()


# a oraz b to parametry
# type hints
def pole_prostokata_v2(a: int = 1, b: int = 2) -> None:
    pole = a * b
    print(f"Pole prostokąta o bokach {a} oraz {b} wynosi {pole}")


# Kiedy wywołujesz funkcję i podstawiasz konkretne dane, wtedy mówimy,
# że podajesz argumenty
pole_prostokata_v2(10, 20)

# x = int(input("Podaj pierwszy bok prostokąta: "))
# y = int(input("Podaj drugi bok prostokąta: "))
# pole_prostokata_v2(x, y)
pole_prostokata_v2(b=11, a=22)
pole_prostokata_v2()
pole_prostokata_v2(11)
pole_prostokata_v2(b=11)

def pole_prostokata_v3(a: int = 1, b: int = 2) -> int:
    pole = a * b
    print(f"Pole prostokąta o bokach {a} oraz {b} wynosi {pole}")
    return pole

p = pole_prostokata_v3(10, 30)
if p > 100:
    print("Pole jest duże")


def pole_prostokata_v4(a: int = 1, b: int = 2) -> int:  # -> int | None:

    # W przypadku nieprawidłowych długości boków zwracamy specyficzną wartość
    # if a <= 0 or b <= 0:
    #     print(f"Podałeś złe długości boków {a=}, {b=}")
    #     # return None
    #     return -1

    # if a <= 0 or b <= 0:
    #     raise ValueError(f"Podałeś złe długości boków {a=}, {b=}")

    pole = a * b
    print(f"Pole prostokąta o bokach {a} oraz {b} wynosi {pole}")
    return pole


print(f"Pole prostokąta: {pole_prostokata_v4(10, -20)}")
print("Koniec")

def min_max_srednia(a: int, b: int, c: int) -> tuple[int, int, float]:
    najmniejsza = min(a, b, c)
    najwieksza = max(a, b, c)
    srednia = (a + b + c) / 3
    # return min(a, b, c), max(a, b, c), (a + b + c) / 3
    return najmniejsza, najwieksza, srednia

wynik = min_max_srednia(10, 20, 30)
print(wynik)
print(wynik[0])
print(wynik[1])
print(wynik[2])

najm, najw, sr = min_max_srednia(20, 30, 40)
print(najm, najw, sr)

_, najw_2, _ = min_max_srednia(20, 30, 40)
print(najw_2)

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

def obwod_prostokata(a: int, b: int) -> int:
    return 2 * (a + b)

def main() -> None:
    print("--")
    print(obwod_prostokata(10, 20))

if __name__ == '__main__':
    main()