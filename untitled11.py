today = int(input("What day of the week is today? (as a number) "))
days_later = int(input("How many days later do you want to go? "))

result_day = (today + days_later -1)%7 + 1

print("In", days_later, "days it will be the", result_day, "th day of the week.")
