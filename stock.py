from yahoofinancials import YahooFinancials as yf

ticker = "^FTSE"
start = "2020-01-01"
end = "2020-04-01"

yahoo_page = yf(ticker)
ftse = yahoo_page.get_historical_price_data(start, end, "daily")


days = ftse["^FTSE"]["prices"]


def opening_stock_price():
    opening = {}

    for price in days:
        date = price["formatted_date"]
        open = price["open"]

        opening[date] = open

    print(opening)


def closing_stock_price():
    closing = {}

    for price in days:
        date = price["formatted_date"]
        close = price["close"]

        closing[date] = close

    print(closing)


opening_stock_price()
closing_stock_price()
