import requests, json

# Hae kelikamerat
cams = requests.get("https://tie.digitraffic.fi/api/weathercam/v1/stations").json()
with open("cams.json","w",encoding="utf-8") as f:
    json.dump(cams,f,ensure_ascii=False,indent=2)

# Hae tiesääasemat
weather = requests.get("https://tie.digitraffic.fi/api/weather/v1/stations/data").json()
with open("weather.json","w",encoding="utf-8") as f:
    json.dump(weather,f,ensure_ascii=False,indent=2)
