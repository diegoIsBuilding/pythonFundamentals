#Functions Review

#Keyword to define a function is def followed by the name of the function
#Fucntions promote code reuse
#Arguements can be passed into a function
def hello_world(worlds):
    #Body of the function
    #Can be the instructions
    print(f'Hello {worlds}')

hello_world('Earth')
hello_world('Mars')

#Can also set a default argument value
def hello_friend(name='My Friend'):
    print(f'Hello {name}')
    
hello_friend('Geoff') #Returns - Hello Geoff
hello_friend() #Returns - Hello My Friend

#Can also pass in multiple parameters
def hola(name, age):
    print(f'Hello {name}, you are {str(age)} years old')
    
hola('Daisy', 1)
