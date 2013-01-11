#!/bin/bash


echo "pypy openssl_des"
time -p pypy _benchmark.py openssl_des > /dev/null
#echo "pypy my_des"
#time -p pypy _benchmark.py my_des > /dev/null
echo "pypy py_des"
time -p pypy _benchmark.py pydes > /dev/null

echo "python openssl_des"
time -p python _benchmark.py openssl_des > /dev/null
#echo "python my_des"
#time -p python _benchmark.py my_des > /dev/null
echo "python py_des"
time -p python _benchmark.py pydes > /dev/null


