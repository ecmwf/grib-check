import unittest
from KeyValue import KeyValue

class TestIndexedLookupTable(unittest.TestCase):
    def test_init(self):
        a = KeyValue("a", 5)
        self.assertEqual(str(a), "a(5)")

    def test_op(self):
        a = KeyValue("a", 5)
        b = KeyValue("b", 10)
        c = KeyValue("c", 15)
        
        x = a + b
        self.assertEqual(x.key(), "a(5) + b(10)")
        self.assertEqual(x.value(), 15)

        x = a - b
        self.assertEqual(x.key(), "a(5) - b(10)")
        self.assertEqual(x.value(), -5)

        x = c % 10
        self.assertEqual(x.key(), "c(15) % 10")
        self.assertEqual(x.value(), 5)

        x = -a
        self.assertEqual(x.key(), "-(a(5))")
        self.assertEqual(x.value(), -5)

    def test_parentheses(self):
        a = KeyValue("a", 5)
        b = KeyValue("b", 10)
        c = KeyValue("c", 15)

        x = a + b * c
        self.assertEqual(x.key(), "a(5) + b(10) * c(15)")
        self.assertEqual(x.value(), 5 + 10 * 15)

        x = (a + b) * c
        self.assertEqual(x.key(), "(a(5) + b(10)) * c(15)")
        self.assertEqual(x.value(), (5 + 10) * 15)

        x = (a + b) % 10
        self.assertEqual(x.key(), "(a(5) + b(10)) % 10")
        self.assertEqual(x.value(), (5 + 10) % 10)
        
        x = -(a + b)
        self.assertEqual(x.key(), "-(a(5) + b(10))")
        self.assertEqual(x.value(), -(5 + 10))
            
if __name__ == '__main__':
    unittest.main()
