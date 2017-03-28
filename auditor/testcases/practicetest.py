
import unittest
from auditor.add import add

class Test(unittest.TestCase):

    def test_add(self):
        
        r = add().adding(op1=4, op2=5)
        self.assertEqual(r, 9)
unittest.main()
