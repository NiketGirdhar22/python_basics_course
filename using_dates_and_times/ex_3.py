from datetime import date
from datetime import time
from datetime import datetime 
from datetime import timedelta

def main():
    print(timedelta(days=365,hours=5,minutes=1))
    now = datetime.now()
    print("Today is: ",now)
    print("one year from now it will be: ",now+timedelta(days=365))
    print("in 2 weeks and 3 days it will be: ",now+timedelta(weeks=2,days=3))
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d %Y")
    print("a week ago it was: ",s)

    now = date.today()
    afd = date(now.year,4,1)

    if afd<now:
        print("April Fool's day already went by: ",(now-afd).days)
        afd = afd.replace(year=now.year+1)
    time_to_afd = afd-now
    print("It is ",time_to_afd.days," days until next AFD")

if __name__ == "__main__":
    main()