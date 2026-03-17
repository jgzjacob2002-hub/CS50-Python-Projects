import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

else:
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=425eef43860ba57cd5ff3d08561153348c6286272bd399b66d92f1566f7183c9")
        precio = float(response.json()["data"]["priceUsd"])
        unidades = float(sys.argv[1])
        print(f"${(unidades * precio):,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        sys.exit()
