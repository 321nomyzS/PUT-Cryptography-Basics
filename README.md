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
