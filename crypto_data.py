import requests
import pandas as pd
import time

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    parameters = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'sparkline': 'false'
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Select relevant columns
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
    df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization', '24h Trading Volume', '24h Price Change (%)']

    return df

def analyze_data(df):
    # Identifying the top 5 cryptocurrencies by market cap
    top_5 = df.nlargest(5, 'Market Capitalization')

    # Calculating the average price of the top 50 cryptocurrencies
    average_price = df['Current Price (USD)'].mean()

    # Analyzing the highest and lowest 24-hour percentage price change
    highest_change = df['24h Price Change (%)'].max()
    lowest_change = df['24h Price Change (%)'].min()

    return top_5, average_price, highest_change, lowest_change

def main():
    while True:
        # Fetch live data
        df = fetch_crypto_data()

        # Analyze data
        top_5, average_price, highest_change, lowest_change = analyze_data(df)

        # Save to Excel
        df.to_excel('top_50_cryptocurrencies.xlsx', index=False)

        # Print analysis results
        print("Top 5 Cryptocurrencies by Market Cap:")
        print(top_5)
        print(f"Average Price of Top 50 Cryptocurrencies: {average_price:.2f} USD")
        print(f"Highest 24h Price Change: {highest_change:.2f}%")
        print(f"Lowest 24h Price Change: {lowest_change:.2f}%")

        # Wait for 5 minutes before fetching the data again
        print("Fetching new data in 5 minutes...")
        time.sleep(300)

if __name__ == "__main__":
    main()
