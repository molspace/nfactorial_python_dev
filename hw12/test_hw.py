import unittest
import hw


class TestFunctions(unittest.TestCase):
    # Exercise-1
    def test_squares(self):
        self.assertEqual(hw.squares(5), [i**2 for i in range(5)])
        self.assertEqual(hw.squares(1000), [i**2 for i in range(1000)])
        self.assertEqual(hw.squares(10000), [i**2 for i in range(10000)])
        self.assertEqual(hw.squares(0), [])
        self.assertEqual(hw.squares(5000), [i**2 for i in range(5000)])

    # Exercise-2
    def test_unique_squares(self):
        self.assertEqual(
            hw.unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), {1, 4, 9, 16}
        )
        self.assertEqual(
            hw.unique_squares([i for i in range(1, 1000)] * 10),
            {i**2 for i in range(1, 1000)},
        )
        self.assertEqual(
            hw.unique_squares([i for i in range(1, 5000)] * 20),
            {i**2 for i in range(1, 5000)},
        )
        self.assertEqual(hw.unique_squares([1, 1, 1, 1]), {1})
        self.assertEqual(
            hw.unique_squares([i for i in range(1, 2000)] * 30),
            {i**2 for i in range(1, 2000)},
        )

    # Exercise-3
    def test_char_counts(self):
        self.assertEqual(hw.char_counts("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})
        self.assertEqual(
            hw.char_counts("a" * 10000 + "b" * 10000), {char: 10000 for char in "ab"}
        )
        self.assertEqual(
            hw.char_counts("abcde" * 2000), {char: 2000 for char in "abcde"}
        )
        self.assertEqual(hw.char_counts("a"), {"a": 1})
        self.assertEqual(
            hw.char_counts("abcdef" * 3000), {char: 3000 for char in "abcdef"}
        )

    # Exercise-4
    def test_flatten(self):
        self.assertEqual(
            hw.flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            hw.flatten([[i for i in range(1, 1000)]] * 10),
            [i for i in range(1, 1000)] * 10,
        )
        self.assertEqual(
            hw.flatten([[i for i in range(1, 2000)]] * 20),
            [i for i in range(1, 2000)] * 20,
        )
        self.assertEqual(hw.flatten([[1]]), [1])
        self.assertEqual(
            hw.flatten([[i for i in range(1, 3000)]] * 30),
            [i for i in range(1, 3000)] * 30,
        )

    # Exercise-5
    def test_squares_gen(self):
        self.assertEqual(list(hw.squares_gen(5)), [0, 1, 4, 9, 16])
        self.assertEqual(list(hw.squares_gen(1000)), [i**2 for i in range(1000)])
        self.assertEqual(list(hw.squares_gen(2000)), [i**2 for i in range(2000)])
        self.assertEqual(list(hw.squares_gen(0)), [])
        self.assertEqual(list(hw.squares_gen(3000)), [i**2 for i in range(3000)])

    # Exercise-6
    def test_odd_squares(self):
        self.assertCountEqual(hw.odd_squares(10), {1, 9, 25, 49, 81})
        self.assertCountEqual(hw.odd_squares(1000), {i**2 for i in range(1, 1000, 2)})
        self.assertCountEqual(hw.odd_squares(2000), {i**2 for i in range(1, 2000, 2)})
        self.assertCountEqual(hw.odd_squares(1), {1})
        self.assertCountEqual(hw.odd_squares(3000), {i**2 for i in range(1, 3000, 2)})

    # Exercise-7
    def test_index_map(self):
        self.assertEqual(hw.index_map("hello"), {"h": 0, "e": 1, "l": 3, "o": 4})
        self.assertEqual(hw.index_map("a" * 1000 + "b" * 1000), {"a": 999, "b": 1999})
        self.assertEqual(
            hw.index_map("abcde" * 200),
            {"a": 995, "b": 996, "c": 997, "d": 998, "e": 999},
        )
        self.assertEqual(hw.index_map("a"), {"a": 0})
        self.assertEqual(
            hw.index_map("abcdef" * 300),
            {"a": 1794, "b": 1795, "c": 1796, "d": 1797, "e": 1798, "f": 1799},
        )

    # Exercise-8
    def test_unique_values(self):
        self.assertEqual(
            hw.unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {1, 2, 3, 4, 5}
        )
        self.assertEqual(
            hw.unique_values([list(range(1, 1000))] * 10), set(range(1, 1000))
        )
        self.assertEqual(
            hw.unique_values([list(range(1, 2000))] * 20), set(range(1, 2000))
        )
        self.assertEqual(hw.unique_values([[1]]), {1})
        self.assertEqual(
            hw.unique_values([list(range(1, 3000))] * 30), set(range(1, 3000))
        )

    # Exercise-9
    def test_fibonacci_gen(self):
        self.assertEqual(list(hw.fibonacci_gen(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        fibs = [0, 1]
        for _ in range(2, 1000):
            fibs.append(fibs[-1] + fibs[-2])
        self.assertEqual(list(hw.fibonacci_gen(1000)), fibs)
        fibs = [0, 1]
        for _ in range(2, 2000):
            fibs.append(fibs[-1] + fibs[-2])
        self.assertEqual(list(hw.fibonacci_gen(2000)), fibs)
        self.assertEqual(list(hw.fibonacci_gen(1)), [0])
        fibs = [0, 1]
        for _ in range(2, 3000):
            fibs.append(fibs[-1] + fibs[-2])
        self.assertEqual(list(hw.fibonacci_gen(3000)), fibs)

    # Exercise-10
    def test_invert_dict(self):
        self.assertEqual(
            hw.invert_dict({"a": 1, "b": 2, "c": 3}), {1: "a", 2: "b", 3: "c"}
        )
        self.assertEqual(
            hw.invert_dict({i: str(i) for i in range(1, 1000)}),
            {str(i): i for i in range(1, 1000)},
        )
        self.assertEqual(
            hw.invert_dict({i: str(i) for i in range(1, 2000)}),
            {str(i): i for i in range(1, 2000)},
        )
        self.assertEqual(hw.invert_dict({1: "a"}), {"a": 1})
        self.assertEqual(
            hw.invert_dict({i: str(i) for i in range(1, 3000)}),
            {str(i): i for i in range(1, 3000)},
        )

    # Exercise-11
    def test_primes(self):
        self.assertEqual(hw.primes(10), [2, 3, 5, 7])
        self.assertEqual(
            hw.primes(1000),
            [
                i
                for i in range(2, 1000)
                if all(i % x != 0 for x in range(2, int(i**0.5) + 1))
            ],
        )
        self.assertEqual(
            hw.primes(2000),
            [
                i
                for i in range(2, 2000)
                if all(i % x != 0 for x in range(2, int(i**0.5) + 1))
            ],
        )
        self.assertEqual(hw.primes(1), [])
        self.assertEqual(
            hw.primes(3000),
            [
                i
                for i in range(2, 3000)
                if all(i % x != 0 for x in range(2, int(i**0.5) + 1))
            ],
        )

    # Exercise-12
    def test_intersection(self):
        self.assertEqual(hw.intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]), {3})
        self.assertEqual(
            hw.intersection([set(range(1, 1000))] * 10), set(range(1, 1000))
        )
        self.assertEqual(
            hw.intersection([set(range(1, 2000))] * 20), set(range(1, 2000))
        )
        self.assertEqual(hw.intersection([{1}] * 100), {1})
        self.assertEqual(
            hw.intersection([set(range(1, 3000))] * 30), set(range(1, 3000))
        )

    # Exercise-13
    def test_factorials_gen(self):
        import math

        self.assertEqual(
            list(hw.factorials_gen(5)), [math.factorial(x) for x in range(5)]
        )
        self.assertEqual(
            list(hw.factorials_gen(100)), [math.factorial(x) for x in range(100)]
        )
        self.assertEqual(
            list(hw.factorials_gen(200)), [math.factorial(x) for x in range(200)]
        )
        self.assertEqual(list(hw.factorials_gen(1)), [1])
        self.assertEqual(
            list(hw.factorials_gen(300)), [math.factorial(x) for x in range(300)]
        )

    # Exercise-14
    def test_str_lengths(self):
        self.assertEqual(
            hw.str_lengths(["hello", "world", "python"]),
            {"hello": 5, "world": 5, "python": 6},
        )
        self.assertEqual(
            hw.str_lengths(["a" * i for i in range(1, 1000)]),
            {str(i * "a"): i for i in range(1, 1000)},
        )
        self.assertEqual(
            hw.str_lengths(["a" * i for i in range(1, 2000)]),
            {str(i * "a"): i for i in range(1, 2000)},
        )
        self.assertEqual(hw.str_lengths(["a"]), {"a": 1})
        self.assertEqual(
            hw.str_lengths(["a" * i for i in range(1, 3000)]),
            {str(i * "a"): i for i in range(1, 3000)},
        )

    # Exercise-15
    def test_transpose(self):
        self.assertEqual(
            hw.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        )
        self.assertEqual(
            hw.transpose([[i for i in range(j, j + 5)] for j in range(1, 1000)]),
            [[i for i in range(j, j + 999)] for j in range(1, 6)],
        )
        self.assertEqual(
            hw.transpose([[i for i in range(j, j + 10)] for j in range(1, 2000)]),
            [[i for i in range(j, j + 1999)] for j in range(1, 11)],
        )
        self.assertEqual(hw.transpose([[1], [2], [3]]), [[1, 2, 3]])
        self.assertEqual(
            hw.transpose([[i for i in range(j, j + 15)] for j in range(1, 3000)]),
            [[i for i in range(j, j + 2999)] for j in range(1, 16)],
        )

    # Exercise-16
    def test_reverse_gen(self):
        self.assertEqual(list(hw.reverse_gen([1, 2, 3, 4, 5])), [5, 4, 3, 2, 1])
        self.assertEqual(
            list(hw.reverse_gen(list(range(1, 1000)))), list(range(999, 0, -1))
        )
        self.assertEqual(
            list(hw.reverse_gen(list(range(1, 2000)))), list(range(1999, 0, -1))
        )
        self.assertEqual(list(hw.reverse_gen([1])), [1])
        self.assertEqual(
            list(hw.reverse_gen(list(range(1, 3000)))), list(range(2999, 0, -1))
        )

    # Exercise-17
    def test_group_by_length(self):
        self.assertEqual(
            hw.group_by_length(["hello", "world", "python", "is", "fun"]),
            {5: ["hello", "world"], 6: ["python"], 2: ["is"], 3: ["fun"]},
        )
        self.assertEqual(
            hw.group_by_length(["a" * i for i in range(1, 1000)]),
            {i: [i * "a"] for i in range(1, 1000)},
        )
        self.assertEqual(
            hw.group_by_length(["a" * i for i in range(1, 2000)]),
            {i: [i * "a"] for i in range(1, 2000)},
        )
        self.assertEqual(hw.group_by_length(["a"]), {1: ["a"]})
        self.assertEqual(
            hw.group_by_length(["a" * i for i in range(1, 3000)]),
            {i: [i * "a"] for i in range(1, 3000)},
        )

    # Exercise-18
    def test_common_elements(self):
        self.assertEqual(hw.common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {3})
        self.assertEqual(
            hw.common_elements([[i for i in range(1, 1000)] for _ in range(10)]),
            set(range(1, 1000)),
        )
        self.assertEqual(
            hw.common_elements([[i for i in range(1, 2000)] for _ in range(20)]),
            set(range(1, 2000)),
        )
        self.assertEqual(hw.common_elements([[1] for _ in range(100)]), {1})
        self.assertEqual(
            hw.common_elements([[i for i in range(1, 3000)] for _ in range(30)]),
            set(range(1, 3000)),
        )

    # Exercise-19
    def test_primes_gen(self):
        self.assertEqual(list(hw.primes_gen(10)), [2, 3, 5, 7])
        self.assertEqual(list(hw.primes_gen(30)), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(
            list(hw.primes_gen(100)),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        )
        self.assertEqual(list(hw.primes_gen(1)), [])
        self.assertEqual(list(hw.primes_gen(2)), [2])

    # Exercise-20
    def test_list_to_dict(self):
        self.assertEqual(hw.list_to_dict(["a", "b", "c"]), {0: "a", 1: "b", 2: "c"})
        self.assertEqual(
            hw.list_to_dict(list(range(1, 1000))), {i: i + 1 for i in range(999)}
        )
        self.assertEqual(
            hw.list_to_dict(list(range(1, 2000))), {i: i + 1 for i in range(1999)}
        )
        self.assertEqual(hw.list_to_dict(["a"]), {0: "a"})
        self.assertEqual(
            hw.list_to_dict(list(range(1, 3000))), {i: i + 1 for i in range(2999)}
        )


if __name__ == "__main__":
    unittest.main()