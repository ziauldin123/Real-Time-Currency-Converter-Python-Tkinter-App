# Real-Time-Currency-Converter-Python-Tkinter-App
A Python-based real-time currency converter app using Tkinter for the GUI and ExchangeRate-API for fetching live exchange rates. Supports dynamic currency selection and conversion.
A simple yet powerful currency converter built using Python and Tkinter for the graphical user interface. This application allows users to convert between various currencies using real-time exchange rates fetched from the [ExchangeRate-API](https://www.exchangerate-api.com/).

## Features
- Real-time currency conversion based on up-to-date exchange rates.
- Ability to convert between any two currencies.
- Simple, user-friendly graphical interface.
- Currencies loaded dynamically from the API.

## Requirements
- Python 3.x
- `requests` library
- `tkinter` library (usually comes pre-installed with Python)

## Setup Instructions

### Step 1: Clone the repository
Clone the repository to your local machine:
```
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

### Step 2: Install dependencies
You need the `requests` library to fetch data from the API. Install it using pip:
```
pip install requests
```

### Step 3: Get your API Key
Sign up for a free account at [ExchangeRate-API](https://www.exchangerate-api.com/) and get your personal API key.

### Step 4: Update the API URL
In the `currency_converter.py` file, replace `YOUR-API-KEY` with your actual API key:
```python
self.api_url = f"https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD"
```

### Step 5: Run the application
Run the `currency_converter.py` script to launch the application:
```
python currency_converter.py
```

### Step 6: Enjoy the app!
You can now use the app to convert between different currencies. Simply select the currencies from the dropdown, enter the amount to convert, and hit the "Convert" button.

## How It Works

1. The app fetches real-time exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).
2. The rates are loaded dynamically into the dropdown menus for selecting the currencies to convert.
3. The user enters an amount to convert and clicks "Convert."
4. The app calculates the converted amount using the rates fetched from the API.

## Troubleshooting
- **404 Error**: If you see a 404 error while fetching rates, ensure that the API URL and your API key are correct.
- **API Limit Exceeded**: If you are using a free-tier API key, make sure you have not exceeded the rate limits. You may need to upgrade your API key for higher limits.

## License
This project is open-source and available under the [MIT License](LICENSE).

