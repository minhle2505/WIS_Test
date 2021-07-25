def number_check(num):
    if num % 2 == 0:
        return "This is an even number"
    else:
        return "This is an odd number"
print(number_check(int(input("Enter the number: "))))
