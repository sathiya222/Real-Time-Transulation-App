import tkinter as tk
from googletrans import Translator
from datetime import datetime

def translate_word():
    word = entry.get().strip()
    if not word:
        output_label.config(text="Please enter a word.")
        return
    
    if word[0].lower() in 'aeiou':
        if datetime.now().hour in range(21, 22):
            try:
                translation = translator.translate(word, src='en', dest='hi').text
                output_label.config(text=translation)
            except Exception as e:
                output_label.config(text=f"Translation error: {e}")
        else:
            output_label.config(text="Translation allowed only between 9 PM and 10 PM.")
    else:
        output_label.config(text="This word starts with a consonant. Please provide another word.")

translator = Translator()

root = tk.Tk()
root.title("English to Hindi Translator")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
