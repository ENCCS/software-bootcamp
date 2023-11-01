#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

# Create the main parser
parser = argparse.ArgumentParser(description='Math Operations')

# Create sub-parsers
subparsers = parser.add_subparsers(dest='operation', help='Available operations')

# Create a sub-parser for the 'add' operation
add_parser = subparsers.add_parser('add', help='Addition')
add_parser.add_argument('numbers', nargs='+', type=int, help='Numbers to add')

# Create a sub-parser for the 'subtract' operation
subtract_parser = subparsers.add_parser('subtract', help='Subtraction')
subtract_parser.add_argument('numbers', nargs='+', type=int, help='Numbers to subtract')

# Parse the command-line arguments
args = parser.parse_args()

# Process the selected operation

if args.operation == 'add':
	result = sum(args.numbers)
elif args.operation == 'subtract':
	result = args.numbers[0] - sum(args.numbers[1:])

print(result)
