import data_processor
import plotter
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='This script can uses functions from libraries numpy, pandas, and matplotlib to create matrices, '
                    'write them into files, get matrix dimensions, and plot data from the Iris dataset provided'
    )
    parser.add_argument(
        '-nr',
        '--num_rows',
        type=int,
        help='number of rows in the matrix'
    )
    parser.add_argument(
        '-nc',
        '--num_columns',
        type=int,
        help='number of columns in the matrix'
    )
    parser.add_argument(
        '-i_d',
        '--iris_data',
        type=str,
        help='file path for iris data'
    )
    parser.add_argument(
        '-ofp',
        '--output_filepath',
        type=str,
        default='matrix.csv',
        help='output filepath for matrix'
    )

    args = parser.parse_args()

    print('Matrix Creation')
    print(data_processor.get_random_matrix(args.num_rows, args.num_columns))
    print('\nWriting matrix into file')
    data_processor.write_matrix_to_file(args.num_rows, args.num_columns, args.output_filepath)
    print('Done, check your directory for the matrix CSV file \n \n')

    print('Dimensions of Iris data')
    print(data_processor.get_file_dimensions(args.iris_data))
    print('Plotting Iris data')
    plotter.plot_iris_data(args.iris_data)
    print('Done, check your directory for png files')
    exit()


if __name__ == "__main__":
    main()
