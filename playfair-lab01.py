# Zdefiniuj stałe
ALPHABET = "abcdefghiklmnopqrstuvwxyz"
KEY = "szyfr"
SECRET = "ga de ry po lu,++123 ki"


class PlayFair:
    def __init__(self, key, alphabet):
        missing_letters = [letter for letter in alphabet if letter not in set(key)]
        key_and_remaining_alphabet = list(sorted(set(key), key=key.index)) + missing_letters
        self.matrix = [key_and_remaining_alphabet[i:i + 5] for i in range(0, len(key_and_remaining_alphabet), 5)]

    def find_letter_coordinates(self, letter):
        for i, row in enumerate(self.matrix):
            try:
                position = row.index(letter)
                return i, position
            except ValueError:
                continue

    def decode(self, secret_message):
        # Zbieranie informacji o podanym tekście
        signs = [' ', ',', '.']
        signs_stats = []
        for sign in signs:
            signs_stats.append((sign, [i for i in range(len(secret_message)) if secret_message[i] == sign]))

        secret_without_spaces = ''.join(c for c in secret_message if c.isalpha()).lower()
        secret_message = secret_without_spaces + "x" * (len(secret_without_spaces) % 2)
        final_message = ""

        for i in range(0, len(secret_message), 2):
            letter_1, letter_2 = secret_message[i], secret_message[i + 1]
            start_position_1 = self.find_letter_coordinates(letter_1)
            start_position_2 = self.find_letter_coordinates(letter_2)

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
            final_message = final_message + final_letter_1 + final_letter_2

        return final_message

    def get_text_stats(self):
        return []


playfair = PlayFair(KEY, ALPHABET)
print(playfair.decode(SECRET))
