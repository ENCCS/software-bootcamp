#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add two arguments (an integer and a float number)
parser.add_argument('--integer', type=int, required="an integer number")
parser.add_argument('--float', type=float, required="a float number")

# Parse the argument
args = parser.parse_args()

# data manipulation
result = args.integer * args.float

print('Result =', result)

