seconds = int(input("Enter seconds: "))

temp = seconds
days = temp//(60*60*24)
temp = temp - days*60*60*24

hours = temp//(60*60)
temp = temp - hours*60*60

minutes = temp//(60)
temp = temp - minutes*60

print(seconds, "seconds =", days, "days",hours, "hours", minutes, "minutes", temp, "seconds")