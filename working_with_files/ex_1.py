def main():
    myfile = open("textfile.txt","w+")
    myfile = open("textfile.txt","a+")
    for i in range(10):
        myfile.write("This is some new text\n")
    myfile = open("textfile.txt","r")
    if myfile.mode == 'r':
        content = myfile.read()
        print(content)
        fl = myfile.readlines()
        print(fl)
        for x in fl:
            print(x)
    # myfile.close()
if __name__ == "__main__":
    main()