import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import threading
import time

class CurrencyConverter:
    def __init__(self, api_url):
        self.api_url = api_url
        self.rates = {}
        self.currency_codes = {}
        self.timestamp = None
        self.fetch_exchange_rates()

    def fetch_exchange_rates(self):
        try:
            response = requests.get(self.api_url)
            
            # Check if the status code is OK (200)
            if response.status_code != 200:
                raise Exception(f"Error fetching data from API. Status Code: {response.status_code}")
            
            # Try to parse the JSON response
            try:
                data = response.json()
            except json.JSONDecodeError:
                raise Exception("Error decoding JSON response. The response might not be in JSON format.")
            
            # Check if the response contains 'rates' key
            if "rates" in data:
                self.rates = data["rates"]
                self.currency_codes = list(self.rates.keys())  # Store only currency codes for reference
                self.timestamp = time.time()  # Store the timestamp of when rates were fetched
                print("Rates fetched successfully.")
            else:
                raise Exception("Error: 'rates' key missing in the response.")

        except Exception as e:
            print(f"Exception: {e}")
            messagebox.showerror("Error", f"Error fetching exchange rates: {e}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]
        converted_amount = amount * self.rates[to_currency]
        return round(converted_amount, 2)

    def is_cache_expired(self):
        if self.timestamp is None:  # If timestamp is None, we haven't fetched rates yet
            return True
        return time.time() - self.timestamp > 3600  # 1 hour cache expiry

class CurrencyConverterApp:
    def __init__(self, root, converter):
        self.root = root
        self.converter = converter
        self.root.title("Currency Converter")
        self.root.geometry("400x350")

        # Currency selection labels
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.pack(pady=5)

        # Dropdown for from_currency
        self.from_currency_combo = ttk.Combobox(root, values=self.converter.currency_codes)
        self.from_currency_combo.set("USD")  # Set default currency as USD
        self.from_currency_combo.pack(pady=5)

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.pack(pady=5)

        # Dropdown for to_currency
        self.to_currency_combo = ttk.Combobox(root, values=self.converter.currency_codes)
        self.to_currency_combo.set("EUR")  # Set default currency as EUR
        self.to_currency_combo.pack(pady=5)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="Converted Amount:")
        self.result_label.pack(pady=5)

        self.result_display = tk.Label(root, text="")
        self.result_display.pack(pady=5)

        # Refresh Button for Currency Rates
        self.refresh_button = tk.Button(root, text="Refresh Rates", command=self.refresh_rates)
        self.refresh_button.pack(pady=10)

        # Check if the exchange rates are expired
        if self.converter.is_cache_expired():
            self.converter.fetch_exchange_rates()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            if not amount or not from_currency or not to_currency:
                raise ValueError("All fields must be filled.")

            if from_currency not in self.converter.rates or to_currency not in self.converter.rates:
                raise ValueError("Invalid currency entered.")

            converted_amount = self.converter.convert(amount, from_currency, to_currency)
            self.result_display.config(text=f"{converted_amount} {to_currency}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def refresh_rates(self):
        thread = threading.Thread(target=self.converter.fetch_exchange_rates)
        thread.start()
        thread.join()
        messagebox.showinfo("Info", "Exchange rates updated successfully.")

if __name__ == "__main__":
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Use the correct API URL for V6
    converter = CurrencyConverter(api_url)

    root = tk.Tk()
    app = CurrencyConverterApp(root, converter)
    root.mainloop()
