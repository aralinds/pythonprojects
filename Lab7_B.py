#Purpose: Lab7-B
#   Program Name: ARRIVAL TIME ESTIMATOR
#   Exercise:
#    1.Create a program that calculates the estimated duration of a trip in hours and minutes.
#    This should include an estimated date/time of departure and an estimated date/time of arrival.
#
#   Author: Kiara Lindsey
#   Date: October 17, 2020


from datetime import datetime, timedelta

import locale

def main():
    print("Arrival Time Estimator")
    print()

    while True:
        # get departure date/time
        dep_date_str = input("Estimated date of departure (YYYY-MM-DD): ")
        dep_time_str = input("Estimated time of departure (HH:MM AM/PM): ")

        # convert str to datetime
        dep_str = dep_date_str + " " + dep_time_str
        # your code to use strptime to convert input to datetime variable goes here
        dep_date = datetime.strptime(date,"%Y-%m-%d")
        return dep_date
        departure_time = datetime.strptime(time, "%I:%M %p")
        return departure_time
        continue


# get miles / mph
def get_miles():
        miles = int(input("Enter miles: "))
        miles = int(miles)
        return miles
def get_miles_per_hour(): #keep getting an indent error?? but when indented, still have an error??
    miles_per_hour = int(input("Enter miles per hour: "))
    mph = int(miles_per_hour)
    return mph

# your code to perform calculations or hours and minutes goes here
def calculate(dep_date,dep_time,mph,miles):
    hours = int(miles/mph)
    minutes = int(((miles/mph)-hours)*60)
    # your code to use timedelta to find the travel time and then arrival time goes here
    travel_time = timedelta(hours = hours, minutes = minutes)
    arrival = datetime.strptime("AM", "%I:%M %p")
    arrival_time = (arrival- departure_time) + timedelta(
        days=1)




# display travel time and eta
print("Estimated travel time")
print("Hours:", hours)
print("Minutes:", minutes)
# your code to use strftime to print estimated date and time of arrival in proper format goes here
print("Estimated date of arrival: ", arrival_date.strftime("%Y-%m-%d"))
print("Estimated time of arrival:", arrival_time.strftime("%I:%M %p"))
print()

# ask if user wants to continue
result = input("Continue? (y/n): ")
print()
if result.lower() != "y":
    miles = get_miles()
    mph = get_miles_per_hour()
    calculate(dep_date, dep_time, mph, miles)
    print("Bye!")
    break

if __name__ == "__main__":
    main()



