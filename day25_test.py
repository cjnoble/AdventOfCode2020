import unittest
import day25

#test_data = day13.read_text_file(f"13_test.txt")

class TestMethods(unittest.TestCase):

    def testloopsize(self):

        self.assertEqual(day25.loop_size(5764801), 8)
        self.assertEqual(day25.loop_size(17807724), 11)

    def test_part1(self):

        self.assertEqual(day25.part_1(5764801, 17807724), 14897079)


if __name__ == '__main__':
    unittest.main()