import unittest
import num_op


class TestOperation(unittest.TestCase):

	# method to test addition operation
	def test_add(self):
		
		num1 = 10
		num2 = 5
		result = num_op.add_num(num1,num2)
		self.assertEqual(result, 15)

	def test_multiply(self):
		
		num1 = 10
		num2 = 2
		result = num_op.multiply_num(num1,num2)
		self.assertEqual(result, 20)


if __name__ == '__main__':
	unittest.main()