#Purpose: Lab 9B
#   Program Name:MONTHLY SALES
#   Exercise:
#    1.Create a program that allows you to view and edit the sales amounts for each month of the current year.
#
#   Author: Kiara Lindsey
#   Date: October 23, 2020
# a file in the current directory
FILENAME = "monthly_sales.txt"


def write_sales(sales):
    # your code to open the file in write mode and store the sales dictionary items into the file
    with open(FILENAME,"w") :
        for month, amount in sales():
         file.write(month + str(amount))
def read_sales():
    # your code to open the file in read mode and read the file items into the sales dictionary
    with open(FILENAME, "r") as file:
        sales = {}
        for line in file:
            line = line.replace("\n","")
            sales =line.split("\t")
        return sales

def view_month(sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in sales:
        name = sales[month]
        print("Sales amount for"+ name +"is .\n")
    else:
        print("Invalid three-letter month.\n")
    # your code to find the month entered in sales dictionary – if found, print month and sales amount – if not found, print “Invalid three-letter month”


def edit_month(sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in sales:
        amount = int(input("Sales Amount: "))
        sales[month] = amount #I keep getting an error here
        print("Sales amount for"+name +"is{:,2f} .\n")
    else:
        print("Invalid three-letter month.")
    # your code to find month entered in sales dictionary – if found, edit sales amount and write amount to file – if not found, print “Invalid three-letter month”

def view_year(sales):
    totals = 0.0
    for month, amount in sales():
      totals += amount
    return totals

# your code to  calculate yearly total and monthly average of all items in sales Dictionary and print output


def display_menu():
    print("COMMAND MENU")
    print("view   - View sales for specified month")
    print("edit   - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit   - Exit program")
    print()


def main():
    print("Monthly Sales program")
    print()

    sales = read_sales()
    display_menu()
    while True:
        command = input("Command: ")
        if command == "view":
            view_month(sales)
        elif command == "edit":
            edit_month(sales)
        elif command == "totals":
            view_year(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()

