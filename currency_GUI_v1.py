from tkinter import *


class Converter():
    """
    Currency conversion tool (°USD to °NZD or °NZD to °USD and NZD to CAD or CAD to NZD)
    """

    def __init__(self):
        """
        Currency converter to GUI
        """

        self.cur_frame = Frame(padx=10, pady=10)
        self.cur_frame.grid()

        self.cur_heading = Label(self.cur_frame,
                                  text="Currency Converter",
                                  font=("Arial", "16", "bold"))
        self.cur_heading.grid(row=0)

        instructions = ("Please enter a Currency below and then press "
                        "one of the buttons to convert it from NZD "
                        "to CAD or USD.")
        self.cur_instructions = Label(self.cur_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.cur_instructions.grid(row=1)

        self.cur_entry = Entry(self.cur_frame,
                                font=("Arial", "14")
                                )
        self.cur_entry.grid(row=2, padx=10, pady=10)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.cur_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To USD",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="To CAD",
                                           bg="#009900",
                                           fg="#ffffff",
                                           font=("Arial", "12", "bold"), width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#ffffff",
                                     font=("Arial", "12", "bold"), width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history = Button(self.button_frame,
                                      text="History / Export",
                                      bg="#004C99",
                                      fg="#ffffff",
                                      font=("Arial", "12", "bold"), width=12)
        self.to_history.grid(row=1, column=1, padx=5, pady=5)

    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()