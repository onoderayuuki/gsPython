import unittest

if __name__ == "__main__":
    unittest.main()

class MyTest (unittest.TestCase):
    def test_do_somthing(self):
        one = 1
        self.assertEqual(one,1,"one is 1s")