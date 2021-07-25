def convert_number(n, b):
    if (n < 0 or b < 2 or b > 32):
        return "";

    sb = "";
    m = 0;
    remainder = n;

    while (remainder > 0):
        if (b > 10):
            m = remainder % b;
            if (m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return "".join(reversed(sb));


n = int(input("Enter the positive integer n = "));
b=int(input("Enter the Body system b = "))
print("Body system of the integer", n, ":", convert_number(n, b))