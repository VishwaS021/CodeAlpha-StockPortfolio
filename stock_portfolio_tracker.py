stock_prices = {
    "AAPL": 180,   
    "TSLA": 250,
    "MSFT": 350,   
    "GOOGL": 140,
    "AMZN": 135
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please enter a valid symbol.")
        continue

    try:
        qty = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + qty
    total_value += qty * stock_prices[stock_name]

print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    print(f"{stock}: {qty} shares = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save_choice = input("\nDo you want to save the portfolio to a file? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            file.write(f"{stock}: {qty} shares = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(" Portfolio saved to portfolio.txt")
