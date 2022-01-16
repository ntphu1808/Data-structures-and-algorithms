def factorial(number):
    if number == 1:
        return number
    return number*factorial(number-1)

giaithua=factorial(1)
print(giaithua)