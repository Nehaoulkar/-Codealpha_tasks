stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 135,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when finished.\n")

while True:
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print(" Stock not found. Please choose from available list.")
        continue

    try:
        qty = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + qty

print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n Total Investment Value: ${total_investment}")




