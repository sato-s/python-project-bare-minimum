import unittest
from target import Target

class TestTarget(unittest.TestCase):
    def test_token(self):
        self.assertEqual(Target().token, 'aaa')

    def test_token2(self):
        self.assertEqual(Target().token2, '2nd aaa')


if __name__ == '__main__':
    unittest.main()
