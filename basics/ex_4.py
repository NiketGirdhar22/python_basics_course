def main():
    x,y = 100,100
    if x<y:
        result = "x is less than y"
    elif x == y:
        result = "x is same as y"
    else:
        result = "x is greater than y"
    print(result)


    result = "x is less than y" if x<y else "x is greater than or equal to y"
    print(result)

    value = "one"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print(result)
if __name__ == "__main__":
    main()