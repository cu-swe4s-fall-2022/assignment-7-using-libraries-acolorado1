import unittest
import random
import numpy as np
import data_processor


random.seed(5)


class MyTestCase(unittest.TestCase):
    def test_get_random_matrix(self):
        rand_row = random.randint(1, 100)
        rand_column = random.randint(1, 100)
        matrix = data_processor.get_random_matrix(rand_row, rand_column)

        self.assertEqual(np.shape(matrix), (rand_row, rand_column))
        self.assertRaises(TypeError, data_processor.get_random_matrix, "1", 1)
        self.assertRaises(ValueError, data_processor.get_random_matrix, 1, -1)

    def test_get_file_dimensions(self):
        known_dim = data_processor.get_file_dimensions("iris.data")

        self.assertEqual(known_dim, (150, 5))
        self.assertRaises(TypeError, data_processor.get_file_dimensions, 2)

    def test_write_matrix_to_file(self):
        self.assertRaises(
            TypeError, data_processor.write_matrix_to_file, 2, 2, ["file.csv"]
        )
        self.assertRaises(
            TypeError, data_processor.write_matrix_to_file, "1", 2, "mat.csv"
        )
        self.assertRaises(
            ValueError, data_processor.write_matrix_to_file, 2, 0, "write.csv"
        )


if __name__ == "__main__":
    unittest.main()
