# logic
''' Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13
'''

num = int(input("enter a number\n"))
fib_series = [0, 1]

if num <= 0:
    print("Sorry, fib_series does not exist for negative numbers")
elif num == 0:
    print("The fib_series of 0 is 0")
else:
    for i in range(2, num):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    print(f"{fib_series}", end="\t")

