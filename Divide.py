a = int(input("Enter the number to dividend:"))
b = int(input("Enter the number divisor:"))

while b !=0:
    if a % b ==0:
        print("Dividend is mulitple of divisor", float(a/b))
    elif a % b != 0:
        print("Dividend is not a mulitple of divisor", float(a/b))
    break
if b ==0:
    print("The divisor is 0, divison not possible")