import unittest 
from unittest.mock import patch
from overlaps import overlaps
from versionstring import *


class TestOverlaps(unittest.TestCase):
    def testpositive(self):
        self.assertEqual(overlaps((1,5),(2,6)),True)
    
    def testnonoverlapvalue(self):
        self.assertEqual(overlaps((1,5),(6,9)),False)

    def testnegativevalue(self):
        self.assertEqual(overlaps((-5,-1),(-4,4)),True)

    def testzerovalue(self):
        self.assertEqual(overlaps((0,0),(0,0)),True)

    def testzeroandnegativevalue(self):
        self.assertEqual(overlaps((-4,0),(0,10)),True)

class Testversionstring(unittest.TestCase):
                              
    def testpositiveversion(self):
        self.assertMultiLineEqual(greateststringcal(4.0,2.0),'4.0 is greater than 2.0')

    def testlesserversion(self):
        self.assertMultiLineEqual(greateststringcal(2.1,4.0),'2.1 is lesser than 4.0')

    def testnotafloatvalue(self):
       self.assertMultiLineEqual(greateststringcal(4,2),'4 is greater than 2')

    def testequalversion(self):
        self.assertMultiLineEqual(greateststringcal(5.0,5.0),'5.0 is Equal to 5.0')

    def testnotfloatequalversion(self):
        self.assertMultiLineEqual(greateststringcal(4,4),'4 is Equal to 4')

#    @patch('versionstring.inputvalues.get_input', return_value=2.0)
#   def testinputvaluesversion(self):
#        self.assertMultiLineEqual(inputvaluevalidation(),'2.0 is Equal to 2.0')


if __name__ =='__main__':
    unittest.main()

    

        

