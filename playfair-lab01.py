import re
import argparse
import sys


class PlayFair:
    def __init__(self, key):
        self.alphabet = "abcdefghiklmnopqrstuvwxyz"
        self.replace_chars = {
            'j': 'i',
            'ą': 'a',
            'ć': 'c',
            'ę': 'e',
            'ł': 'l',
            'ń': 'n',
            'ó': 'o',
            'ś': 's',
            'ż': 'z',
            'ź': 'z'
        }

        # Tworzenie macierzy playfair
        key = key.lower()
        missing_letters = [letter for letter in self.alphabet if letter not in set(key)]
        key_and_remaining_alphabet = list(sorted(set(key), key=key.index)) + missing_letters
        self.matrix = [key_and_remaining_alphabet[i:i + 5] for i in range(0, len(key_and_remaining_alphabet), 5)]

    def __str__(self):
        result = \
            f"""
╔═══╦═══╦═══╦═══╦═══╗
║ {self.matrix[0][0]} ║ {self.matrix[0][1]} ║ {self.matrix[0][2]} ║ {self.matrix[0][3]} ║ {self.matrix[0][4]} ║
╠═══╬═══╬═══╬═══╬═══╣
║ {self.matrix[1][0]} ║ {self.matrix[1][1]} ║ {self.matrix[1][2]} ║ {self.matrix[1][3]} ║ {self.matrix[1][4]} ║
╠═══╬═══╬═══╬═══╬═══╣
║ {self.matrix[2][0]} ║ {self.matrix[2][1]} ║ {self.matrix[2][2]} ║ {self.matrix[2][3]} ║ {self.matrix[2][4]} ║
╠═══╬═══╬═══╬═══╬═══╣
║ {self.matrix[3][0]} ║ {self.matrix[3][1]} ║ {self.matrix[3][2]} ║ {self.matrix[3][3]} ║ {self.matrix[3][4]} ║
╠═══╬═══╬═══╬═══╬═══╣
║ {self.matrix[4][0]} ║ {self.matrix[4][1]} ║ {self.matrix[4][2]} ║ {self.matrix[4][3]} ║ {self.matrix[4][4]} ║
╚═══╩═══╩═══╩═══╩═══╝
"""
        return result

    def decode(self, secret_message):
        """
        Rozszyfrowuje zaszyfrowaną wiadomość przy pomocy algorytmu Playfair.

        :param secret_message: Zaszyfrowana wiadomość, która ma być odszyfrowana.
        :type secret_message: str
        :return: Odszyfrowana wiadomość.
        :rtype: str
        """

        text_to_decode = self._normalize_text(secret_message)
        decoded_text = self._playfair(text_to_decode, encrypt=False)
        formatted_text = self._format_text(secret_message, decoded_text)
        return formatted_text

    def encode(self, secret_message):
        """
        Szyfruje podaną wiadomość przy pomocy algorytmu Playfair.

        :param secret_message: Wiadomość, która ma być zaszyfrowana.
        :type secret_message: str
        :return: Zaszyfrowana wiadomość.
        :rtype: str
        """

        text_to_encode = self._normalize_text(secret_message)
        encoded_text = self._playfair(text_to_encode, encrypt=True)
        formatted_text = self._format_text(secret_message, encoded_text)
        return formatted_text

    def _find_letter_coordinates(self, letter):
        """
        Funkcja _find_letter_coordinates służy do znajdowania współrzędnych podanej litery w macierzy Playfair.
        W przypadku braku litery w macierzy funkcja zwraca wartość None.

        :param letter: Litera, dla której mają zostać znalezione współrzędne.
        :type letter: str
        :return: Współrzędne litery w macierzy Playfair.
        :rtype: Tuple[int, int] lub None, gdy litera nie znajduje się w macierzy.
        """
        for i, row in enumerate(self.matrix):
            try:
                position = row.index(letter)
                return i, position
            except ValueError:
                continue

    def _playfair(self, secret_message, encrypt):
        """
            Szyfruje lub odszyfrowuje podaną wiadomość szyfrem Playfair.

            :param secret_message: str
                Wiadomość do zaszyfrowania lub odszyfrowania.
            :param encrypt: int
                Wartość równa True oznacza tryb szyfrowania, wartość równa False oznacza tryb odszyfrowywania.
            :return: str
                Zaszyfrowana lub odszyfrowana wiadomość.

            Algorytm szyfrowania Playfair działa na dwuliterowych blokach tekstu jawnego.
            Jeśli długość wiadomości nie jest parzysta, dodaje się na końcu wiadomości literę "x".
            Następnie dla każdej pary kolejnych liter wiadomości znajduje się ich pozycje na macierzy 5×5.
            W zależności od wzajemnego położenia liter i trybu działania wyznacza się ich nowe pozycje na macierzy.
            Ostatecznie zaszyfrowana lub odszyfrowana wiadomość składa się z liter znajdujących się na nowych pozycjach.

        """
        if encrypt:
            mode = 1
        else:
            mode = -1

        secret_message += "x" * (len(secret_message) % 2)
        encoded_text = ""

        for i in range(0, len(secret_message), 2):
            letter_1, letter_2 = secret_message[i], secret_message[i + 1]
            start_position_1 = self._find_letter_coordinates(letter_1)
            start_position_2 = self._find_letter_coordinates(letter_2)

            # Te same litery
            if letter_1 == letter_2:
                x, y = start_position_1
                final_position_1 = final_position_2 = x, (y + mode) % 5

            # Ta sama kolumna
            elif start_position_1[0] == start_position_2[0]:
                x, y = start_position_1
                final_position_1 = x, (y + mode) % 5

                x, y = start_position_2
                final_position_2 = x, (y + mode) % 5

            # Ten sam rząd
            elif start_position_1[1] == start_position_2[1]:
                x, y = start_position_1
                final_position_1 = (x + mode) % 5, y

                x, y = start_position_2
                final_position_2 = (x + mode) % 5, y

            # Różny rząd i różna kolumna
            else:
                x_1, y_1 = start_position_1
                x_2, y_2 = start_position_2

                final_position_1 = x_1, y_2
                final_position_2 = x_2, y_1

            final_letter_1 = self.matrix[final_position_1[0]][final_position_1[1]]
            final_letter_2 = self.matrix[final_position_2[0]][final_position_2[1]]
            encoded_text += final_letter_1 + final_letter_2

        return encoded_text

    def _normalize_text(self, original_text):
        """
        Usuwa polskie znaki diakrytyczne oraz znaki niebędące literami z tekstu wejściowego.

        :param original_text: Tekst wejściowy, który ma być znormalizowany.
        :type original_text: str
        :return: znormalizowany tekst bez polskich znaków diakrytycznych i znaków niebędących literami.
        :rtype: str
        """
        original_text = original_text.lower()

        # Konwersja polskich znaków
        for char, replacement in self.replace_chars.items():
            original_text = original_text.replace(char, replacement)

        return re.sub(r'[^a-z]+', '', original_text)

    def _format_text(self, original_text, decoded_text):
        """
        Funkcja _format_text służy do uzupełnienia zaszyfrowanej wiadomości o odpowiednie znaki,
        tak aby była w takim samym formacie co oryginalny tekst.

        :param original_text: Oryginalny tekst, do którego porównujemy zaszyfrowaną wiadomość.
        :type original_text: str
        :param decoded_text: Zaszyfrowana wiadomość.
        :type decoded_text: str
        :return: Zaszyfrowana wiadomość uzupełniona o odpowiednie znaki, aby była w takim samym formacie co oryginalny tekst.
        :rtype: str
        """

        # Konwersja polskich znaków
        for char, replacement in self.replace_chars.items():
            original_text = original_text.replace(char, replacement)

        # Sprawdzanie, czy oryginalny tekst ma parzystą, czy nieparzystą liczbę liter
        original_clean = re.sub(r'[^a-zA-Z\s]+', '', original_text)
        odd_or_even = (sum([len(word) for word in original_clean.split()]) % 2)

        decoded_letters = [letter for letter in decoded_text]

        # Uzupełnianie tekst o symbole i wielkość liter
        for i, letter in enumerate(original_text):
            if letter.isalpha():
                # Wielka litera
                if letter.isupper():
                    decoded_letters[i] = decoded_letters[i].upper()
            else:
                # Ostatni znak
                if i == len(original_text) - 1:
                    decoded_letters.insert(i + odd_or_even, letter)
                # Reszta
                else:
                    decoded_letters.insert(i, letter)

        return "".join(decoded_letters)


def main():
    parser = argparse.ArgumentParser(description="Playfair cipher - an application for encrypting and decrypting text.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to a file containing the text to encrypt.")
    group.add_argument("--text", help="Text to encrypt.")
    parser.add_argument("--key", required=True, help="Playfair cipher key.")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True,
                        help="Mode of operation: encrypt - encryption, decrypt - decryption.")
    parser.add_argument("--show_matrix", action="store_true", help="Display Playfair matrix.")
    args = parser.parse_args()

    # Ładowanie danych
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_text = f.read()
        except FileNotFoundError:
            sys.stderr.write(f"Cannot open file {args.file}.\n")
            return
    else:
        input_text = args.text

    # Tworzenie obiektu Playfair
    try:
        playfair = PlayFair(args.key)
    except ValueError:
        sys.stderr.write(f"Invalid key: {args.key}.\n")
        return

    # Szyfrowanie lub odszyfrowywanie tekstu
    try:
        if args.mode == "encrypt":
            output_text = playfair.encode(input_text)
        else:
            output_text = playfair.decode(input_text)
    except ValueError as e:
        sys.stderr.write(str(e) + "\n")
        return

    # (opcjonalne) Wyświetlanie macierzy playfair
    if args.show_matrix:
        print(playfair)

    print(output_text)


if __name__ == "__main__":
    main()
