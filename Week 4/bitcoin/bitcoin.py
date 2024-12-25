import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit(" Request exception occured")

price = response["bpi"]["USD"]["rate_float"]


print(f"${price*n:,.4f}")
