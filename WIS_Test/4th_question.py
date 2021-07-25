output = []
input = [x for x in input("Enter binary numbers: ").split(",")]
for value in input:
    int_value = int(value, 2)
    if int_value % 5 == 0:
        output.append(value)
print(",".join(output))

