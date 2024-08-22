'''FizzBuzz Test: Write a program that prints numbers from 1 to 100.
# Loop For However, for multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."'''

# logic
'''number /3>> "frizz
   number/5>>> buzz
    number/3 and 5>>>frizzbuzz'''

#number = int(input("Enter a number from 1 to 100 "))
#print(number)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
       print(f" {number} is Multiple of 3 and 5 ---> FrizzBuzz")
    elif number % 3 == 0:
       print(f" {number} is Multiple of 3 ---> Frizz")
    elif number % 5 == 0:
       print(f" {number} is Multiple of 5 ---> Buzz")