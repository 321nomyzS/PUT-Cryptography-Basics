class BBS:
    def __init__(self, p, q, seed):
        self.p = p
        self.q = q
        self.seed = seed

        self.random_bits = []
        self.n = p*q
        self.x = [self.seed]

    def generating_random_number(self, number_size):
        for i in range(1, number_size+1):
            self.x.append((self.x[i - 1] ** 2) % self.n)
        self.random_bits = list(map(str, map(lambda x: x % 2, self.x[1:])))
        return "".join(self.random_bits)


def main():
    bbs = BBS(26183, 11887, 2023)
    print(bbs.generating_random_number(1000))


if __name__ == "__main__":
    main()
