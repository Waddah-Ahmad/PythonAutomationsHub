
# Project: Automated Cryptocurrency Price Tracker
"""
Description: This project automates the process of fetching real-time cryptocurrency prices from a cryptocurrency exchange using its API. 
It then processes the data and provides insights, such as price changes and trends.
"""


import requests

def get_crypto_prices(api_key, crypto_symbols):
    base_url = "https://api.coinbase.com/v2/prices/"
    prices = {}

    for symbol in crypto_symbols:
        response = requests.get(f"{base_url}{symbol}-USD/spot", headers={"Authorization": f"Bearer {api_key}"})
        data = response.json()
        prices[symbol] = float(data["data"]["amount"])

    return prices

def analyze_price_changes(prices):
    sorted_prices = sorted(prices.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 Cryptocurrencies by Price:")
    for symbol, price in sorted_prices[:5]:
        print(f"{symbol}: ${price:.2f}")

    average_price = sum(prices.values()) / len(prices)
    print(f"Average Price of All Cryptocurrencies: ${average_price:.2f}")

if __name__ == "__main__":
    coinbase_api_key = "your_coinbase_api_key"  # Replace with your Coinbase API key
    crypto_symbols = ["BTC", "ETH", "ADA", "XRP", "DOGE"]  # Replace with your desired crypto symbols

    crypto_prices = get_crypto_prices(coinbase_api_key, crypto_symbols)
    analyze_price_changes(crypto_prices)




    