from unittest import TestCase
from main import array_diff_check


class Test(TestCase):
    def test_array_diff_check(self):
        list1 = (0, 1, 2, 3, 4, 5, 6, 7)
        list2 = (2, 1, 0, 3, 4, 5, 6, 7)
        list3 = (2, 1, 4, 3, 0, 5, 6, 7)

        result = array_diff_check(list1,list2)
        self.assertEqual(result, "arrays all good")

        result = array_diff_check(list1, list3)
        self.assertEqual(result,"needs more processing")

        result = array_diff_check(list1,list3,diff_items=3)
        self.assertEqual(result, "arrays all good")

