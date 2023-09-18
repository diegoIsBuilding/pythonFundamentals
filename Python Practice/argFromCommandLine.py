#Accepting Arguements
#import sys #this library provides various functions and variables that are used 
           #to manipultate different parts of the python runtime evnironment 

#First print all the arguments that passed into the file?
#name = sys.argv[1]
#print(f'Hello {name}')

#Other method that helps
import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)
#proceed by writing function that accepts arguments
parser.add_argument('-c', '--color', metavar='color', required=True, choices = {'red', 'yellow'}
                    help='The color to search for')
args = parser.parse_args()

print(args.color)
#Got an error -- a file was previously name enum.py which caused a circular import
#Python attempts to import from the local file instead of from the standard library
#causing a circular import issue
#renamed the enum.py file to enum2.py and the program worked

#In the command line when an argument is not specified the following error 
#pops up- 'the following arguments are required '-c/--color'