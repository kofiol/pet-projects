#      made by psyhik as a pet project for improving skills
#      this project is one of the funniest things ive ever written and continuing to update. this program is made to count characters, symbols, analyze the text and other useful things for seo optimization
#      i started this pet project 14 june 2024
#      last update: 25 july 2024



import tkinter as tk
from tkinter import scrolledtext
import re
from collections import Counter

#     next todo -- make the desing not ugly 

def count_characters(text):
    return len(text)

def count_spaces(text):
    return text.count(' ')

def count_latin_letters(text):
    return sum(1 for char in text if 'a' <= char.lower() <= 'z')

def count_words(text):
    return len(text.split())

def count_special_symbols(text):
    return len(re.findall(r'[^\w\s]', text))

def count_punctuation_marks(text):
    punctuation_mark = '.,;:!?'
    return sum(text.count(sep) for sep in punctuation_mark)

def count_digits(text):
    return sum(1 for char in text if char.isdigit())

def count_numbers(text):
    return len(re.findall(r'\b\d+\b', text))

def count_uppercase(text):
    return sum(1 for char in text if char.isupper() and 'A' <= char <= 'Z')

def count_lowercase(text):
    return sum(1 for char in text if char.islower() and 'a' <= char <= 'z')

def count_sentences(text):
    return len(re.findall(r'[.!?]', text))

def count_paragraphs(text):
    return text.count('\n\n') + 1

def count_frequent_letters(text):
    letters = [char.lower() for char in text if 'a' <= char.lower() <= 'z']
    return Counter(letters).most_common()

def update_counts():
    text = text_area.get("1.0", tk.END).strip()  # Remove trailing newline
    char_count.set(count_characters(text))
    space_count.set(count_spaces(text))
    latin_count.set(count_latin_letters(text))
    word_count.set(count_words(text))
    special_count.set(count_special_symbols(text))
    separator_count.set(count_punctuation_marks(text))
    digit_count.set(count_digits(text))
    number_count.set(count_numbers(text))
    uppercase_count.set(count_uppercase(text))
    lowercase_count.set(count_lowercase(text))
    sentence_count.set(count_sentences(text))
    paragraph_count.set(count_paragraphs(text))
    
    # Update frequent letters list
    frequent_letters = count_frequent_letters(text)
    frequent_letters_str = ', '.join(f"{letter}: {count}" for letter, count in frequent_letters)
    frequent_letters_count.set(frequent_letters_str)
    
    # Schedule the next update
    root.after(300, update_counts)

root = tk.Tk()
root.title("Text Analysis")

char_count = tk.StringVar()
space_count = tk.StringVar()
latin_count = tk.StringVar()
word_count = tk.StringVar()
special_count = tk.StringVar()
separator_count = tk.StringVar()
digit_count = tk.StringVar()
number_count = tk.StringVar()
uppercase_count = tk.StringVar()
lowercase_count = tk.StringVar()
sentence_count = tk.StringVar()
paragraph_count = tk.StringVar()
frequent_letters_count = tk.StringVar()

tk.Label(root, text="Text Analysis", font=("Helvetica", 16)).pack()

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

tk.Button(root, text="Start Updates", command=lambda: root.after(300, update_counts)).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="characters:").grid(row=0, column=0, sticky='e')
tk.Label(frame, textvariable=char_count).grid(row=0, column=1, sticky='w')
tk.Label(frame, text="spaces:").grid(row=1, column=0, sticky='e')
tk.Label(frame, textvariable=space_count).grid(row=1, column=1, sticky='w')
tk.Label(frame, text="latin Letters:").grid(row=2, column=0, sticky='e')
tk.Label(frame, textvariable=latin_count).grid(row=2, column=1, sticky='w')
tk.Label(frame, text="words:").grid(row=3, column=0, sticky='e')
tk.Label(frame, textvariable=word_count).grid(row=3, column=1, sticky='w')
tk.Label(frame, text="special symbols:").grid(row=4, column=0, sticky='e')
tk.Label(frame, textvariable=special_count).grid(row=4, column=1, sticky='w')
tk.Label(frame, text="punctuation marks:").grid(row=5, column=0, sticky='e')
tk.Label(frame, textvariable=separator_count).grid(row=5, column=1, sticky='w')
tk.Label(frame, text="digits:").grid(row=6, column=0, sticky='e')
tk.Label(frame, textvariable=digit_count).grid(row=6, column=1, sticky='w')
tk.Label(frame, text="numbers:").grid(row=7, column=0, sticky='e')
tk.Label(frame, textvariable=number_count).grid(row=7, column=1, sticky='w')
tk.Label(frame, text="uppercase:").grid(row=8, column=0, sticky='e')
tk.Label(frame, textvariable=uppercase_count).grid(row=8, column=1, sticky='w')
tk.Label(frame, text="lowercase:").grid(row=9, column=0, sticky='e')
tk.Label(frame, textvariable=lowercase_count).grid(row=9, column=1, sticky='w')
tk.Label(frame, text="sentences:").grid(row=10, column=0, sticky='e')
tk.Label(frame, textvariable=sentence_count).grid(row=10, column=1, sticky='w')
tk.Label(frame, text="paragraphs:").grid(row=11, column=0, sticky='e')
tk.Label(frame, textvariable=paragraph_count).grid(row=11, column=1, sticky='w')
tk.Label(frame, text="frequent letters:").grid(row=12, column=0, sticky='e')
tk.Label(frame, textvariable=frequent_letters_count).grid(row=12, column=1, sticky='w')

root.mainloop()
