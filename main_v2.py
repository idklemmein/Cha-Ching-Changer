from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import datetime  # For date formatting

# Constants
MAX_CALCS = 5  # Maximum number of calculations to display in history
EXPORT_FILENAME = "currency_conversions.txt"

# --- Currency Conversion Functions ---
def round_currency(val):
    """
    Rounds currency to the nearest tenth (0.1)
    :param val: Number to be rounded
    :return: String formatted to one decimal place
    """
    val_rounded = round(val * 10) / 10  # Round to nearest 0.1
    return "{:.1f}".format(val_rounded)

def convert_to_usd(nzd_amount):
    exchange_rate = 0.59
    usd = nzd_amount * exchange_rate
    return round_currency(usd)

def convert_to_cad(nzd_amount):
    exchange_rate = 0.82
    cad = nzd_amount * exchange_rate
    return round_currency(cad)


# --- GUI Classes ---
class Converter:
    def __init__(self, master):
        self.all_calculations_list = []

        self.answer_error = Frame(master, padx=10, pady=10)
        self.answer_error.grid()

        self.temp_heading = Label(self.answer_error,
                                  text="Currency Converter",
                                  font=("Arial", 16, "bold"))
        self.temp_heading.grid(row=0)

        instructions = ("Please enter an amount in NZD below and then press "
                        "one of the buttons to convert it to CAD or USD.")
        self.temp_instructions = Label(self.answer_error,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.answer_error, font=("Arial", 14))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        self.output_label = Label(self.answer_error, text="", fg="#9C0000")
        self.output_label.grid(row=3)

        self.button_frame = Frame(self.answer_error)
        self.button_frame.grid(row=4)

        button_details_list = [
            ["To USD", "#990099", lambda: self.check_amount("USD"), 0, 0],
            ["To CAD", "#009900", lambda: self.check_amount("CAD"), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", self.to_history, 1, 1]
        ]

        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(self.make_button)

        # Disable history/export button initially
        self.button_ref_list[3].config(state=DISABLED)

    def check_amount(self, currency_type):
        to_convert = self.temp_entry.get()

        try:
            to_convert = float(to_convert)
            if to_convert > 0:
                error = ""
                self.convert(to_convert, currency_type)
            else:
                error = "Amount must be greater than 0"
        except ValueError:
            error = "Please enter a valid number"

        if error:
            self.output_label.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
        else:
            self.temp_entry.config(bg="white")

    def convert(self, amount, currency_type):
        if currency_type == "USD":
            converted = convert_to_usd(amount)
        elif currency_type == "CAD":
            converted = convert_to_cad(amount)
        else:
            converted = "0.0"

        result = f"{round_currency(amount)} NZD is {converted} {currency_type}"
        self.output_label.config(
            text=result, fg="#004C99")

        self.all_calculations_list.append(result)
        self.button_ref_list[3].config(state=NORMAL)  # Enable History/Export

    def to_help(self):
        DisplayHelp(self)

    def to_history(self):
        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()
        partner.button_ref_list[2].config(state=DISABLED)
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = (
            "To use the program, enter the amount of money in New Zealand Dollars (NZD) "
            "that you want to convert.\n\nThen choose the target currency — either US Dollars (USD) or Canadian Dollars (CAD).\n\nAfter selecting the currency, click the 'Convert' button to see the converted amount.\n\nTo view your conversion history or export it to a text file, click the 'History / Export' button.\n\nNote: Make sure all amounts entered are positive numbers."
        )

        self.help_text_label = Label(self.help_frame, text=help_text,
                                     wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600", fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        for item in [self.help_frame, self.help_heading_label, self.help_text_label]:
            item.config(bg=background)

    def close_help(self, partner):
        partner.button_ref_list[2].config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:
    def __init__(self, partner, calculations):
        self.calculations = calculations

        self.history_box = Toplevel()
        partner.button_ref_list[3].config(state=DISABLED)
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        if len(calculations) <= MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {MAX_CALCS} / {len(calculations)}")

        recent_intro_txt = (f"Below are {calc_amount} currency conversions.")

        newest_first_string = "\n".join(list(reversed(calculations[:MAX_CALCS])))

        export_instruction_txt = ("Please push <Export> to save your conversions in a "
                                  "text file. If the filename already exists, it will be overwritten.")

        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None],
        ]

        for count, item in enumerate(history_labels_list):
            Label(self.history_box, text=item[0], font=item[1],
                  bg=item[2], wraplength=300,
                  justify="left", pady=10, padx=20).grid(row=count)

        self.export_status_label = Label(self.history_box, text="", font=("Arial", "10", "italic"))
        self.export_status_label.grid(row=5)

        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        button_details_list = [
            ["Export", "#004C99", self.export_to_file, 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            Button(self.history_button_frame, font=("Arial", "12", "bold"),
                   text=btn[0], bg=btn[1], fg="#FFFFFF", width=12,
                   command=btn[2]).grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def export_to_file(self):
        try:
            with open(EXPORT_FILENAME, "w") as f:
                f.write("***** Currency Conversion Calculations *****\n")
                f.write(f"Generated: {datetime.now().strftime('%d/%m/%Y')}\n\n")
                f.write("Here is your conversion history (oldest to newest)...\n\n")
                for calc in self.calculations:
                    f.write(calc + "\n")
            self.export_status_label.config(
                text=f"Exported to '{EXPORT_FILENAME}' successfully.", fg="green")
        except Exception as e:
            self.export_status_label.config(text=f"Export failed: {e}", fg="red")

    def close_history(self, partner):
        partner.button_ref_list[3].config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter(root)
    root.mainloop()
