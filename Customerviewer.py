class Customer:
    def __init__(self,cust_id,first_name,last_name,city,state,zip_code):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.zip_code = zip_code
    def getFullName(self):
        return (self.first_name + self.last_name ,cust_id)
    def getFullAddress(self):
        return (self.city,self.state,self.zip_code)
def main():
    print input(first_name,last_name,cust_id)
    print()
    print input(city,state,zip_code)
    print()
#??
#I wasn't sure where to put the input for user



if __name__ == "__main__":
    main()