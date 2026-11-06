# Lista to uporządkowany ciąg elementów zapisany w nawiasach kwadratowych.
# Lista jest modyfikowalna. Można zmieniać, dodawać i usuwać jej elementy.
# Każdy element listy ma indeks, czyli numer pozycji. Pierwszy element ma
# indeks zero. Ostatni ma indeks równy długości listy minus jeden. Indeksy
# ujemne liczą od końca. Minus jeden to ostatni element, minus dwa przedostatni.

def lista_podstawy() -> None:
    liczby = [11, 22, 33, 44, 55]
    print(liczby[0])
    print(liczby[1])
    print(liczby[-1])
    print(liczby[-2])
    print(len(liczby))
    print(liczby[len(liczby) - 1])
    # print(liczby[-10])

    liczby[0] += 2
    print(liczby)

    pusta: list[int] = []
    zera = [0] * 5
    cyfry = list(range(10))
    litery = list("abc")
    print(pusta)
    print(zera)
    print(cyfry)
    print(litery)

    # Pusta lista jest traktowana jako False
    liczby_2: list[int] = []
    if liczby_2:
        print("Lista zawiera elementy")
    else:
        print("Lista jest pusta")

    liczby_3 = [11, 22, 33, 44]
    liczby_3.append(55)  # Dodawanie elementu na koniec listy
    print(liczby_3)
    liczby_3.extend([66, 77])  # Dodawanie kilku elementów na koniec listy
    print(liczby_3)
    liczby_3.insert(2, 999)
    print(liczby_3)

    ostatni = liczby_3.pop()  # Usuwa i zwraca ostatni element
    print(liczby_3, ostatni)
    usuniety = liczby_3.pop(2)  # Usuwa i zwraca element na pozycji 2
    print(liczby_3, usuniety)
    liczby_3.remove(11)  # Usuwa pierwsze wystąpienie elementu o wartości 11
    print(liczby_3)
    del liczby_3[0]  # Usuwa element na pozycji 0
    print(liczby_3)
    # liczby_3.clear()
    # print(liczby_3)

    # Możesz bardzo szybko tworzyć nową listę z innych list - dodawanie list
    polaczona = liczby_3 + [1, 2]
    print(polaczona)

def przegladanie_listy() -> None:
    liczby = [100, 205, 300]

    print("--- [ 1 ] ---")
    for liczba in liczby:  # Przeglądasz element po elemencie
        print(liczba)

    print("--- [ 2 ] ---")
    for i in range(len(liczby)):
        print(f"indeks = {i}, wartość = {liczby[i]}")

    print("--- [ 3 ] ---")
    for index, wartosc in enumerate(liczby):
        print(f"indeks = {index}, wartość = {wartosc}")

    print("--- [ 4 ] ---")
    for index, wartosc in enumerate(liczby, start=1):
        print(f"indeks = {index}, wartość = {wartosc}")


    imiona = ["Ala", "Ola", "Jan"]
    punkty = [87, 92, 75]

    print("--- [ 5 ] ---")
    for imie, p in zip(imiona, punkty):
        print(f"Imię: {imie}, punkty: {p}")


def przeglad_metod_list() -> None:
    liczby = [10, 20, 30]
    print(10 in liczby)
    print(15 not in liczby)
    print([1, 2] + [3])
    print([1, 2] * 3)
    print([1, 2] == [1, 2])
    print([1, 2] == [2, 1])

    # Listy porównuje się element po elemencie. Pierwsze elementy są równe, więc Python
    # porównuje drugie. 2 jest mniejsze od 3, więc pierwsza lista jest mniejsza. Dalszych
    # elementów już nie sprawdza.
    print([1, 2, 9] < [1, 3])

    liczby_2 = [22, 45, 32, 56, 67, 32]
    print(len(liczby_2))
    print(sum(liczby_2))
    print(min(liczby_2))
    print(max(liczby_2))
    print(sum(liczby_2) / len(liczby_2))  # Średnia
    print(liczby_2.index(32))  # Pierwszy indeks w liście liczby_2, pod którym wystąpiła wartość 32
    print(liczby_2.count(32))  # Ile razy w liście wystąpiła wartość 32
    odwrocona_liczby_2 = list(reversed(liczby_2))  # Takie zastosowanie reversed tworzy nową listę
    print(odwrocona_liczby_2)

    liczby_3 = [11, 22, 33]
    liczby_3.reverse()  # Odwraca elementy bezpośrednio w liście liczby_3
    print(liczby_3)

    liczby_4 = [42, -7, 15, 0, -23, 8, 15, 100]
    print(sorted(liczby_4))
    print(sorted(liczby_4, reverse=True))
    print(sorted(liczby_4, key=abs))

    liczby_5 = [43, 56, 23, 13, 73, 78, 98]
    print(sorted(liczby_5, key=lambda x: x % 10))
    print(sorted(liczby_5, key=lambda x: x % 10, reverse=True))
    print(sorted(liczby_5, key=lambda x: (x % 10, x)))

    liczby_6 = [21, 45, 56, 32, 43, 21, 46, 78, 21]
    licznik = 0
    for liczba in liczby_6:
        if liczba == 21:
            licznik += 1
    print(licznik)
    liczby_6.sort()
    print(liczby_6)


def wycinki() -> None:
    liczby = list(range(1, 10))
    print(liczby)

    print(liczby[2:5])
    print(liczby[:4])
    print(liczby[4:])
    print(liczby[-3:])
    print(liczby[:-3])
    print(liczby[::2])  # co drugi element, licząc od indeksu 0
    print(liczby[1::2])  # elementy o nieparzystych indeksach
    print(liczby[2:8:3])  # indeksy 2 i 5
    print(liczby[::-1])  # odwrócona lista
    print(liczby[-1:-5:-2])
    print(liczby[5:500])  # wycinek poza zakresem nie zgłosi błędu
    print(liczby[:])  # kopia całej listy

    liczby2 = liczby[:]
    liczby2[0] = -1
    print(liczby)
    print(liczby2)


def lista_dwuwymiarowa() -> None:
    macierz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(macierz[1])
    print(macierz[0][1])
    print(len(macierz))
    print(len(macierz[0]))

    wiersze = len(macierz)
    kolumny = len(macierz[0])

    print("Macierz 1")
    for i in range(wiersze):
        for j in range(kolumny):
            print(f"i = {i}, j = {j}, element = {macierz[i][j]}", end="\t")
        print()

    macierz2: list[list[int]] = []
    macierz2.append([10, 20, 30])
    macierz2.append([40, 50, 60])
    macierz2[1].append(70)

    print("Macierz 2")
    for i in range(len(macierz2)):
        for j in range(len(macierz2[i])):
            print(f"i = {i}, j = {j}, element = {macierz2[i][j]}", end="\t")
        print()


def wyrazenia_listowe() -> None:
    liczby = [10, 20, 23, 30, 53, 40]

    # Nowa lista, w której każdy element z listy liczby będzie podwojony
    # liczby2: list[int] = []
    # for liczba in liczby:
    #     liczby2.append(2 * liczba)
    # print(liczby2)
    liczby2 = [2 * liczba for liczba in liczby]
    print(liczby2)

    # Bierzemy parzyste elementy listy liczby i podwajamy je
    liczby3 = [2 * liczba for liczba in liczby if liczba % 2 == 0]
    print(liczby3)

    # Każdy parzysty mnożysz przez 2, a nieparzysty mnożysz przez 3
    liczby4 = [2 * liczba if liczba % 2 == 0 else 3 * liczba for liczba in liczby]
    print(liczby4)


def wyrazenia_generatora() -> None:
    liczby = [10, 20, 23, 30, 53, 40]

    # Ile elementów jest podzielnych przez 5
    print(sum(1 for liczba in liczby if liczba % 5 == 0))
    print(sum(liczba % 5 == 0 for liczba in liczby))

    # Czy wszystkie elementy są większe od 0
    print(all(liczba > 0 for liczba in liczby))

    # Czy jakikolwiek element jest większy od 0
    print(any(liczba > 0 for liczba in liczby))

    # Wyrażenie generatora możesz używać z min lub max
    # Największa nieparzysta
    print(max(liczba for liczba in liczby if liczba % 2 == 1))
    # Najmniejsza nieparzysta
    print(min(liczba for liczba in liczby if liczba % 2 == 1))


def wyrazenia_listowe_listy_dwuwymiarowe() -> None:
    macierz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print([sum(wiersz) for wiersz in macierz])

    wiersze = len(macierz)
    kolumny = len(macierz[0])

    # Wierszami
    print([macierz[i][j] for i in range(wiersze) for j in range(kolumny)])

    # Kolumnami
    print([macierz[i][j] for j in range(kolumny) for i in range(wiersze)])


def main() -> None:
    # lista_podstawy()
    # przegladanie_listy()
    # przeglad_metod_list()
    # wycinki()
    # lista_dwuwymiarowa()
    # wyrazenia_listowe()
    # wyrazenia_generatora()
    wyrazenia_listowe_listy_dwuwymiarowe()


if __name__ == '__main__':
    main()