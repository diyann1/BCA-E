num = 567
reversed_num = 50

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Number reversed: " + str(reversed_num))
