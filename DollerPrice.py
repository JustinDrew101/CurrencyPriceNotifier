import requests
import pywhatkit as pwk
import time

# WhatsApp credentials
RECIPIENT_PHONE_NUMBER = ""
from_currency = ""
to_currency = ""

# Alpha Vantage API credentials
API_KEY = ""

# Function to get the exchange rate from Alpha Vantage
def get_exchange_rate():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    print("Exchange")
    return rate

# Function to send a WhatsApp message using pywhatkit
def send_whatsapp_message(message):
    pwk.sendwhatmsg_instantly(RECIPIENT_PHONE_NUMBER, message)

# Function to check the exchange rate and send a message if it decreases
def check_exchange_rate():
    previous_rate = None

    while True:
        current_rate = get_exchange_rate()
        print("REACH")
        if previous_rate is not None and current_rate < previous_rate:
            message = f"The {from_currency} price has decreased to {current_rate} {to_currency} from {previous_rate}."
            send_whatsapp_message(message)

        previous_rate = current_rate
        time.sleep(3600)  # Wait for 1 hour before checking again

# Start checking the exchange rate
check_exchange_rate()