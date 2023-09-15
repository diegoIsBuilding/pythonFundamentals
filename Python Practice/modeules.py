#consider a module to be the same as a code library 
#a containing a set of functions you want to include in your app

#save the code I want in a file with the .py extension 
#Example - classes.py

#Now the code in the classes.py file can be accessed by using the 
#import satement/keyword

#Example
#import classes

#classes.function('Some parameter')

#One file is the entry point
import mod
mod.handshake() #Returns shake hands

#Can also bring over specific functions from different files
from mod import handshake
handshake() #Returns shake hands

from lib import math
math.addition(1, 2) #Returns 3

from lib.math import addition
addition(3, 100)

#Example of Python modules you can access
#math for math utilities
#re for regular expressions
#json to work with json
#datetime
#sqlites3
#os
#random
#statistics
#requests
#http
#urllib

import math 

print(math.sqrt(4))

from math import sqrt
print(sqrt(4))