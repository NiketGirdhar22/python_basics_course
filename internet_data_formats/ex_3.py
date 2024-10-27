from html.parser import HTMLParser

paragraph = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print("Encountered a comment: ",data)
        pos = self.getpos()
        print("At line: ",pos[0]," and the character position: ",pos[1])
        print("----------------------------------------------\n")

    def handle_starttag(self,tag,attrs):
        print("Encountered a start tag: ",tag)
        pos = self.getpos()
        print("At line: ",pos[0]," and the character position: ",pos[1])
        print("----------------------------------------------\n")

        global paragraph
        if tag == 'p':
            paragraph += 1
        
        if len(attrs) > 0:
            print("Attributes: ")
            for a in attrs:
                print("\t",a[0]," = ",a[1])

    def handle_data(self,data):
        if data.isspace():
            return
        print("Encountered text data: ",data)
        pos = self.getpos()
        print("At line: ",pos[0]," and the character position: ",pos[1])
        print("----------------------------------------------\n")

def main():
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

    print("Total paragraph tags: ",paragraph)
        

if __name__ == "__main__":
    main()