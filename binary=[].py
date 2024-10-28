binary=[]
amount=[8,4,2,1]
t=int(input("change what number"))

def check(num, leftover):
    if leftover-num>=0:
        leftover=leftover-num
        binary.append(1)
    else:
        binary.append(0)
    return leftover

for num in amount:
    t = check(num, t)
print("Your 4 bit binary code",binary)

# Extra Credit 1: Converting any positive integer
def convertAnyPositive(num):
    binary_any = []
#I keep devide by 2 and count remainder
    while num>0:
        binary_any.append(num%2)
        num=num//2 #this gives remainder
    binary_any.reverse() # it reverses
    print("Your positive integer in binary",binary_any)
convertAnyPositive(int(input("Enter any positive integer to convert")))

# Extra Credit 2: Convert binary string back to decimal
def binaryToDecimal(binary_string):
    decimal = 0
    tens_place = len(binary_string) - 1
    for digit in binary_string:
        decimal += int(digit) * (2 ** tens_place)
        tens_place -= 1
    print("Decimal equivalent:", decimal)
binaryToDecimal(int(input("Enter binary string to convert to decimal")))