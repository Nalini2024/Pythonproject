# Take user input and print the table

a = int(input("enter the number to print the table \n"))
# print(f"{a} * 1 = {a*1}")
# print(f"{a} * 2 = {a*2}")
# print(f"{a} * 3 = {a*3}")
# print(f"{a} * 4 = {a*4}")
# print(f"{a} * 5 = {a*5}")
# print(f"{a} * 6 = {a*6}")
# print(f"{a} * 7 = {a*7}")
# print(f"{a} * 8 = {a*8}")
# print(f"{a} * 9 = {a*9}")
# print(f"{a} * 10 = {a*10}")

for i in range(1,11):
    print(f"{a} * {i} = {a * i}")