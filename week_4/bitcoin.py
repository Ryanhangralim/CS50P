import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
else:
    try:
        btc = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        output = response.json()
        price = float(output["bpi"]["USD"]["rate"].replace(",", ""))
        print(f"${(btc * price):,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.ext("API Error")
