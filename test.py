# test


def divide(a, b):
    print("dividing", a, "by", b)
    result = a / b
    print("Result is", result)

    return result

try:
    print("Before calling divide")
    divide(10, 0)
    print("After calling divide")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division was successful")
finally:
    print("Finished Division operation")



#try:
    #print(divide(10, 2)) # output: 5.0
   # print(divide(10, "one")) # This will raise a ZeroDivisionError
#except ZeroDivisionError:
    #print("Second parameter cannot be zero")
#except :
    #print("An unexpected error occurred")