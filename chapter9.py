import subprocess

#subprocess.call('/bin/date')

# subprocess.call('/bin/date "+%A %d %m %Y"', shell=True)

# subprocess.call('ls *.ipynb |wc -l', shell=True)

# name = 'Peter'
# subprocess.call('echo ' + name, shell=True)

# not safe! don't pass user supplied data to the shell
# name = '; rm exons.txt'
# subprocess.call('echo ' + name, shell=True)

# name = 'Peter'
# subprocess.call(['echo', name])

# subprocess.call(['ls', 'dna.txt'])

# this will not work - the '*' is not seen as a pattern
# subprocess.call(['ls', '*.ipynb'])

# import os

# notebooks = []
# for filename in os.listdir():
#     if filename.endswith('.ipynb'):
#         notebooks.append(filename)

# cmd = ['ls'] + notebooks
# subprocess.call(cmd)

# return_code = subprocess.call(['ls', '*.ipynb'])
# print('return_code', return_code)

# current_month = subprocess.check_output('/bin/date +%B', shell=True)
# print("Current month:", current_month)
# current_month_str = current_month.rstrip().decode()
# print("Current month:", current_month_str)
# current_month_str = current_month.rstrip().decode('utf-8')
# print("Current month:", current_month_str)

# print("Types of string: ByteString ", type(current_month), " and normal str String:", type(current_month_str))

# the equivalent of the shell > errors.txt
# error_file = open('errors.txt', 'w')
# subprocess.call(['ls', '*.ipynb'], stderr=error_file)
# error_file.close()

# error_file = open('errors.txt', 'w')
# output_file = open('output.txt', 'w')
# subprocess.call(['ls', 'dna.txt'], stdout=output_file, stderr=error_file)
# error_file.close()
# output_file.close()


# output = subprocess.check_output(['ls', '*.ipynb'])
# print("output:", output)

# reading user input
# number1_str = input("Enter a number: ")
# number2_str = input("Enter another number: ")
# number1 = int(number1_str)
# number2 = int(number2_str)
# print("Added", number1, "+", number2, "result", number1 + number2)

# import sys

# the magic sys.argv list contains the name of our program and 
# our command line parameters
# print("sys.argv:", sys.argv)

# if len(sys.argv) != 3:
#     sys.exit("Error: expected 2 parameters on the command line")
    
# number1_str = sys.argv[1]
# number2_str = sys.argv[2]
# number1 = int(number1_str)
# number2 = int(number2_str)
# print("Added", number1, "+", number2, "result", number1 + number2)

# import argparse

# parser = argparse.ArgumentParser(description='Add two numbers')
# parser.add_argument('number1', type=int, help='First number')
# parser.add_argument('number2', type=int, help='Second number')
# args = parser.parse_args()

# number1 = args.number1
# number2 = args.number2
# print("Added", number1, "+", number2, "result", number1 + number2)

import argparse

parser = argparse.ArgumentParser(description='Add two numbers')
# if the optional --multiply is there, store the value True
# else use the default, which is False, for the value of the multiply parameter
parser.add_argument('--multiply', action='store_true', default=False)
parser.add_argument('number1', type=int, help='First number')
parser.add_argument('number2', type=int, help='Second number')
args = parser.parse_args()

number1 = args.number1
number2 = args.number2
if args.multiply:
    result = number1 * number2
else:
    result = number1 + number2
    
print("Result", result)
