#Purpose: Lab 9 A
#   Program Name:GREATEST COMMON DIVISOR
#   Exercise:
#    Create a program that finds the greatest common divisor of two numbers through recursive programming
#
#   Author: Kiara Lindsey
#   Date: November  2020
def main():
    print("Greatest Common Divisor")
    print()

    while True:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))

        if num1 < num2:
            print("Number 1 must be greater than number 2.Try again.")
            continue

        print("Greatest common divisor:", gcd(num1, num2))
        print()

        again = input("Continue? (y/n): ").lower()
        print()
        if again != "y":
            print("Bye!")
            break

# a recursive function
def gcd(x, y):
    #your code for the recursive function goes here.
    if (y==0 ):
        return x
    else:
        return gcd(y,x%y)

if __name__ == "__main__":
    main()
