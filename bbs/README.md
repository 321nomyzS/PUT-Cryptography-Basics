# Algorymt BBS
Algorytm BBS to jeden z algorytmów generowania ciągów pseudolosowych, który został zaproponowany przez Bluma, Blum i Shub w 1986 roku. Jest to algorytm deterministyczny, co oznacza, że na podstawie zadanego seeda (ziarna) jest w stanie generować taki sam ciąg losowych 0 i 1 za każdym razem.

Algorytm BBS polega na wyznaczeniu reszt kwadratowych modulo p i q, gdzie p i q to duże, losowo wybrane liczby pierwsze spełniające warunek, że p ≡ q ≡ 3 (mod 4). Seed (ziarno) musi być liczbą losową i względnie pierwszą z iloczynem (p-1)(q-1).

Ciąg wygenerowany przez algorytm BBS jest prawie na pewno losowy (tj. z bardzo dużym prawdopodobieństwem), ale nie jest to ciąg idealny. W szczególności, nie należy go stosować do celów kryptograficznych bez dodatkowego zabezpieczenia, np. poprzez zastosowanie procedury mieszania lub szyfrowania.

## Jak używać programu

Program bbs.py umożliwia wygenerowanie losowego ciągu 0 i 1 przy użyciu algorytmu BBS. Program ten może być uruchomiony z wiersza poleceń, a jego użycie jest bardzo proste. W programie znajduje się klasa BBS, która zawiera metodę generating_random_number, która przyjmuje jeden parametr - liczbę bitów, które mają zostać wygenerowane.

Program umożliwia dodatkowo ustawienie wartości p, q i seed. Wartość seed jest domyślnie ustawiona na losową liczbę z zakresu od 1 do 10000, ale można ją zmienić za pomocą opcji -s lub --seed. Wartości p i q można ustawić za pomocą opcji -p i -q lub --p-value i --q-value.

```
python bbs.py 16 -p 11 -q 19 -s 12345
```

Powyższa komenda spowoduje wygenerowanie losowego ciągu 16 bitów przy użyciu algorytmu BBS z wartościami p=11, q=19 i seed=12345.

## Testowanie generatora

Aby przetestować wartości p, q oraz seed, możemy użyć drugiego programu. Program bbs_test.py zawiera testy jednostkowe dla klasy BBS w programie bbs.py. Program ten korzysta z biblioteki unittest do przeprowadzenia testów. Aby uruchomić testy, należy wywołać ten program z wiersza poleceń.

Program umożliwia ustawienie wartości p, q i seed za pomocą opcji -p, -q i -s, tak samo jak program bbs.py. Można również ustawić inne opcje test

```
python bbs_test.py -p 11 -q 19 -s 12345
```