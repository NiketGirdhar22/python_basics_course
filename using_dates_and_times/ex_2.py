from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("The current year is: %y"))

    print(now.strftime("%a, %d %B, %y"))
    
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local date: %x"))
    print(now.strftime("Local time: %X"))

    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24 Hr time time: %H:%M:%S"))


if __name__ == "__main__":
    main()