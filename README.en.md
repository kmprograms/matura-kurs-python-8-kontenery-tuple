[Polski](README.md) · **English**

---

# Computer Science Matura, extended level - Python course, part 8. "Containers - tuple"

> ### 🎬 Video walkthrough
> You can find a full step-by-step walkthrough of this material on my YouTube channel:
> **[Link to the YouTube video](https://youtu.be/8K2QsnZxA_0)**
>
> In the video I show how to create tuples (`tuple`), how to index them, unpack them and combine them with lists. Then I move on to `namedtuple` from the `collections` module, which gives you tuples with named fields.

---

## Description

This is the code for part 8 of a Python course that prepares students for the Matura exam in computer science at the extended level.

The recording builds on what you already know about tuples, the `tuple` type. Tuples have appeared earlier in the course, for example when returning more than one value from a function and when sorting by several criteria. Here I cover them in full: from creating and indexing, through lists of tuples, to `namedtuple`.

A tuple is an ordered sequence of elements, similar to a list. The key technical difference is that a tuple is immutable. Once it is created, you cannot change, add or remove an element. The practical difference is that lists usually store many elements of the same kind, while a tuple describes a single entity made of several pieces of data, often of different types. Examples are an employee with a name, age and salary, or a point with x and y coordinates.

On the Matura exam these structures are useful in tasks where you read data from a file and each line holds several values, for example three words, three numbers, or a string and a number. A list of tuples or a list of `namedtuple` objects lets you store such data in your program conveniently.

The repository also contains files from earlier parts of the course. The next recording covers dictionaries (`dict`) in Python.

## Requirements

- Python 3.10 or newer, because the `app-4-instrukcje-warunkowe.py` file uses the `match` statement
- No external dependencies, only the standard library is used (`collections`, `random`, `math`)

## Running

```bash
git clone https://github.com/kmprograms/matura-kurs-python-8-kontenery-tuple
cd matura-kurs-python-8-kontenery-tuple
python app-8-kontenery-tuple.py
```

The `main` function in `app-8-kontenery-tuple.py` currently calls only `krotki_z_nazwanymi_polami`. To run the examples from the first part of the recording, remove the comment sign before the `krotki()` call:

```python
def main() -> None:
    # krotki()
    krotki_z_nazwanymi_polami()

if __name__ == '__main__':
    main()
```

You run the other files the same way, by passing the file name, for example `python app-7-kontenery-listy.py`.

## Project structure

| File | Description |
| --- | --- |
| `app-1-pierwszy-program-zmienne.py` | First program, variables, f-strings, arithmetic operators, type conversion and augmented assignment operators |
| `app-2-liczby-calkowite.py` | Integer operations, integer division and remainder, relational operators, logical operators and the digits of a number |
| `app-3-pozyskiwanie-danych-systemy-liczbowe-float.py` | Reading input with `input` (commented out), the `random` module, number systems, bitwise operations and the `math` module |
| `app-4-instrukcje-warunkowe.py` | `if`, `elif` and `else` statements, the conditional expression, the `match` statement and the `min`, `max` and `abs` functions |
| `app-5-petle.py` | `while` and `for` loops, the `range` function, the `break` and `continue` statements and nested loops |
| `app-6-funkcje.py` | Functions, parameters and arguments, default values, type hints, `return` and returning a tuple from a function |
| `app-7-kontenery-listy.py` | Lists, indexing, list methods, `enumerate`, `zip`, sorting with `key`, slicing, two-dimensional lists, list comprehensions and generator expressions |
| `app-8-kontenery-tuple.py` | Tuples (`tuple`) and `namedtuple`, the material from this recording |

## Topics covered

### Creating tuples and accessing elements

The `krotki` function starts with three ways of writing a tuple:

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

Parentheses are not required, as the `punkt` example shows. For a single-element tuple, remember the comma after the element. Without it, Python will not treat the expression as a tuple.

Indexing works exactly as it does with lists. The first element has index 0, and negative indices and slicing work too. `pracownik[:2]` returns the elements at indices 0 and 1, and `pracownik[-1]` returns the last element, the salary.

The statement `imie, wiek, pensja = pracownik` unpacks the tuple. Its elements go into three separate variables.

### Concatenating tuples and conversions

```python
    nowy_pracownik = ("BARTEK", ) + pracownik[1:]
    print(nowy_pracownik)

    print(list(pracownik))
    print(tuple([10, 20, 30]))

    print(len(pracownik))
    for element in pracownik:
        print(element)
```

Tuples can be concatenated with the `+` operator. The new employee is named `BARTEK` and takes the age and salary from the slice `pracownik[1:]`. The original tuple does not change, a new one is created.

The `list` and `tuple` functions convert a tuple to a list and a list to a tuple. The `len` function returns the number of elements, and a `for` loop iterates over a tuple just like over a list.

### A list of tuples

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

The `list[tuple[str, int, int]]` type hint says this is a list of tuples, and each tuple holds a string and two integers. In the square brackets after `list` you give the type of the list elements, and after `tuple` you give the types of the consecutive tuple elements.

The `for` loop unpacks each tuple right in its header. In every iteration you get the name, age and salary of the next employee as separate variables.

The salary is not needed in the list comprehension, so `_` stands in its place. This symbol shows that the value is deliberately ignored. As a result, anyone reading the code does not have to check whether the salary is used somewhere.

### Maximum by several criteria

```python
    # Pracownik o największej pensji
    print(max(pracownicy, key=lambda p: (p[2], p[1])))
```

The `key` parameter works here the same way as in sorting. The lambda expression returns the tuple `(p[2], p[1])`, so the salary is compared first, and the age is compared when salaries are equal. OLA and IZA have the same salary of 5200, so the second criterion decides and IZA, who is 27, wins. `min` and `sorted` work on the same principle.

### Tuples with named fields (namedtuple)

```python
from collections import namedtuple

Pracownik = namedtuple("Pracownik", "imie, wiek, pensja")
```

You import `namedtuple` from the `collections` module. Such a type is usually created globally, at the top of the script. The first argument is the type name, and the second contains the field names written in a string and separated by commas. Field names can also be given in other ways, described in the Python documentation.

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

You can create an object by passing the values in order or together with the field names. Right at creation it is clear that this is an employee and what each value means. A `namedtuple` is still a tuple, so indexing and the `tuple(p1)` conversion work. On top of that, you access fields with the dot operator, for example `p1.imie`. You do not have to remember which index holds which piece of data, and that reduces the risk of mistakes in a Matura task. A printed object is also easier to read, because it shows the field names.

### A list of namedtuples, filtering and sorting

```python
    pracownicy: list[Pracownik] = [p1, p2, Pracownik("OLA", 30, 5200)]
    print([p.imie for p in pracownicy if p.pensja > 4000])
    print(sorted(pracownicy, key=lambda p: (p.wiek, p.pensja)))
```

The `list[Pracownik]` type hint is easier to read than `list[tuple[str, int, int]]`. In the list comprehension there is no need to unpack the tuple, because fields are available through the dot. Sorting goes by age first, and by salary when the ages are equal. ADAM and OLA are both 30, so ADAM, with the lower salary, comes first, followed by OLA.

### The `_replace` method

```python
    nowy_p1 = p1._replace(pensja=1000)
    print(nowy_p1)
```

`namedtuple` provides additional methods. `_replace` creates a new object based on an existing one and changes the specified fields. Here the new employee has the same data as `p1`, but a salary of 1000.

## Output

In its current form the program runs the `krotki_z_nazwanymi_polami` function and prints:

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

After uncommenting the `krotki()` call, the `krotki` function prints:

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

## Implementation notes

The code is grouped into the `krotki` and `krotki_z_nazwanymi_polami` functions. What actually runs is decided by the `main` function, called in the `if __name__ == '__main__':` block.

The `punkt` and `pojedynczy` variables in the `krotki` function only demonstrate a tuple written without parentheses and a single-element tuple. The program does not print them.

The `Pracownik` type is defined globally, right below the import. This makes it available in type hints and in every function of the script.

The spaces after the commas in the `"imie, wiek, pensja"` string are not a problem. The field names are still recognized correctly.

Using `namedtuple` is not mandatory. Plain tuples work too, and named fields are a matter of convenience and code readability.

I expect we will come back to `namedtuple` many times when solving Matura tasks, especially those where you read data from a file and a single line contains more than one value.