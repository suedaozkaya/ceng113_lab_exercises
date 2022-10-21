int_number = int(input("Enter an integer: "))

temp = int_number

ones = int_number%10
temp = temp//10

tens = temp%10
temp = temp//10

hundreds = temp%10
temp = temp//10

thousands = temp%10

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)
print("Thousands:", thousands)

