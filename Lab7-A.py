#Purpose: Lab7-A
#   Program Name: BIRTHDAY CALCULATOR
#   Exercise:
#    1. Create a program that accepts a name and a birth date and displays the person’s birthday,
#    the current day, the person’s age, and the number of days until the person’s next birthday.
#
#   Author: Kiara Lindsey
#   Date: October 17, 2020


from datetime import datetime, timedelta


def get_birth_date():
    birth_date_str = input("Enter birthday (MM/DD/YY): ")
    # your code to use strptime to properly format the entered birthdate and convert it to a datetime variable goes here
    birth_date = datetime.strptime(birth_date_str, "%m/%d/%Y")
    return birth_date
    print("Birthday: ",birth_date)



# if necessary, subtract 100 to fix birth year
current_year = datetime.now().year
if birth_date.year > current_year:
    fixed_birth_year = birth_date.year - 100
    birth_date = datetime(fixed_birth_year, birth_date.month, birth_date.day)
    #return birth_date keeps saying outside the function?


def main():
    print("Birthday Calculator")
    print()

    while True:
        name = input("Enter name: ")
        birth_date = get_birth_date()
        current_date = datetime.now()

        # your code to user strftime and convert entered dates to datetime variables and print them goes here.
        birth_date.strtime("%B %d,%Y")
        print ()



# your code to calculate and print the person’s age goes here
def calculate_age(born):
    if birthday > today:
        today.year - born.year - 1
    else:
        today.year-born.year
age = calculate_age(get_birth_date)
# your code to calculate and print days until person’s next birthday goes here
def calculate_dates():
    today = date.today
    birthday = date(today.year, get_birth_date)
    if today > birthday:
     next_year = today.year + 1
     birthday = date(next_year,get_birth_date)
days_until = (birthday - today).days
print(days_until,get_birth_date )
# ask if user wants to continue
print()
result = input("Continue? (y/n): ")
print()
if result.lower() != "y":
    print("Bye!")

if __name__ == "__main__":
    main()