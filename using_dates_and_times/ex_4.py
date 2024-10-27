import calendar

def main():
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(2022,1)
    print(str)


    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    str = hc.formatmonth(2022,1)
    print(str)


    for i in c.itermonthdays(2022,8):
        print(i)
    
    for name in calendar.month_name:
        print(name)
    for day in calendar.day_name:
        print(day)


    print("Team meetings will be on: ")
    for m in range(1,13):
        cal = calendar.monthcalendar(2022,m)
        weekone = cal[0]
        weektwo = cal[1]
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print(calendar.month_name[m],meetday) 

if __name__ == "__main__":
    main()