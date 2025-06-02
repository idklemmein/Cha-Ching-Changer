from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Currency conversion tool GUI
    """

    def __init__(self):
        """
        Currency converter GUI
        """
        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.to_help_button = Button(self.currency_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        """
        Open help dialogue box and disable button
        (to prevent multiple help boxes).
        """
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # Setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_button.config(state=DISABLED)

        # If user clicks the close button, call close_help to re-enable button
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
            "that you want to convert.\n\n"
            "Then choose the target currency — either US Dollars (USD) or Canadian Dollars (CAD).\n\n"
            "After selecting the currency, click the 'Convert' button to see the converted amount.\n\n"
            "To view your conversion history or export it to a text file, click the "
            "'History / Export' button.\n\n"
            "Note: Make sure all amounts entered are positive numbers."
        )

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # Set background colour on all labels and frames
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box and re-enables the help button
        """
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()
