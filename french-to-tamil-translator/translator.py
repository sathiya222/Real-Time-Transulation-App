import tkinter as tk

# Updated dictionary for 5-letter French to Tamil translation
translation_dict = {
    "heure": "மணி",
    "bleus": "நீல",
    "porte": "வாசல்",
    "livre": "புத்தகம்",
    "table": "மேசை"
}

def translate():
    french_word = entry.get().strip().lower()  # Convert to lowercase and strip any extra spaces
    if len(french_word) == 5:
        tamil_word = translation_dict.get(french_word, "Not Found")
    else:
        tamil_word = "Invalid (Not 5 letters)"
    output_label.config(text=tamil_word)

# Set up the GUI
root = tk.Tk()
root.title("French to Tamil Translator")

tk.Label(root, text="Enter 5-letter French word:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Translate", command=translate).pack()
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
