age = 26
#Regular Format
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
#Ternary Format
def is_adult_ternary(age):
    return True if age > 18 else False

print(is_adult(age))
print(is_adult_ternary(age))