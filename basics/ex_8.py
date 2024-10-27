try:
    answer = int(input("What number should i divinde 10 by: "))
    print(10/answer)
except ZeroDivisionError as e:
    print("Division by 0 not possible")
    print(e)
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)

finally:
    print("This code always runs!")