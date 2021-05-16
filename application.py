from tkinter import *
from translator import *


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("morse code converter")
        self.root.resizable(False, False)
        self.root.geometry("600x380")

        self.create_frames()
        self.create_labels()
        self.create_IO()
        self.create_buttons()
        self.layout_widgets()

    def create_frames(self):
        self.window = Frame(self.root)
        self.button_window = Frame(self.root)
        self.instruction_window = Frame(self.root)

    def create_labels(self):
        self.morse_to_eng = True
        self.top_label = Label(self.window, text="Morse Code: ")
        self.bottom_label = Label(self.window, text="English: ")
        self.instruction_label = Label(self.instruction_window, text="-Accepted keys-\n"
                                                                     "Morse: dash, dot, forward-slash\n"
                                                                     "English: A-Z, 0-9, and punctuations  . , ? / - "
                                                                     "( ) ")

    def create_IO(self):
        self.input_text = Text(self.window, height=8, width=70)
        self.input_text.configure(wrap="none")
        self.output_text = Text(self.window, state="disabled", height=8, width=70)

    def create_buttons(self):
        self.swap_button = Button(self.button_window, command=self.swap, text="Swap", width=9)
        self.convert_button = Button(self.button_window, command=self.convert, text="Convert", width=9)
        self.clear_button = Button(self.button_window, command=self.clear, text="Clear", width=9)
        self.exit_button = Button(self.button_window, command=self.quit_app, text="Quit", width=9)
        # key binding
        self.root.bind("<Return>", self.convert)
        self.root.bind("<Escape>", self.quit_app)

    def layout_widgets(self):
        self.window.grid(column=0, row=0, padx=10, pady=5)
        self.top_label.grid(column=0, row=0, pady=10, sticky="N")
        self.bottom_label.grid(column=0, row=1, pady=10, sticky="N")
        self.input_text.grid(column=1, row=0, pady=10)
        self.output_text.grid(column=1, row=1, pady=10)

        self.button_window.grid(row=2, pady=12)
        self.convert_button.grid(column=0, row=0, padx=5)
        self.swap_button.grid(column=1, row=0, padx=5)
        self.clear_button.grid(column=2, row=0, padx=5)
        self.exit_button.grid(column=3, row=0, padx=5)

        self.instruction_window.grid(row=3)
        self.instruction_label.grid(column=0)

    # converts english to morse, or more to english
    def convert(self, event=None):
        entry = self.input_text.get("1.0", END).upper()

        if self.morse_to_eng:
            output = morse_to_english(entry)
        else:
            output = english_to_morse(entry)

        self.output_text.configure(state="normal")
        self.output_text.delete('1.0', END)
        self.output_text.insert('end', output)
        self.output_text.configure(state="disable")

    # swaps the languages (default: morse code to english)
    def swap(self):
        self.clear()

        if self.morse_to_eng:
            self.morse_to_eng = False
            self.top_label.config(text="English: ")
            self.bottom_label.config(text="Morse Code: ")

        else:
            self.morse_to_eng = True
            self.top_label.config(text="Morse Code: ")
            self.bottom_label.config(text="English: ")

    # deletes all user input & output
    def clear(self):
        self.output_text.configure(state="normal")
        self.input_text.delete('1.0', END)
        self.output_text.delete('1.0', END)
        self.output_text.configure(state="disable")

    # stops the application
    def quit_app(self, event=None):
        self.root.quit()
