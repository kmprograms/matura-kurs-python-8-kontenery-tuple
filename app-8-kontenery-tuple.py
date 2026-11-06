from collections import namedtuple

Pracownik = namedtuple("Pracownik", "imie, wiek, pensja")

def krotki() -> None:
    pracownik = ("ADAM", 30, 3500)
    punkt = 3, 7
    pojedynczy = ("EWA", )
    print(pracownik[0])
    print(pracownik[:2])
    print(pracownik[-1])
    imie, wiek, pensja = pracownik
    print(f"{imie=}, {wiek=}, {pensja=}")

    nowy_pracownik = ("BARTEK", ) + pracownik[1:]
    print(nowy_pracownik)

    print(list(pracownik))
    print(tuple([10, 20, 30]))

    print(len(pracownik))
    for element in pracownik:
        print(element)


    pracownicy: list[tuple[str, int, int]] = [
        ("ADAM", 30, 3500),
        ("EWA", 40, 4500),
        ("OLA", 25, 5200),
        ("IZA", 27, 5200),
    ]

    for imie, wiek, pensja in pracownicy:
        print(f"Pracownik {imie} ma wiek {wiek} i pensję {pensja}")

    # Bierzemy imiona pracowników o wieku większym od 28
    print([imie for imie, wiek, _ in pracownicy if wiek > 28])

    # Pracownik o największej pensji
    print(max(pracownicy, key=lambda p: (p[2], p[1])))


def krotki_z_nazwanymi_polami() -> None:
    p1 = Pracownik("ADAM", 30, 3500)
    p2 = Pracownik(imie="EWA", wiek=50, pensja=4500)
    print(p1)
    print(tuple(p1))
    print(p1[0])
    print(p1.imie)
    print(p1.wiek)
    print(p1.pensja)

    pracownicy: list[Pracownik] = [p1, p2, Pracownik("OLA", 30, 5200)]
    print([p.imie for p in pracownicy if p.pensja > 4000])
    print(sorted(pracownicy, key=lambda p: (p.wiek, p.pensja)))

    nowy_p1 = p1._replace(pensja=1000)
    print(nowy_p1)


def main() -> None:
    # krotki()
    krotki_z_nazwanymi_polami()

if __name__ == '__main__':
    main()