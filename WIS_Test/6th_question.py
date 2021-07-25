x = int(input("enter the factorial number: "))
def factorial_cal(x):
    if x == 0:
        return 1
    return x * factorial_cal(x-1)
print(factorial_cal(x))