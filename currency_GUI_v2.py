from tkinter import *


class Converter:
    """
    Currency conversion tool (NZD to CAD or NZD to USD)
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

        # button list (Button text | bg color | command | row | column)
        button_details_list = [
            ["To USD", "#990099", "", 0, 0],
            ["To CAD", "#009900", "", 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve history / export button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()