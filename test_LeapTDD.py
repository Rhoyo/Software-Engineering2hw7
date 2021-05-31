import unittest
import leapTDD

 class testLeap(unittest.TestCase):	
	def test_div4(self):
		res=leapTDD.leap(2004)
		self.assertEqual(res, 0)
	
	
