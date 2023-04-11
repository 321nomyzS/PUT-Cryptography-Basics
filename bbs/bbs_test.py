import unittest
import argparse
from bbs import BBS
from math import gcd


def _join_neighbors(lst):
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


class TestBBS(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(description='Test the BBS algorithm')
        parser.add_argument('-p', type=int, default=0, help='the value of p (default: 0)')
        parser.add_argument('-q', type=int, default=0, help='the value of q (default: 0)')
        parser.add_argument('-s', '--seed', type=int, default=0, help='the seed value (default: 0)')
        self.args = parser.parse_args()

        self.bbs = BBS(p=self.args.p, q=self.args.q, seed=self.args.seed)
        self.bbs.generating_random_number(20_000)

    def test_p_q_seed(self):
        p_modulo = self.bbs.p % 4
        self.assertEqual(p_modulo, 3, f"Expected p mod 4 equal 3, but got {p_modulo}")

        q_modulo = self.bbs.q % 4
        self.assertEqual(q_modulo, 3, f"Expected q mod 4 equal 3, but got {q_modulo}")

        p_q_seed_gcd = gcd(self.bbs.seed, self.bbs.q * self.bbs.p)
        self.assertEqual(p_q_seed_gcd, 1, f"Expected GCD(seed, n) equal 1, but got {p_q_seed_gcd}")

    def test_zeros_ones_amount(self):
        zeros = self.bbs.random_bits.count('0')
        ones = self.bbs.random_bits.count('1')

        self.assertTrue(9725 < zeros < 10275, f"Expected zeros between 9725 and 10275, but got {zeros}")
        self.assertTrue(9725 < ones < 10275, f"Expected ones between 9725 and 10275, but got {ones}")

    def test_series(self):
        bytes_series = _join_neighbors(self.bbs.random_bits)
        expected_series_len = {
            1: (2315, 2685),
            2: (1114, 1386),
            3: (527, 723),
            4: (240, 384),
            5: (103, 209),
            '6+': (103, 209)
        }

        for bit in ['0', '1']:
            for i in range(1, 6):
                series_amount = sum(1 for element in bytes_series if len(element) == i and bit in element)
                min_len = expected_series_len[i][0]
                max_len = expected_series_len[i][1]
                self.assertTrue(min_len < series_amount < max_len,
                                f"Expected that the number of {bit} series of length {i} is expected to occur between {min_len} and {max_len} times, but got {series_amount}")

            series_amount = sum(1 for element in bytes_series if len(element) >= 6 and bit in element)
            min_len = expected_series_len['6+'][0]
            max_len = expected_series_len['6+'][1]
            self.assertTrue(min_len < series_amount < max_len,
                            f"Expected that the number of {bit} series of length 6+ is expected to occur between {min_len} and {max_len} times, but got {series_amount}")

    def test_longest_series(self):
        bytes_series = _join_neighbors(self.bbs.random_bits)
        longest_series = max(map(len, bytes_series))
        self.assertTrue(longest_series < 26, f"Expected that the longest series is less then 26, but is {longest_series}")

    def test_poker(self):
        bytes_numbers = [self.bbs.random_bits[i:i + 4] for i in range(0, len(self.bbs.random_bits) - 3, 4)]
        counter = [0] * 16

        for element in bytes_numbers:
            number = int("".join(element), 2)
            counter[number] += 1

        sum_of_squares = sum(number*number for number in counter)
        x = 16 / 5000 * sum_of_squares - 5000

        self.assertTrue(2.16 < x < 46.17, f"Expected 2.16 < x < 46.17, but got {x}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
