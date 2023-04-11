# Cryptography_Basics
Ten projekt zawiera różne programy związane z kryptografią.

## Szyfr Playfair
playfair.py to program umożliwiający szyfrowanie i deszyfrowanie wiadomości przy użyciu szyfru Playfair. Program obsługuje znaki polskie, a także inne znaki specjalne takie jak kropki, przecinki itp.

### Jak używać?
Program można uruchomić za pomocą wiersza poleceń. Aby zaszyfrować wiadomość, należy wywołać program z opcją --mode encrypt i podać wiadomość do zaszyfrowania. Aby odszyfrować wiadomość, należy wywołać program z opcją --mode decrypt i podać zaszyfrowaną wiadomość.
Program obsługuje również szyfrowanie treści pliku lub treści wpisanej w poleceniu.

Przykład szyfrowania wiadomości:
```
python playfair.py --mode encrypt --text "To jest tajna wiadomość" --key tojestklucz
```

Przykład odszyfrowania wiadomości:
```
python playfair.py --mode decrypt --file plik.txt --key tojestklucz
```

## Algorytm BBS
Algorytm BBS to jeden z algorytmów generowania ciągów pseudolosowych, który został zaproponowany przez Bluma, Blum i Shub w 1986 roku. Jest to algorytm deterministyczny, co oznacza, że na podstawie zadanego seeda (ziarna) jest w stanie generować taki sam ciąg losowych 0 i 1 za każdym razem.

### Jak używać?
Program bbs.py umożliwia wygenerowanie losowego ciągu 0 i 1 przy użyciu algorytmu BBS. Program ten może być uruchomiony z wiersza poleceń, a jego użycie jest bardzo proste. W programie znajduje się klasa BBS, która zawiera metodę generating_random_number, która przyjmuje jeden parametr - liczbę bitów, które mają zostać wygenerowane.

Program umożliwia dodatkowo ustawienie wartości p, q i seed. Wartość seed jest domyślnie ustawiona na losową liczbę z zakresu od 1 do 10000, ale można ją zmienić za pomocą opcji -s lub --seed. Wartości p i q można ustawić za pomocą opcji -p i -q lub --p-value i --q-value.

```
python bbs.py 16 -p 11 -q 19 -s 12345
```