import sys
import numpy as np
import pandas as pd

np.random.seed(5)


def get_random_matrix(num_rows, num_columns):
    """Generate a N x M matrix of random floating point numbers sampled from a uniform range of (0,1]

    :param num_rows: integer
        number of rows in the matrix
    :param num_columns: integer
        number of columns in the matrix

    :return: a numpy array of user specified dimensions
    """
    # ensure row and column numbers are int
    if not isinstance(num_rows, int):
        raise TypeError("num_rows must be of type integer")
    if not isinstance(num_columns, int):
        raise TypeError("num_columns must be of type integer")

    # ensure there are 1 or more rows and columns
    if num_rows < 1:
        raise ValueError("There must be at least 1 row")
    if num_columns < 1:
        raise ValueError("There must be at least 1 column")

    # generate matrix
    matrix = np.random.randn(num_rows, num_columns)

    return matrix


def get_file_dimensions(file_name):
    """take a CSV file path and return the number of rows and columns

    :param file_name: string
        file path to CSV file

    :return: tuple containing file dimensions
    """
    # make sure file path is a string
    if not isinstance(file_name, str):
        raise TypeError("file path must be a string")

    f = open(file_name, "r")
    rows = 0
    columns = 0

    # for every line in the file
    for line in f:
        # if line is not empty count row
        if line != "\n":
            rows += 1

        # if number of columns has not been found
        if columns == 0:
            line = line.rstrip().split(",")
            columns = len(line)

    f.close()

    # ensure columns and rows have been detected
    if (rows, columns) == (0, 0):
        print("no rows or columns found")
        sys.exit(1)
    if rows == 0:
        print("no rows found")
        sys.exit(1)
    if columns == 0:
        print("no columns found")
        sys.exit(1)

    return rows, columns


def write_matrix_to_file(num_rows, num_columns, file_name):
    """writes a N x M matrix as a CSV file using user defined row and column numbers

    :param num_rows: integer
        number of rows
    :param num_columns: integer
        number of columns
    :param file_name: string
        output file name

    :return: None
    """
    # ensure file path is a string
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string")

    # create matrix
    matrix = get_random_matrix(num_rows, num_columns)

    # write matrix into a file
    matrix_df = pd.DataFrame(data=matrix.astype(float))
    matrix_df.to_csv('matrix.csv',
                     sep=',',
                     header=False,
                     float_format='%.2f',
                     index=False)

    return None

