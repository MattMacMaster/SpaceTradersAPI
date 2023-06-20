import requests

def RegisterNewAgent(callsign,faction):
    PARAMS = {"symbol":""}
    URL = "https://api.spacetraders.io/v2/register"
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print(data)