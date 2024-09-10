from googletrans import Translator
from tkinter import Tk, Label, Entry, Button, messagebox
from datetime import datetime
import pytz

def translate_word():
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%H:%M')

    # Check for time restrictions
    if "21:00" <= current_time <= "22:00":
        messagebox.showerror("Error", "Service unavailable between 9 PM to 10 PM IST.")
        return

    word = entry.get().strip()
    
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word to translate.")
        return
    
    # Check if the word starts with a vowel
    if word[0].lower() in 'aeiou':
        messagebox.showinfo("Exception", f"No translation for words starting with vowels: {word}")
        return

    try:
        # Translate using Googletrans
        translator = Translator()
        translated = translator.translate(word, src='en', dest='hi').text
        label_result.config(text=f'Translation: {translated}')
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Setup GUI
root = Tk()
root.title("English to Hindi Translator")

label = Label(root, text="Enter English word:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Translate", command=translate_word)
button.pack()

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
