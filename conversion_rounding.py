# currency_converter.py

def round_currency(val):
    val = round(val * 10) / 10
    return "{:.1f}".format(val)

def convert_to_usd(nzd_amount):
    exchange_rate = 0.59
    usd = nzd_amount * exchange_rate
    return round_currency(usd)

def convert_to_cad(nzd_amount):
    exchange_rate = 0.82
    cad = nzd_amount * exchange_rate
    return round_currency(cad)

if __name__ == "__main__":
    while True:
        try:
            nzd_input = input("Enter NZD amount to convert (or 'q' to quit): ").strip()
            if nzd_input.lower() == 'q':
                print("Exiting Currency Converter.")
                break

            nzd_amount = float(nzd_input)
            if nzd_amount <= 0:
                print("Amount must be greater than 0.\n")
                continue

            usd = convert_to_usd(nzd_amount)
            cad = convert_to_cad(nzd_amount)

            print(f"{nzd_amount} NZD is {usd} USD (rounded to 1 decimal place)")
            print(f"{nzd_amount} NZD is {cad} CAD (rounded to 1 decimal place)\n")

        except ValueError:
            print("Please enter a valid number.\n")
