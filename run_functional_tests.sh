#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run matrix_library_tests python3 functional_tests.py 2 2 "matrix.csv" "iris.data"
assert_exit_code 0