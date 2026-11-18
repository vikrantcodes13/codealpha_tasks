
import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
    "NVDA": 480,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    print("-" * 28)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price:>8.2f}")
    print("-" * 28)


def get_quantity(symbol):
    """Ask for a valid positive whole number quantity."""
    while True:
        raw = input(f"  Quantity of {symbol}: ").strip()
        try:
            quantity = int(raw)
            if quantity <= 0:
                print("  Quantity must be greater than 0.")
            else:
                return quantity
        except ValueError:
            print("  Please enter a whole number.")


def collect_portfolio():
    """Collect stock names and quantities from the user."""
    portfolio = {}
    print("\nEnter your stocks one by one. Type 'done' when finished.")

    while True:
        symbol = input("\nStock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if not portfolio:
                print("You haven't added any stocks yet.")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not available. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        quantity = get_quantity(symbol)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added {quantity} x {symbol}.")

    return portfolio


def calculate_investments(portfolio):
    """Return a list of (symbol, qty, price, value) and the total."""
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append((symbol, quantity, price, value))
        total += value
    return rows, total


def display_summary(rows, total):
    print("\n" + "=" * 52)
    print(f"{'PORTFOLIO SUMMARY':^52}")
    print("=" * 52)
    print(f"{'Stock':<8}{'Qty':>8}{'Price':>14}{'Value':>18}")
    print("-" * 52)
    for symbol, quantity, price, value in rows:
        print(f"{symbol:<8}{quantity:>8}{'$' + format(price, ',.2f'):>14}{'$' + format(value, ',.2f'):>18}")
    print("-" * 52)
    print(f"{'TOTAL INVESTMENT':<30}{'$' + format(total, ',.2f'):>22}")
    print("=" * 52)


def save_to_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
        f.write("-" * 45 + "\n")
        for symbol, quantity, price, value in rows:
            f.write(f"{symbol}: {quantity} shares x ${price:,.2f} = ${value:,.2f}\n")
        f.write("-" * 45 + "\n")
        f.write(f"Total investment: ${total:,.2f}\n")
    print(f"Saved to {filename}")


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Saved to {filename}")


def ask_to_save(rows, total):
    choice = input("\nSave results? (txt / csv / both / no): ").strip().lower()
    if choice in ("txt", "both"):
        save_to_txt(rows, total)
    if choice in ("csv", "both"):
        save_to_csv(rows, total)
    if choice not in ("txt", "csv", "both"):
        print("Results not saved.")


def main():
    print("=" * 40)
    print("      STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    show_available_stocks()
    portfolio = collect_portfolio()
    rows, total = calculate_investments(portfolio)
    display_summary(rows, total)
    ask_to_save(rows, total)
    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
