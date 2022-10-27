# Using Libraries

## Description 
This script shows ways of using numpy, pandas, and matplotlib libraries. Specifically, it can generate a random matrix 
of user specified number of rows and columns, get the dimensions of a matrix, and write a matrix in a comma delimited 
formatted file. This script is also able to create three plots using the Iris data provided.   

## Workflow 

### Arguments 

Here is a list of required and optional arguments that can be accessed by typing **python .\UsingLibraries.py -h** from 
the terminal in the directory containing the *UsingLibraries.py* file.

```text
usage: UsingLibraries.py [-h] [-nr NUM_ROWS] [-nc NUM_COLUMNS] [-i_d IRIS_DATA] [-ofp OUTPUT_FILEPATH]

This script can uses functions from libraries numpy, pandas, and matplotlib to create matrices, write them into files, get matrix dimensions, and plot data from the Iris dataset provided

optional arguments:
  -h, --help            show this help message and exit
  -nr NUM_ROWS, --num_rows NUM_ROWS
                        number of rows in the matrix
  -nc NUM_COLUMNS, --num_columns NUM_COLUMNS
                        number of columns in the matrix
  -i_d IRIS_DATA, --iris_data IRIS_DATA
                        file path for iris data
  -ofp OUTPUT_FILEPATH, --output_filepath OUTPUT_FILEPATH
                        output filepath for matrix
```

### Inputs 

This script requires one type of input file containing the *iris.data*. The first 5 rows should be: 

```text
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5.0,3.6,1.4,0.2,Iris-setosa
```

### Command 

To run this program in the command line interface type: 

```text
python .\UsingLibraries.py \
        -nr 2 \
        -nc 4 \
        -i_d ".\iris.data" \
        -ofp ".\matrix.csv"
```

### Output 

This script will print the random matrix created as well as the dimensions of the iris data. In addition, 4 files will 
be created. 

The first will contain the matrix and will look like the following for a 2 x 4 matrix. 

```text
0.19,-0.33,-1.19,-0.20
-0.36,0.60,-1.66,-0.70
```

The following three outputs will be figures created from the iris data. They will be a boxplot, a scatter plot, and a 
merged figure of the two. For example: 

![Example Boxplot](https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-acolorado1/blob/1bc59afabfc4d127c025d99bc2c8e7919c90299b/iris_boxplot.png)

![Example Scatter Plot](https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-acolorado1/blob/1bc59afabfc4d127c025d99bc2c8e7919c90299b/petal_width_v_length_scatter.png)

![Example of Merged Plot](https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-acolorado1/blob/1bc59afabfc4d127c025d99bc2c8e7919c90299b/multi_panel_figure.png)

## Release History
+ 1.0 
  + ADD: random matrix generator 
  + ADD: function that outputs number of rows and columns from a CSV file 
  + ADD: function to create a CSV file containing a matrix 
  + ADD: function that will create a boxplot, scatter plot, and merged plot of the iris data
  + ADD: Unit and functional testing of data_processor functions 
  + ADD: Parser to run all functions and demonstrate library usage 

## Installation and Dependencies 

You must have Python 3 installed. Any Python 3 version should work, but it was written in Python 3.9 using a Windows-based 
operating system. Packages matplotlib 3.6.0, numpy 1.23.4, pandas 1.5.1 and argparse 1.4.0 will need to be installed. 

## Contact 

Angela Sofia Burkhart Colorado - angelasofia.burkhartcolorado@cuanschutz.edu




