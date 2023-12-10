import unittest
import day13

test_data = day13.read_text_file(f"13_test.txt")

class TestMethods(unittest.TestCase):

    def test_cop(self):

        self.assertTrue(day13.co_prime(7, 8))

    def test_crt1(self):

        self.assertEqual(day13.crt([3, 5, 7], [2, 3, 2]), 23)

    def test_crt2(self):

        self.assertEqual(day13.crt([5, 11, 6], [0, 10, 4]), 10)

    def test_crt3(self):

        self.assertEqual(day13.crt([3, 4, 5], [1, 2, 3]), 58)

    def test_part2_1(self):
        self.assertEqual(day13.part_2(test_data), 1068781)

    def test_part2_2(self):
        self.assertEqual(day13.solve_busses("17,x,13,19"), 3417)
    def test_part2_3(self):
        self.assertEqual(day13.solve_busses("67,7,59,61"), 754018)
    def test_part2_4(self):
        self.assertEqual(day13.solve_busses("67,x,7,59,61"), 779210)
    def test_part2_5(self):
        self.assertEqual(day13.solve_busses("67,7,x,59,61"), 1261476)
    def test_part2_6(self):
        self.assertEqual(day13.solve_busses("1789,37,47,1889"), 1202161486)
    def test_part2_7(self):
        self.assertEqual(day13.solve_busses("10, 11"), 10)
    def test_part2_8(self):
        self.assertEqual(day13.solve_busses("5, 11, 6"), 10)

if __name__ == '__main__':
    unittest.main()