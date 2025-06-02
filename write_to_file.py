from datetime import date

calculations = ['10.0 NZD is 5.9 USD', '20.0 NZD is 11.8 USD',
                '30.0 NZD is 17.7 USD', '40.0 NZD is 23.6 USD',
                '50.0 NZD is 29.5 USD', '60.0 NZD is 35.4 USD']

# **** Get current heading for heading and file name ****
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"currency_conversions_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:
    text_file.write("***** Currency Conversion Calculations *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your conversion history (oldest to newest)...\n\n")

    # write each item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")

print(f"Exported to file: {write_to}")