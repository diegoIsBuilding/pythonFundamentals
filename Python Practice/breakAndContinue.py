#Break and Continue Loops
#Break - Stops the loop all together
#Continue - tells python to stop the current iteration and to start the next one

#Example
items = [1, 2, 3, 4, 5]
for item in items:
    if item == 2:
        continue
    print('Prints after continue')