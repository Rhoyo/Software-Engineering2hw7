import unittest
import fizzBuzz

class testFizz(unittest.TestCase):	
	def test_fizz(self):
		res=fizzBuzz.fizzBuzz(3)
		self.assertEqual(res, 0)
	
	def test_buzz(self):
		res=fizzBuzz.fizzBuzz(5)
		self.assertEqual(res, 2)

	def test_fizzBuzz(self):
		res=fizzBuzz.fizzBuzz(15)
		self.assertEqual(res, 3)

