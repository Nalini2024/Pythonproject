'''Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.'''

# logic
'''cond1:Year divisible by 4= leap year
   year not divisible by 4= not a leap year
   cond2:year  not divisible by 100= leap year
   year divisible by 100 = not a leap year
   cond3:year divisible by 400= leap year
   Year not divisible by 400= not a leap year'''

Year = int(input("Enter an year "))

if Year % 4 == 0 and Year % 100 != 0:
    print(f"Leap year: {Year}")
    print(f"Enter Year {Year} is a Leap Year")

elif Year % 400 == 0:
    print(f"Leap year: {Year}")
    print(f"Enter Year {Year} is a Leap Year")

else:
    print("Not a Leap Year", Year)
    print(f"Enter Year {Year} is Not a Leap Year")
