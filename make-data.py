import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

def generate_data(file):
    # Constants
    hours_per_day = 24
    num_days = 10
    total_hours = hours_per_day * num_days

    # Generating timestamps
    timestamps = np.repeat(np.arange(1, total_hours + 1), 2)

    # Generating tickers
    tickers = np.tile(['ABCD', 'EFGH'], total_hours)

    # Generating prices for each stock with a random walk
    # np.random.seed(0)  # for reproducibility
    start_price_A = 50
    start_price_B = 35
    price_walk_A = np.random.normal(0, 0.7, total_hours)  # Mean, standard deviation
    price_walk_B = np.random.normal(0, 0.5, total_hours)

    # Cumulative sum to simulate the price change
    price_A = np.round(np.cumsum(price_walk_A) + start_price_A, 2)
    price_B = np.round(np.cumsum(price_walk_B) + start_price_B, 2)

    # Combining prices
    prices = np.ravel(np.column_stack((price_A, price_B)))

    # Creating the DataFrame
    df = pd.DataFrame({
        'timestamp': timestamps,
        'ticker': tickers,
        'price per unit': prices
    })

    # Saving to a CSV file
    df.to_csv(file, index=False)
    print(f"wrote {file}")

def visualize_data(file):
    df = pd.read_csv(file)
    # Filtering data for each ticker
    df_A = df[df['ticker'] == 'ABCD']
    df_B = df[df['ticker'] == 'EFGH']

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(df_A['timestamp'], df_A['price per unit'], color='red', label='ABCD')
    plt.plot(df_B['timestamp'], df_B['price per unit'], color='blue', label='EFGH')

    plt.title('Stock Prices Over Time')
    plt.xlabel('Time (Hourly Intervals)')
    plt.ylabel('Price Per Unit')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visualize', type=str, help='Visualize the data in the given csv file')
    parser.add_argument('-g', '--generate', type=str, help='Generate new data, write it to the given file, and visualize it')
    args = parser.parse_args()

    if args.visualize:
        visualize_data(args.visualize)

    if args.generate:
        generate_data(args.generate)

if __name__ == "__main__":
    main()
