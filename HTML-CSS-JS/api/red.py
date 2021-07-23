
import os
import requests

USERNAME = os.getenv("USERNAME")
IP = os.getenv("IP")
URL = f"http://{IP}/api/{USERNAME}/lights/1/state"

body = {
    "hue": 65535,
    "sat": 254
}


requests.put(URL, json=body)