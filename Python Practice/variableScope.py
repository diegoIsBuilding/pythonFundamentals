#Variable Scope
#Example - Local Scope
#A variable created inside of a function belongs to the local scope of that
#function and can only be used inside that function
def localScopeFunction():
    localScopeVariable = 'This variable only prints inside this function'
    print(localScopeVariable)
    
localScopeFunction() #Returns the print statement in the function
#print(localScopeVariable) #Returns Error: the variable is not defined

#Function inside a function
#A variable created in the highest level of a function is available for 
#other function inside the parent function
#Example:

def parentFunction():
    parentVariabele = 'Parent Variable'
    def childFunction():
        print(f'{parentVariabele} is printing inside child function')
        
    childFunction()
parentFunction()

#Global Scope
#A variable created in the main body of the Python code is a global variable
#and belongs to the global scope
#Global variables are available from within any scope global or local

globalVariable = 'Gone Global!'
def mainFunction():
    print(f'The global variable is accessable in this mainFunction --> {globalVariable}')

mainFunction()
print(globalVariable)    

#Naming variables
#Having two variables with the same name one in the
# global scope and the other in the local scope of a function
#python will treat those variables as two seperate variables (not recommended)
#Example:
variable = 300
def newFunction():
    variable = 'Hello'
    print(variable)
    return
newFunction()
print(variable)

#Global Keyword
#If you need to create a global variable but stuck in local scope -use the 
#keyword: global
#global makes a variable global

def localFunction():
    global newGlobalVariable
    newGlobalVariable = 'NGV'
    return
localFunction()
print(newGlobalVariable)