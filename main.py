#!/usr/bin/env python3

import requests
import random
import webbrowser
from call import useragents, sites, user

user = user.lower().replace('.','')
for url in sites.values():
    print(f"\nChecking out {url} ")
    try:
        response = requests.get(url, allow_redirects=False, headers={'User-Agent': random.choice(useragents)})
        body = response.text
        try:
            response.raise_for_status()
        except:
            pass
        status_code = response.status_code
        print("status_code:", status_code)
        if status_code == 200:
          print(f"|\n---> (Possible Hit)")
          webbrowser.open(url)
    except requests.exceptions.RequestException as e:
        pass
