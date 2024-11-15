from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com"
API_KEY = "fca_live_9KPSXMSpFlLtB0KJ3r38tKJHkG8WNlsfp57q3tww"

#https://api.freecurrencyapi.com/v1/latest
#apikey=fca_live_9KPSXMSpFlLtB0KJ3r38tKJHkG8WNlsfp57q3tww&currencies=EUR%2CUSD%2CCAD


printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    printer.pprint(data)

get_currencies()
