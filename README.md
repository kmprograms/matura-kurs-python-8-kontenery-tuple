**Polski** · [English](README.en.md)

---

# Matura z informatyki, poziom rozszerzony - kurs Pythona, część 8. "Kontenery - tuple"

> ### 🎬 Wideo z omówieniem
> Pełne omówienie tego materiału krok po kroku znajdziesz na moim kanale YouTube:
> **[Link do filmu na YouTube](https://youtu.be/8K2QsnZxA_0)**
>
> Na filmie pokazuję, jak tworzyć krotki (`tuple`), jak je indeksować, rozpakowywać i łączyć z listami. Potem przechodzę do `namedtuple` z modułu `collections`, czyli krotek z nazwanymi polami.

---

## Opis

To kod do ósmej części kursu Pythona, który przygotowuje do matury z informatyki na poziomie rozszerzonym.

Nagranie uzupełnia wiadomości o krotkach, czyli typie `tuple`. Krotki pojawiały się już wcześniej w kursie, na przykład przy zwracaniu z funkcji więcej niż jednej wartości i przy sortowaniu po kilku kryteriach. Tutaj omawiam je w całości: od tworzenia i indeksowania, przez listy krotek, aż po `namedtuple`.

Krotka to uporządkowany ciąg elementów podobny do listy. Najważniejsza różnica techniczna jest taka, że krotka jest niemodyfikowalna. Po jej utworzeniu nie zmienisz, nie dodasz ani nie usuniesz elementu. Różnica użytkowa polega na tym, że w listach zwykle przechowujesz wiele elementów tego samego rodzaju, a krotka opisuje jeden byt złożony z kilku danych, często różnego typu. Przykładem jest pracownik z imieniem, wiekiem i pensją albo punkt o współrzędnych x i y.

Na maturze takie struktury przydają się w zadaniach, w których wczytujesz dane z pliku, a w każdym wierszu jest kilka wartości, na przykład trzy słowa, trzy liczby albo napis i liczba. Lista krotek albo lista obiektów `namedtuple` pozwala wygodnie przechować takie dane w programie.

Repozytorium zawiera też pliki z wcześniejszych części kursu. Kolejne nagranie dotyczy słowników (`dict`) w Pythonie.

## Wymagania

- Python 3.10 lub nowszy, ponieważ plik `app-4-instrukcje-warunkowe.py` korzysta z instrukcji `match`
- Brak zewnętrznych zależności, wykorzystano wyłącznie bibliotekę standardową (`collections`, `random`, `math`)

## Uruchomienie

```bash
git clone https://github.com/kmprograms/matura-kurs-python-8-kontenery-tuple
cd matura-kurs-python-8-kontenery-tuple
python app-8-kontenery-tuple.py
```

Funkcja `main` w pliku `app-8-kontenery-tuple.py` wywołuje obecnie tylko `krotki_z_nazwanymi_polami`. Żeby uruchomić przykłady z pierwszej części nagrania, usuń znak komentarza przed wywołaniem `krotki()`:

```python
def main() -> None:
    # krotki()
    krotki_z_nazwanymi_polami()

if __name__ == '__main__':
    main()
```

Pozostałe pliki uruchamiasz tak samo, podając nazwę pliku, na przykład `python app-7-kontenery-listy.py`.

## Struktura projektu

| Plik | Opis |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | Pierwszy program, zmienne, f-stringi, operatory arytmetyczne, zamiana typów i operatory przypisania złożonego |
| `app-2-liczby-calkowite.py` | Operacje na liczbach całkowitych, dzielenie całkowite i reszta z dzielenia, operatory relacji, spójniki logiczne i cyfry liczby |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Pobieranie danych funkcją `input` (fragment zakomentowany), moduł `random`, systemy liczbowe, operacje na bitach i moduł `math` |
| `app-4-instrukcje-warunkowe.py` | Instrukcje `if`, `elif` i `else`, wyrażenie warunkowe, instrukcja `match` oraz funkcje `min`, `max` i `abs` |
| `app-5-petle.py` | Pętle `while` i `for`, funkcja `range`, instrukcje `break` i `continue` oraz pętle zagnieżdżone |
| `app-6-funkcje.py` | Funkcje, parametry i argumenty, wartości domyślne, adnotacje typów, `return` i zwracanie krotki z funkcji |
| `app-7-kontenery-listy.py` | Listy, indeksowanie, metody list, `enumerate`, `zip`, sortowanie z `key`, wycinki, listy dwuwymiarowe, wyrażenia listowe i wyrażenia generatora |
| `app-8-kontenery-tuple.py` | Krotki (`tuple`) i `namedtuple`, czyli materiał z tego nagrania |

## Omawiane zagadnienia

### Tworzenie krotek i dostęp do elementów

Funkcja `krotki` zaczyna od trzech sposobów zapisu krotki:

```python
def krotki() -> None:
    pracownik = ("ADAM", 30, 3500)
    punkt = 3, 7
    pojedynczy = ("EWA", )
    print(pracownik[0])
    print(pracownik[:2])
    print(pracownik[-1])
    imie, wiek, pensja = pracownik
    print(f"{imie=}, {wiek=}, {pensja=}")
```

Nawiasy okrągłe nie są konieczne, co widać na przykładzie `punkt`. Przy krotce jednoelementowej pamiętaj o przecinku po elemencie. Bez niego Python nie potraktuje zapisu jako krotki.

Indeksowanie działa tak samo jak w listach. Pierwszy element ma indeks 0, działają też indeksy ujemne i wycinki. `pracownik[:2]` zwraca elementy o indeksach 0 i 1, a `pracownik[-1]` zwraca ostatni element, czyli pensję.

Zapis `imie, wiek, pensja = pracownik` rozpakowuje krotkę. Kolejne elementy trafiają do trzech osobnych zmiennych.

### Łączenie krotek i konwersje

```python
    nowy_pracownik = ("BARTEK", ) + pracownik[1:]
    print(nowy_pracownik)

    print(list(pracownik))
    print(tuple([10, 20, 30]))

    print(len(pracownik))
    for element in pracownik:
        print(element)
```

Krotki można łączyć operatorem `+`. Nowy pracownik ma imię `BARTEK`, a wiek i pensję przejmuje z wycinka `pracownik[1:]`. Oryginalna krotka się nie zmienia, powstaje nowa.

Funkcje `list` i `tuple` zamieniają krotkę na listę i listę na krotkę. Funkcja `len` zwraca liczbę elementów, a pętla `for` przechodzi po krotce tak samo jak po liście.

### Lista krotek

```python
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
```

Adnotacja `list[tuple[str, int, int]]` mówi, że to lista krotek, a każda krotka zawiera napis i dwie liczby całkowite. W nawiasach kwadratowych przy `list` podajesz typ elementów listy, a przy `tuple` typy kolejnych elementów krotki.

Pętla `for` rozpakowuje każdą krotkę już w nagłówku. W każdym obiegu masz osobno imię, wiek i pensję kolejnego pracownika.

W wyrażeniu listowym pensja nie jest potrzebna, dlatego w jej miejscu stoi `_`. Ten znak pokazuje, że wartość jest celowo pomijana. Dzięki temu osoba czytająca kod nie musi sprawdzać, czy pensja została gdzieś użyta.

### Maksimum według kilku kryteriów

```python
    # Pracownik o największej pensji
    print(max(pracownicy, key=lambda p: (p[2], p[1])))
```

Parametr `key` działa tu tak samo jak przy sortowaniu. Wyrażenie lambda zwraca krotkę `(p[2], p[1])`, więc najpierw porównywana jest pensja, a przy równych pensjach wiek. OLA i IZA mają tę samą pensję 5200, dlatego o wyniku decyduje drugie kryterium i wygrywa IZA, która ma 27 lat. Na tej samej zasadzie działają `min` i `sorted`.

### Krotki z nazwanymi polami (namedtuple)

```python
from collections import namedtuple

Pracownik = namedtuple("Pracownik", "imie, wiek, pensja")
```

`namedtuple` importujesz z modułu `collections`. Taki typ zwykle tworzy się globalnie, na górze skryptu. Pierwszy argument to nazwa typu, a drugi to nazwy pól zapisane w napisie i oddzielone przecinkami. Nazwy pól można podać też na inne sposoby, które opisuje dokumentacja Pythona.

```python
def krotki_z_nazwanymi_polami() -> None:
    p1 = Pracownik("ADAM", 30, 3500)
    p2 = Pracownik(imie="EWA", wiek=50, pensja=4500)
    print(p1)
    print(tuple(p1))
    print(p1[0])
    print(p1.imie)
    print(p1.wiek)
    print(p1.pensja)
```

Obiekt możesz utworzyć, podając wartości po kolei albo razem z nazwami pól. Już przy tworzeniu wiadomo, że chodzi o pracownika i co oznacza każda wartość. `namedtuple` nadal jest krotką, więc działa indeksowanie i konwersja `tuple(p1)`. Dodatkowo do pól odwołujesz się operatorem kropki, na przykład `p1.imie`. Nie musisz pamiętać, pod którym indeksem jest która dana, a to zmniejsza ryzyko pomyłki w zadaniu maturalnym. Wypisany obiekt też jest czytelniejszy, bo pokazuje nazwy pól.

### Lista namedtuple, filtrowanie i sortowanie

```python
    pracownicy: list[Pracownik] = [p1, p2, Pracownik("OLA", 30, 5200)]
    print([p.imie for p in pracownicy if p.pensja > 4000])
    print(sorted(pracownicy, key=lambda p: (p.wiek, p.pensja)))
```

Adnotacja `list[Pracownik]` jest czytelniejsza niż `list[tuple[str, int, int]]`. W wyrażeniu listowym nie trzeba rozpakowywać krotki, bo pola są dostępne przez kropkę. Sortowanie odbywa się najpierw po wieku, a przy równym wieku po pensji. ADAM i OLA mają po 30 lat, dlatego jako pierwszy jest ADAM z niższą pensją, a po nim OLA.

### Metoda `_replace`

```python
    nowy_p1 = p1._replace(pensja=1000)
    print(nowy_p1)
```

`namedtuple` udostępnia dodatkowe metody. `_replace` tworzy nowy obiekt na podstawie istniejącego i zmienia wskazane pola. Tutaj nowy pracownik ma te same dane co `p1`, ale pensję 1000.

## Wyniki

Program w obecnej postaci uruchamia funkcję `krotki_z_nazwanymi_polami` i wypisuje:

```
Pracownik(imie='ADAM', wiek=30, pensja=3500)
('ADAM', 30, 3500)
ADAM
ADAM
30
3500
['EWA', 'OLA']
[Pracownik(imie='ADAM', wiek=30, pensja=3500), Pracownik(imie='OLA', wiek=30, pensja=5200), Pracownik(imie='EWA', wiek=50, pensja=4500)]
Pracownik(imie='ADAM', wiek=30, pensja=1000)
```

Po odkomentowaniu wywołania `krotki()` funkcja `krotki` wypisuje:

```
ADAM
('ADAM', 30)
3500
imie='ADAM', wiek=30, pensja=3500
('BARTEK', 30, 3500)
['ADAM', 30, 3500]
(10, 20, 30)
3
ADAM
30
3500
Pracownik ADAM ma wiek 30 i pensję 3500
Pracownik EWA ma wiek 40 i pensję 4500
Pracownik OLA ma wiek 25 i pensję 5200
Pracownik IZA ma wiek 27 i pensję 5200
['ADAM', 'EWA']
('IZA', 27, 5200)
```

## Uwagi implementacyjne

Kod jest pogrupowany w funkcje `krotki` i `krotki_z_nazwanymi_polami`. O tym, co się uruchomi, decyduje funkcja `main` wywoływana w bloku `if __name__ == '__main__':`.

Zmienne `punkt` i `pojedynczy` w funkcji `krotki` pokazują tylko zapis krotki bez nawiasów i krotki jednoelementowej. Program ich nie wypisuje.

Typ `Pracownik` jest zdefiniowany globalnie, zaraz pod importem. Dzięki temu można go używać w adnotacjach typów i w każdej funkcji skryptu.

Spacje po przecinkach w napisie `"imie, wiek, pensja"` nie przeszkadzają. Nazwy pól zostaną rozpoznane poprawnie.

Używanie `namedtuple` nie jest obowiązkowe. Klasyczne krotki też działają, a nazwane pola to kwestia wygody i czytelności kodu.

Myślę, że do `namedtuple` wrócimy jeszcze nie raz przy rozwiązywaniu zadań maturalnych, szczególnie tych, w których wczytujesz dane z pliku i w jednym wierszu jest więcej niż jedna dana.