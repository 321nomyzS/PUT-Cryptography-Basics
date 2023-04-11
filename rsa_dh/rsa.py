from math import gcd


class RSA:
    def __init__(self, p, q):
        self.n = p*q
        self.phi_n = (p-1) * (q-1)

        self.e = self.calculate_e()
        self.d = pow(self.e, -1, self.phi_n)

    def calculate_e(self):
        self.e = 2
        while self.e < self.phi_n:
            if gcd(self.e, self.phi_n) == 1:
                return self.e
            else:
                self.e += 1

    def _encode_number(self, msg):
        c = pow(msg, self.e) % self.n
        return c

    def _decode_number(self, c):
        msg = pow(c, self.d) % self.n
        return msg

    def encode_message(self, msg):
        message_letters_ascii = [ord(element) for element in [*msg]]
        encoded_letters_ascii = [self._encode_number(element) for element in message_letters_ascii]
        return encoded_letters_ascii

    def decode_message(self, sec):
        encoded_letters_ascii = [self._decode_number(element) for element in sec]
        encoded_letters = [chr(int(element)) for element in encoded_letters_ascii]

        return "".join(encoded_letters)

    def __str__(self):
        obj = \
f"""{"*"*15}
n = {self.n}
phi(n) = {self.phi_n}
e = {self.e}
d = {self.d}
{"*"*15}
"""
        return obj


if __name__ == "__main__":
    rsa = RSA(457, 641)
    message = input("Type message to encode using RSA algorithm: ")

    secret = rsa.encode_message(message)
    print(f"Secret generated using RSA algorithm: {secret}")

    message = rsa.decode_message(secret)
    print(f"Message decoded from secret using RSA algorithm: {message}")
