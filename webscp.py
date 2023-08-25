from urllib.request import urlopen
import json

with urlopen("https://google.com") as response:
    body = response.read()
print(body[:15])