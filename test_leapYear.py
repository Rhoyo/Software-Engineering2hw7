import leapYear
import unittest

def test_input():
	assert(leapYear.leap(-2004)==1)


class leapTest(unittest.TestCase):
	
	def test_type(self):
		self.assertIsInstance(2004, int)
		res=leapYear.leap(2004)

	def test_res(self):
		res=leapYear.leap(2004)	
		self.assertEqual(res,0)
