from tkinter import *


class Converter:
    """
    Currency conversion tool: NZD to USD or CAD
    """

    def __init__(self, master):
        """
        Currency converter GUI
        """

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

        self.temp_entry = Entry(self.answer_error,
                                font=("Arial", 14))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        self.output_label = Label(self.answer_error, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.answer_error)
        self.button_frame.grid(row=4)

        # button list (Button text | bg color | command | row | column)
        button_details_list = [
            ["To USD", "#990099", lambda: self.check_amount("USD"), 0, 0],
            ["To CAD", "#009900", lambda: self.check_amount("CAD"), 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve history / export button and disable it at the start
        self.button_ref_list[3].config(state=DISABLED)

    def check_amount(self, currency_type):
        """
        Checks if amount is valid, then converts to the given currency
        """

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
            self.output_label.config(text="", fg="#004C99")
            self.temp_entry.config(bg="white")

    def convert(self, amount, currency_type):
        # Dummy exchange rates for demonstration
        if currency_type == "USD":
            converted = amount * 0.60  # Example: 1 NZD = 0.60 USD
        elif currency_type == "CAD":
            converted = amount * 0.85  # Example: 1 NZD = 0.85 CAD
        else:
            converted = 0

        self.output_label.config(
            text=f"NZD ${amount:.2f} = {currency_type} ${converted:.2f}",
            fg="#004C99"
        )


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter(root)
    root.mainloop()
