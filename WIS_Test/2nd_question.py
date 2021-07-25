def fibonacci_seq(value):
    if(value < 0):
        print("Please re-enter positive value")
    if (value == 0):
        return False
    if (value == 1):
        return 1
    fibonacci = [1,1]
    for i in range(2, value):
        fibonacci.append(fibonacci[i - 1]+ fibonacci[i - 2])
    return fibonacci
a = int(input("Input your desired number to print in the Fibonacci sequence: "))
print(fibonacci_seq(a))