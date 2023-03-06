import re

# Zdefiniuj stałe
ALPHABET = "abcdefghiklmnopqrstuvwxyz"
KEY = "szyfr"
SECRET = "gaderypoluki"


class PlayFair:
    def __init__(self, key, alphabet):
        missing_letters = [letter for letter in alphabet if letter not in set(key)]
        key_and_remaining_alphabet = list(sorted(set(key), key=key.index)) + missing_letters
        self.matrix = [key_and_remaining_alphabet[i:i + 5] for i in range(0, len(key_and_remaining_alphabet), 5)]

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
        text_to_decode = self._normalize_text(secret_message)
        decoded_text = self._decode_playfair(text_to_decode)
        formated_text = self._format_text(secret_message, decoded_text)
        return formated_text

    def _find_letter_coordinates(self, letter):
        for i, row in enumerate(self.matrix):
            try:
                position = row.index(letter)
                return i, position
            except ValueError:
                continue

    def _decode_playfair(self, secret_message):
        secret_message += "x" * (len(secret_message) % 2)
        decoded_text = ""

        for i in range(0, len(secret_message), 2):
            letter_1, letter_2 = secret_message[i], secret_message[i + 1]
            start_position_1 = self._find_letter_coordinates(letter_1)
            start_position_2 = self._find_letter_coordinates(letter_2)

            # Te same litery
            if letter_1 == letter_2:
                x, y = start_position_1
                final_position_1 = final_position_2 = x, (y + 1) % 5

            # Ta sama kolumna
            elif start_position_1[0] == start_position_2[0]:
                x, y = start_position_1
                final_position_1 = x, (y + 1) % 5

                x, y = start_position_2
                final_position_2 = x, (y + 1) % 5

            # Ten sam rząd
            elif start_position_1[1] == start_position_2[1]:
                x, y = start_position_1
                final_position_1 = (x + 1) % 5, y

                x, y = start_position_2
                final_position_2 = (x + 1) % 5, y

            # Różny rząd i różna kolumna
            else:
                x_1, y_1 = start_position_1
                x_2, y_2 = start_position_2

                final_position_1 = x_1, y_2
                final_position_2 = x_2, y_1

            final_letter_1 = self.matrix[final_position_1[0]][final_position_1[1]]
            final_letter_2 = self.matrix[final_position_2[0]][final_position_2[1]]
            decoded_text += final_letter_1 + final_letter_2

        return decoded_text

    def _normalize_text(self, original_text):
        """
        Usuwa polskie znaki diakrytyczne oraz znaki niebędące literami z tekstu wejściowego.

        :param original_text: Tekst wejściowy, który ma być znormalizowany.
        :type original_text: str
        :return: znormalizowany tekst bez polskich znaków diakrytycznych i znaków niebędących literami.
        :rtype: str
        """
        original_text = original_text.lower()

        for char, replacement in self.replace_chars.items():
            original_text = original_text.replace(char, replacement)

        return re.sub(r'[^a-z]+', '', original_text)

    def _format_text(self, original_text, decoded_text):
        for char, replacement in self.replace_chars.items():
            original_text = original_text.replace(char, replacement)

        original_clean = re.sub(r'[^a-zA-Z\s]+', '', original_text)
        original_clean += "x" * (sum([len(word) for word in original_clean.split()]) % 2)

        return ""


playfair = PlayFair(KEY, ALPHABET)
tekst = "Ala ma kota o imieniu Aleksander, który jest bardzo miły. Jak ma na imię?"
playfair.decode(tekst)
