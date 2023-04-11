import argparse
import random


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
    parser = argparse.ArgumentParser(description='Generate a random sequence of 0s and 1s using the BBS algorithm')
    parser.add_argument('num_bits', type=int, help='the number of bits to generate')
    parser.add_argument('-p', type=int, default=26183, help='the value of p (default: 26183)')
    parser.add_argument('-q', type=int, default=11887, help='the value of q (default: 11887)')
    parser.add_argument('-s', '--seed', type=int, default=random.randint(1, 10000),
                        help='the seed value (default: a random integer between 1 and 10000)')

    args = parser.parse_args()

    bbs = BBS(p=args.p, q=args.q, seed=args.seed)
    print(bbs.generating_random_number(1000))


if __name__ == "__main__":
    main()
