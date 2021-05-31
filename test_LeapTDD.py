import unittest
import leapTDD

class testLeap(unittest.TestCase):	
	def test_div4(self):
		res=leapTDD.leap(2004)
		self.assertEqual(res, 0)
	
	def test_div4not100(self):
		res=leapTDD.leap(2100)
		self.assertEqual(res, 1)

	def test_div4not100unless400(self):
		res=leapTDD.leap(2400)
		self.assertEqual(res, 0)

	
