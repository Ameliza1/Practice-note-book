# Creating a function that can calculate  factorial of a positive integer
# In everyday calculation factorial(n) = n*(n-1)*(n-2)*(n-3)*...*3*2*1
#method 1
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    while num > 0:
        return num*(num-1)
result3 = factorial(5)
print(result3)

#method 2
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    
    fact = 1
    counter = 1
    while counter <= num:
        fact = fact * counter
        counter = counter + 1
    return fact

