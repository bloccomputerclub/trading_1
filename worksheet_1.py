portfolio = {
    'cash': 1000.0,  # Starting with $1,000 in cash
    'stocks': {}  # An empty dictionary to hold stock shares
}


def read_csv(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(',') for line in lines][1:]  # Skip header
        return [(int(timestamp), ticker, float(price)) for timestamp, ticker, price in data]


# Read market data
market_data = read_csv('starter-data.csv')

# Print the first 5 entries of the market data to check
for entry in market_data[:5]:
    print(entry)

# The market_data is now a list of tuples, where each tuple is (date, price).


# Updated function to simulate buying a stock at a specific time


def buy(ticker, time, num_shares):
    # Find the price of the stock at the given time
    for date, stock_ticker, price in market_data:
        print(stock_ticker)
        if stock_ticker == ticker and date == time:
            shares_to_buy = num_shares
            portfolio['stocks'].setdefault(ticker, 0)
            portfolio['stocks'][ticker] += shares_to_buy
            portfolio['cash'] -= shares_to_buy * price
            print(f"Portfolio after buying: {portfolio}")
            return
    print(f"Time {time} not found in data or ticker {ticker} not found.")

# Updated function to simulate selling a stock at a specific time


def sell(ticker, time, shares_to_sell):
    # Find the price of the stock at the given time
    # shares_to_sell = portfolio['stocks'].get(ticker_to_trade, 0)
    for date, stock_ticker, price in market_data:
        if stock_ticker == ticker and date == time:
            if ticker in portfolio['stocks'] and shares_to_sell <= portfolio['stocks'][ticker]:
                portfolio['stocks'][ticker] -= shares_to_sell
                portfolio['cash'] += shares_to_sell * price
                if portfolio['stocks'][ticker] == 0:
                    # Remove the ticker if no shares left
                    del portfolio['stocks'][ticker]
                print(f"Portfolio after selling: {portfolio}")
            else:
                print(f"Not enough shares of {ticker} to sell.")
            return
    print(f"Time {time} not found in data or ticker {ticker} not found.")


# Example usage:
buy('ABCD', 1, 2)

sell('ABCD', 5, 1)
