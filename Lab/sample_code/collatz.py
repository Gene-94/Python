
def collatz(number):
    if((number % 2) == 0):
        return number // 2
    else:
        return 3 * number + 1

print("\n\t# The Collatz Program #")
while(1):
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Not a number! please insert a valid integer.")
while num != 1: 
    num = collatz(num)
    print(num)
    
