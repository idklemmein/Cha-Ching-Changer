from tkinter import *
from functools import partial  # To prevent unwanted windows

MAX_CALCS = 5  # Maximum number of calculations to display in history


class Converter:
    """
    Currency converter GUI (NZD to USD or NZD to CAD)
    """

    def __init__(self):
        """
        Initializes the Currency Converter GUI
        """

        self.all_calculations_list = ['10.0 NZD is 5.9 USD', '20.0 NZD is 11.8 USD',
                                      '30.0 NZD is 24.6 CAD', '40.0 NZD is 32.8 CAD',
                                      '50.0 NZD is 29.5 USD', '60.0 NZD is 49.2 CAD']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=15,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and
        # 'release' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background color and text for calculations list
        if len(calculations) <= MAX_CALCS:
            calc_back = "D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {MAX_CALCS} / {len(calculations)}")

        # Message describing what is displayed
        recent_intro_txt = (f"Below are {calc_amount} currency conversions.")

        # Create string from calculations list (newest first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_list) <= MAX_CALCS:
            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[-1]
        else:
            for item in newest_first_list[:MAX_CALCS-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[MAX_CALCS-1]

        export_instruction_txt = ("Please push <Export> to save your conversions in a "
                                  "text file. If the filename already exists, it will be overwritten.")

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None],
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)
            history_label_ref.append(make_label)

        # Retrieve export instruction label for showing filename later
        self.export_filename_label = history_label_ref[3]

        # Button frame (for export and close)
        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        # Button details (text | bg color | command | row | column)
        button_details_list = [
            ["Export", "#004C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):
        """
        Closes history dialogue box (and enables history button)
        """
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()