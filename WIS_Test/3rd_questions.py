import math
def prime_number_test(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
            return True
a = int(input("Enter the number you want to check: "))
print(prime_number_test(a))
