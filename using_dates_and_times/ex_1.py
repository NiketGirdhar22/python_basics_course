from datetime import date
from datetime import time
from datetime import datetime

def main():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    today = date.today()
    print("Today's date is :",today)
    print("Components of date: ",today.day, today.month,today.year)
    print("Today's weekday is ",today.weekday()," i.e. : ",days[today.weekday()])


    today = datetime.now()
    print("The current date and time is: ",today)

    t = datetime.time(today)
    print("The current time is: c",t)

if __name__ == "__main__":
    main()