import unittest
from lab2 import Money


class TestMoney(unittest.TestCase):
    test = Money(458)
    test_2 = Money(90.50)

    def test_add__(self):
        self.assertEqual(self.test.__add__(500), 958)
        self.assertEqual(self.test.__add__(10), 468)
        self.assertEqual(self.test_2.__add__(0.50), 91)
        self.assertEqual(self.test_2.__add__(500), 590.50)
        self.assertRaises(TypeError, self.test.__add__, 'abc')

    def test_sub__(self):
        self.assertEqual(self.test.__sub__(100), 358)
        self.assertEqual(self.test_2.__sub__(30), 60.50)
        self.assertTrue(self.test.__sub__(100),isinstance(self.test.__sub__(100),int))


    def test_mul__(self):
        self.assertEqual(self.test.__mul__(1), 458)
        self.assertEqual(self.test_2.__mul__(2),181)

    def test_div(self):
        self.assertRaises(ValueError, self.test.__truediv__,0 )
        self.assertEqual(self.test.__truediv__(2),229)

    def test_format(self):
        self.assertEqual(self.test.__format__('$'),'458 $')


if __name__ == '__main__':
    unittest.main()
