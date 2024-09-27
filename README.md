# Live Cryptocurrency Data Analysis

This project fetches live cryptocurrency data from a public API, analyzes it, and presents the data in a live-updating Excel sheet using Python. The goal is to provide real-time insights into cryptocurrency trends by monitoring and displaying the data in an easily accessible format.

## Project Overview

The Python script fetches live cryptocurrency data at regular intervals, processes the data, and continuously updates an Excel sheet with the most recent values. The project includes:

- Fetching live cryptocurrency prices via API.
- Storing and dynamically updating data in an Excel sheet.
- Analyzing price trends and changes over time.
- A customizable setup for selecting specific cryptocurrencies.

## Features

- **Real-Time Data Fetching**: Automatically retrieve cryptocurrency data every few seconds.
- **Live Excel Updates**: Continuously update the Excel sheet with new cryptocurrency data.
- **Data Analysis**: Track and analyze trends in cryptocurrency prices.
- **API Integration**: Retrieve data for multiple cryptocurrencies using a public API.

## Installation

Navigate to the project directory:

bash
Copy code
cd crypto-data-analysis
Install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Start the script:

bash
Copy code
python crypto_analysis.py
The script will begin fetching live cryptocurrency data and updating the Excel sheet.

Open the Excel file to see live-updated cryptocurrency prices and trends.

Dependencies
This project relies on the following Python libraries:

requests: To handle API calls and fetch live data.
openpyxl: To work with Excel files and update the data.
pandas: For data analysis and manipulation.
To install these dependencies, run:

bash
Copy code
pip install requests openpyxl pandas
How It Works
API Fetching: The script uses a public API to fetch cryptocurrency prices at set intervals.
Excel Integration: It saves the data into an Excel file and continuously updates it with the latest prices.
Analysis: The Excel sheet serves as a live tracker for cryptocurrency price movements, allowing you to monitor trends over time.
Customization
Update Frequency: You can adjust the interval between API calls in the script.
Select Cryptocurrencies: Customize the API query to fetch data for specific cryptocurrencies you are interested in.
