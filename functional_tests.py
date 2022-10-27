import data_processor
import sys

nrow = sys.argv[1]
ncol = sys.argv[2]
output_file = sys.argv[3]
test_csv_data = sys.argv[4]

print('Testing matrix creation')
data_processor.get_random_matrix(nrow, ncol)

print('Testing get file dimensions')
data_processor.get_file_dimensions(test_csv_data)

print('Testing writing random matrix to a file')
data_processor.write_matrix_to_file(nrow, ncol, output_file)
