def is_palindrome(number):
    for i in range(len(number)):
        if (number != number[::-1]):
            return False
        return True
print(is_palindrome(input("Insert your value: ")))
