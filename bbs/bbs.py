class BBS:
    def __init__(self, p, q, s):
        self.random_bytes = []
        if p % 4 != 3:
            print("Test pierwszy nie przeszedł pomyślnie -> p mod 4 != 3")
            exit()
        self.n = p*q

        if self._nwd(s, self.n) != 1:
            print("Test drugi nie przeszedł pomyślnie -> nwd(s, n) != 1")
            exit()
        self.seed = s
        self.x = [self.seed]

    def generating_random_number(self, number_size):
        for i in range(1, number_size+1):
            self.x.append((self.x[i - 1] ** 2) % self.n)
        self.random_bytes = list(map(str, map(lambda x: x % 2, self.x[1:])))
        return "".join(self.random_bytes)

    def _nwd(self, a, b):
        if b > 0:
            return self._nwd(b, a % b)
        else:
            return a

    def test1(self):
        zeros_amount = self.random_bytes.count('1')
        ones_amount = self.random_bytes.count('0')
        print(f"Ilość wystąpień '1' w ciągu bitów: {zeros_amount}")
        print(f"Ilość wystąpień '0' w ciągu bitów: {ones_amount}")

    def test2(self):
        bytes_series = self._join_neighbors(self.random_bytes)
        for i in range(1, 6):
            print(f"Seria o długości {i} występuje w ciągu {sum([1 for element in bytes_series if len(element) == i])} razy.")
        print(f"Seria o długości 6+ występuje w ciągu {sum([1 for element in bytes_series if len(element) >= 6])} razy.")

    def test3(self):
        bytes_series = self._join_neighbors(self.random_bytes)
        print(f"Najdłuższa seria ma {max(map(len, bytes_series))}")

    def test4(self):
        bytes_numbers = [self.random_bytes[i:i + 4] for i in range(0, len(self.random_bytes) - 3, 4)]

        counter = [0] * 16

        for element in bytes_numbers:
            number = int("".join(element), 2)
            counter[number] += 1

        for i, amount in enumerate(counter):
            print(f"Liczba wystąpień liczby {i} jest równa {amount}")


    def _join_neighbors(self, lst):
        result = []
        current = lst[0]
        count = 1

        for i in range(1, len(lst)):
            if lst[i] == current:
                count += 1
            else:
                result.append(str(current) * count)
                current = lst[i]
                count = 1

        result.append(str(current) * count)
        return result


def main():
    bss = BBS(p=3923, q=7919, s=1583)
    bss.generating_random_number(20000)
    bss.test1()
    print(f"{'-'* 40}")
    bss.test2()
    print(f"{'-' * 40}")
    bss.test3()
    print(f"{'-' * 40}")
    bss.test4()


main()
