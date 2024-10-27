def main():
    x=0
    while(x<5):
        print(x)
        x+=1

    for x in range(5,10):
        print(x)

    days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]

    for i in days:
        print(i)
    
    for i in range(5,10):
        if i==7:
            break
        if i%2 == 0:
            continue
        print(i)

    for i,d in enumerate(days):
        print(i,d)

if __name__ == "__main__":
    main()