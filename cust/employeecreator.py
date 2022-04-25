class Person:
    def __init__(self,first_name,last_name,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def getFullName(self):
        return self.first_name + last_name
class Customer(Person):
    def __init__(self,first_name,last_name,email,customer_number):
        Person.__init__(self,first_name,last_name,email)
        self.customer_number = customer_number
class Employee(Person):
    def __init__(self,first_name,last_name,email,ssn):
        Person.__init__(self, first_name, last_name, email)
        self.ssn = ssn
 def show_choice(Person):

        if isinstance(Person, Customer):
            print("CUSTOMER"/n ,Person,customer_number)
        if isinstance(Person, Employee):
            print("EMPLOYEE"/n , Person,ssn)
def main():
    print("Customer/Employee Data Entry")
    print("Customer or Employee? (c/e): ").lower()
    while True:
        print("First name: ",first_name)
        print("Last name: ", last_name)
        print("Email: ", email)
        print("Number: ", first_name)


    # ??
    again = input("Continue? (y/n): ").lower()
    print()
    if again != "y":
        break


print("Bye!")
if __name__ == "__main__":
    main()