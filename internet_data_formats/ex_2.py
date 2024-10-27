import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)
    print("-------------------------------\n")
    print(theJSON)
    print("-------------------------------\n")
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    print("-------------------------------\n")
    count = theJSON["metadata"]["count"]
    print(count," events recorded")
    print("-------------------------------\n")
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-------------------------------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("||||||||||||||||||||||||||||||||||\n")
            print(i["properties"]["place"]," : ",i["properties"]["mag"])

    print("-------------------------------\n")
    print("Events that were felt: ")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"]," : ",feltReports," times")

def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("Request Code: "+str(webUrl.getcode()))
    if(webUrl.getcode()==200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error from server, Cann;t print results",webUrl.getcode())

if __name__ == "__main__":
    main()