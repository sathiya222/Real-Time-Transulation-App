import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Define the supported languages
supported_languages = ['en', 'fr', 'hi']
language_list = [LANGUAGES[lang_code] for lang_code in supported_languages]
languages = {v: k for k, v in LANGUAGES.items() if k in supported_languages}

def trans_late():
    txt2.delete(1.0, tk.END)
    try:
        from_language = c1.get()
        to_language = c2.get()

        if not from_language or not to_language:
            messagebox.showerror("Error", "Please select both source and target languages.")
            return

        text_to_translate = txt1.get(1.0, tk.END).strip()
        if not text_to_translate:
            messagebox.showerror("Error", "Please enter text to translate.")
            return

        from_language_key = languages[from_language]
        to_language_key = languages[to_language]

        translator = Translator()
        translated_text = translator.translate(text_to_translate, src=from_language_key, dest=to_language_key)

        txt2.insert(1.0, translated_text.text)

    except KeyError as e:
        messagebox.showerror("Error", f"Invalid language: {e}")
    except Exception as e:
        messagebox.showerror("Translator Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.geometry("700x400")
root.title("Language Translator")
root.config(bg='#D3D3D3')

# Header label
tk.Label(root, text="Language Translator", font=('Arial', 20, 'bold'), bg='#8B8B7A', fg='White', width=50, pady=5).pack(pady=10)

# Frames
f1 = tk.Frame(root, bg='white', bd=5)
f1.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.5)
f2 = tk.Frame(root, bg='white', bd=5)
f2.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.5)

# Text boxes
txt1 = tk.Text(f1, font=('Arial', 12, 'bold'))
txt1.pack(expand=True, fill=tk.BOTH)
txt2 = tk.Text(f2, font=('Arial', 12, 'bold'))
txt2.pack(expand=True, fill=tk.BOTH)

# Combo boxes
c1 = ttk.Combobox(root, values=language_list, font=('Arial', 12, 'bold'), width=20)
c1.place(relx=0.1, rely=0.8)
c1.set(language_list[0])  # Set default language

c2 = ttk.Combobox(root, values=language_list, font=('Arial', 12, 'bold'), width=20)
c2.place(relx=0.55, rely=0.8)
c2.set(language_list[1])  # Set default language

# Translate button
btn = tk.Button(root, text="Translate", font=('Arial', 15, 'bold'), bd=5, bg='#8B8B7A', fg='White', command=trans_late)
btn.place(relx=0.35, rely=0.9, anchor='center')

root.mainloop()
