import unittest
from addnumbers import addnumbers

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addnumbers(2, 3), 5)
        self.assertEqual(addnumbers(-1, 1), 0)
        self.assertAlmostEqual(addnumbers(2.5, 3.1), 5.6)

if __name__ == "__main__":
    unittest.main()