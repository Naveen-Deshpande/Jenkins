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

	def test_sub(self):
		num1 = 50
		num2 = 20
		result = num_op.sub_num(num1,num2)
		self.assertEqual(result,30)


if __name__ == '__main__':
	unittest.main()