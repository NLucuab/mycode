#!/usr/bin/env python3

import requests
import datetime

API = "http://api.open-notify.org/iss-now.json"

def main():
    # need to convert api response to json to handle in python
    resp = requests.get(API).json()
    # print(resp)
    # Returns this: {'timestamp': 1677686812, 'message': 'success', 'iss_position': {'longitude': '-61.4565', 'latitude': '-21.6941'}}

    timestamp = resp['timestamp']

    print("CURRENT LOCATION OF THE ISS: ")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(timestamp)}")
    print(f"Lon: {resp['iss_position']['longitude']}")
    print(f"Lat: {resp['iss_position']['latitude']}")
    
if __name__ == '__main__':
    main()