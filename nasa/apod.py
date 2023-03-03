#!/usr/bin/env python3
import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"


def main():
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=9KbxOILILBUWwJx3b4yowqjG9VGIy3siZRyGSivb" + \
        nasacreds.strip("\n")

    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    apodread = apodurlobj.read()

    apod = json.loads(apodread.decode("utf-8"))

    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__ == "__main__":
    main()
