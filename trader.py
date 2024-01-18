import alpaca_trade_api as tradeapi
import time

APCA_API_BASE_URL = "https://api.alpaca.markets"
APCA_API_KEY_ID = input("Enter your API key ID: ")
APCA_API_SECRET_KEY = input("Enter your API secret key: ")

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, base_url=APCA_API_BASE_URL, api_version='v2')

def get_account():
    account = api.get_account()
    return account

def get_market_status():
    clock = api.get_clock()
    return clock

def place_order(symbol, qty, side, order_type, time_in_force):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=order_type,
        time_in_force=time_in_force
    )
    return order

def main():
    while True:
        try:
            account = get_account()
            market_status = get_market_status()

            if account.trading_blocked == 'false':
                print("Account trading is blocked on this Account")
                print("Exiting...")
                break

            if not market_status.is_open:
                print("Market is closed. Waiting...")

            if market_status.is_open:
                manual_trade = input("Do you want to manually trade? (y/n): ")

                if manual_trade == 'y':
                    symbol = input("Enter the symbol you want to trade: ")

                    # Set the quantity, side, order type, and time in force according to your strategy
                    qty = input("Enter the quantity: ")
                    side = 'buy'
                    order_type = 'market'
                    time_in_force = 'gtc'

                    # Place an order
                    order = place_order(symbol, qty, side, order_type, time_in_force)

                    print(f"Order placed: {order}")
                
                else:
                    # do trading strategy here
                    print("Trading strategy goes here")
            else:
                print("Market closed or trading is blocked. Waiting...")
            
            # Sleep for a minute (you can adjust this based on your strategy)
            time.sleep(60)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()