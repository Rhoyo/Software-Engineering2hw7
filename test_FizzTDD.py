import unittest
import fizzBuzz

class testFizz(unittest.TestCase):	
	def test_fizz(self):
		res=fizzBuzz.fizzBuzz(3)
		self.assertEqual(res, 0)
