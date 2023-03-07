# Playfair
Program ten pozwala na szyfrowanie i deszyfrowanie tekstu za pomocą szyfru Playfair. Jest to szyfr polialfabetyczny, który został wynaleziony w XIX wieku. Szyfr Playfair używa macierzy z literami alfabetu, która służy do kodowania wiadomości. W przypadku tego programu, macierz jest tworzona na podstawie klucza przekazanego przez użytkownika.

Program obsługuje znaki polskie i zamienia je na ich odpowiedniki w trakcie szyfrowania i deszyfrowania. Ponadto, program radzi sobie z innymi znakami, takimi jak kropka, przecinek czy wykrzyknik, i zachowuje ich pozycję w oryginalnej wiadomości.

## Jak używać programu
Aby użyć programu, należy wprowadzić tekst do zaszyfrowania lub deszyfrowania, klucz, który będzie używany do stworzenia macierzy i wskazać, czy chcemy zaszyfrować czy odszyfrować tekst.

Używanie programu:
```
python playfair.py [-h] --mode (encrypt | decrypt) --key KEY (--file FILE | --text TEXT) [--show-matrix]
```

## Argumenty
Program wymaga trzech argumentów:

- '--key' - klucz do zaszyfrowania lub deszyfrowania tekstu, musi składać się z liter alfabetu angielskiego bez powtórzeń, bez polskich znaków i bez spacji,
- '--file' lub '--text' - tekst do zaszyfrowania lub deszyfrowania, użytkownik może wybrać jedną z tych opcji,
- '--mode': określa tryb szyfrowania, czyli 'encrypt' lub 'decrypt'. 

Opcjonalny argument:
- '--show-matrix' - wyświetla macierz, z której został zaszyfrowany tekst.

## Przykłady użycia
Aby zaszyfrować plik text.txt za pomocą klucza CRYPTOGRAPHY, należy wykonać poniższą komendę:
```
python playfair.py --encrypt --key CRYPTOGRAPHY --file text.txt
```

Aby odszyfrować tekst "Kryptografia to dziedzina wiedzy o przekazywaniu informacj.", należy wykonać poniższą komendę:
```
python playfair.py --mode decrypt --key tojestklucz --text "Atxqoiaybgtd oi guesguuwd resguv s hxcsahgsrdwud updtvhbueew!"
```

