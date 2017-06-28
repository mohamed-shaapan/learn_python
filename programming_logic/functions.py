def factorial(number):
    "obtains the value of factorial(number)"
    if number==0 :
        return 1
    else:
        return number*factorial((number-1))

number=5 #input("enter your number : ")
print(factorial(number))