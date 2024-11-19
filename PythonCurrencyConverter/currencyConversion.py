from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://free.currconv.com/"
API_KEY = "1a93775ca87c544bab27"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']

        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - ({symbol})")

def exchange_rates(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies.")
        return

    rate = list(data.values())[0] # grabs 0th element which is what the rate is
    print(f"{currency1} -> {currency2} = {rate}")

    return  rate

def convert(currency1, currency2, amount):
    rate = exchange_rates(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} = {currency2}.")

    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to Currency Converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")

    while True:
        command = input("Enter a command (q to quit): ").lower()
        if command == "q":
            break

        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency id: ").upper()
            amount = input(f"Enter amount to in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)

        elif command == "rate":
            currency1 = input("Enter a base currency id").upper()
            currency2 = input(f"Enter a currency to convert to: ").upper()
            exchange_rates(currency1, currency2)
        else:
            print("Unrecognized command.")
main()


################################################
#ata = get_currencies()
#print_currencies(data)
#rate = exchange_rates("USD", "CAD")
#print(rate)