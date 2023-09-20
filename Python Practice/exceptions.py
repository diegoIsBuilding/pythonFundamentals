#Exceptions
#Exception handling - wrap blocks of code in a try 

#Example
#try:
    #Lines of code
#    except #Error 1
    #handle error
#    except #Error 2
    #handle error
    
#else: 
    #no exceptions were raised the code ran successfilly
    
#finally:
    #do something in any case

#Example - Dividing by Zero
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot Divide by zero')
finally:
    result = 1

print(result)


    