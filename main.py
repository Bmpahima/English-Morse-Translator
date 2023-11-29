import pandas as pd
from tkinter import *
from tkinter import messagebox
import subprocess

TITLE_FONT = ("helvetica", 36, "bold")
NORMAL_FONT = ("helvetica", 16, "normal")
BG_COLOR = "#DAE2DF"


# Create Tk window
window = Tk()
window.title("Morse Code Translator")
window.config(height="500", width="800", background=BG_COLOR, padx=50, pady=50)


# English to Morse converter function based on the Morse alphabet written in the morse-alphabet.csv file
def morse_converter():
    try:
        df = pd.read_csv("morse-alphabet.csv")

        if english_morse_button.cget("text") == "English to Morse":
            # Convert input to uppercase and replace spaces and commas
            word = word_entry.get().upper().replace(" ", "s").replace(",", "c")
            # Translate each character to Morse code
            translated_word = " ".join(df[df['English'] == char]['Morse'].item() for char in word)
        else:
            # Convert input to list of characters and replace to spaces and commas
            word = word_entry.get().split(" ")
            # Translate each character to English
            translated_word = "".join(df[df['Morse'] == char]['English'].item() for char in word)
            translated_word = translated_word.replace("s", " ").replace("c", ",")

        # Update UI components
        copy_button.config(text="Copy")
        answer_label.config(text=translated_word)

    except (Exception, ):
        messagebox.showwarning("Error", f"Undefined Character")


# Create a function that enables the user to copy the translation
def copy_word():
    if answer_label.cget("text"):
        data = answer_label.cget("text")
        subprocess.run("pbcopy", text=True, input=data)
        copy_button.config(text="COPIED")


# Switch the options: "English to Morse" or "Morse to English"
def switch_english_morse():
    if english_morse_button.cget("text") == "Morse to English":
        english_morse_button.config(text="English to Morse")
        from_lang_label.config(text="English:")
        translation_label.config(text="Morse:")

    else:
        english_morse_button.config(text="Morse to English")
        from_lang_label.config(text="Morse:")
        translation_label.config(text="English:")


title_label = Label(text="Text to Morse Translator", fg="black", bg=BG_COLOR, font=TITLE_FONT)
title_label.grid(row=1, column=1, columnspan=2, pady=50)

photo = PhotoImage(file="morse-code.png")
canvas = Canvas(height=130, width=130, bg=BG_COLOR, bd=0, highlightthickness=0)
canvas.create_image(75, 75, image=photo)
canvas.grid(row=0, column=1, columnspan=2)

english_morse_button = Button(text="English to Morse", highlightthickness=0, bd=0, font=NORMAL_FONT, width=10, command=switch_english_morse)
english_morse_button.grid(row=2, column=1, columnspan=2, pady=20)

from_lang_label = Label(text="English:", fg="black", bg=BG_COLOR, font=NORMAL_FONT)
from_lang_label.grid(row=3, column=0)

word_entry = Entry(width=30)
word_entry.grid(row=3, column=1, columnspan=2)

convert_button = Button(text="Convert", highlightthickness=0, command=morse_converter, bd=0, font=NORMAL_FONT, width=7)
convert_button.grid(row=3, column=3)

translation_label = Label(text="Morse:", fg="black", bg=BG_COLOR, font=NORMAL_FONT)
translation_label.grid(row=5, column=0)

answer_label = Label(bg=BG_COLOR, font=NORMAL_FONT, fg="black")
answer_label.grid(row=5, column=1)

copy_button = Button(text="Copy", command=copy_word, highlightthickness=0, bd=0, font=NORMAL_FONT, width=7)
copy_button.grid(row=5, column=3)

window.mainloop()
