import unittest
import day18



class TestMethods(unittest.TestCase):


    def test_calc_part1_1(self):
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["1 + 2"])[0])[0], 3)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["1 + 2 * 3 + 4 * 5 + 6"])[0])[0], 71)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["1 + (2 * 3) + (4 * (5 + 6))"])[0])[0], 51)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["2 * 3 + (4 * 5)"])[0])[0], 26)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["5 + (8 * 3 + 9 + 3 * 4 * 3)"])[0])[0],  437)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"])[0])[0], 12240)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"])[0])[0], 13632)
        self.assertEqual(day18.calc_p1_ordering(['5', '+', '3', '*', '2', '*', '(', '9', '+', '6', '*', '6', '+', '9', ')', '*', '3'])[0], 4752)
        self.assertEqual(day18.calc_p1_ordering(day18.prep_data(["5 + 3 * 2 * (9 + 6 * 6 + 9) * 3"])[0])[0], 4752)

    def test_calc_part2(self):
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["1 + 2"])[0])[0], 3)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["1 + 2 * 3 + 4 * 5 + 6"])[0])[0], 231)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["1 + (2 * 3) + (4 * (5 + 6))"])[0])[0], 51)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["2 * 3 + (4 * 5)"])[0])[0], 46)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["5 + (8 * 3 + 9 + 3 * 4 * 3)"])[0])[0],  1445)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"])[0])[0], 669060)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["6 + 9 * 8 + 6"])[0])[0], 210)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)"])[0])[0], (210+6)*54)
        #self.assertEqual(day18.calc_p2_ordering([11664, "+",  "2",  "+",  "4",  "*", "2"])[0], 23340)
        self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"])[0])[0], 23340)
        #self.assertEqual(day18.calc_p2_ordering(day18.prep_data(["((9 + 6 * 4 * 4 * 7 * 5) + 3 * 5 * 7 * 2) * 9 + 9 * (3 * (8 * 2 * 9 * 2 * 5 + 8) + (7 * 2 * 7) * 2)"])[0])[0], 23340)

if __name__ == '__main__':
    unittest.main()