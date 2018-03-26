import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.ttk import *

from readability import Readability

# window
window = tk.Tk()
window.geometry('625x600')
window.title("Readability Analysis")
sentence_display = tk.StringVar()
word_display = tk.StringVar()
syllable_display = tk.StringVar()
index_display = tk.StringVar()


# routines
def read_file(file_name):
    file_contents = ""
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents


# events
def load_document():
    file_name = filedialog.askopenfilename()
    if file_name:
        document = read_file(file_name)
        if document:
            sctxt.delete(1.0, tk.END)
            sctxt.insert(tk.INSERT, document)


def analyse_document():
    document = sctxt.get(1.0, tk.END)
    read = Readability()
    sentence_count, word_count, syllable_count, index = \
        read.calculate_readability(document)

    global sentence_display
    sentence_display.set("Sentences: " + str(sentence_count))
    global word_display
    word_display.set("Words: " + str(word_count))
    global syllable_display
    syllable_display.set("Syllables: " + str(syllable_count))
    global index_display
    index_display.set("Index: " + "%6.2f" % index)


# document
# scrolledtext
sctxt = tk.scrolledtext.ScrolledText(window, width=60, height=35, padx=5, pady=5, wrap="word")
sctxt.grid(column=0, row=0, rowspan=6, padx=10, pady=10)

# buttons
load = tk.Button(window, text="Load", command=load_document, padx=20, pady=5)
load.grid(column=2, row=0, sticky=tk.W + tk.E + tk.N + tk.S, pady=20)
load.focus()
# button
btn = tk.Button(window, text="Analyse", command=analyse_document)
btn.grid(column=2, row=1, sticky=tk.W + tk.E + tk.N + tk.S)
# labels
sentences = Label(window, textvariable=sentence_display)
sentences.grid(column=2, row=2, sticky=tk.W + tk.E + tk.N + tk.S)
words = Label(window, textvariable=word_display)
words.grid(column=2, row=3, sticky=tk.W + tk.E + tk.N + tk.S)
syllables = Label(window, textvariable=syllable_display)
syllables.grid(column=2, row=4, sticky=tk.W + tk.E + tk.N + tk.S)
flesch_index = Label(window, textvariable=index_display)
flesch_index.grid(column=2, row=5, sticky=tk.W + tk.E + tk.N + tk.S)

# main loop
window.mainloop()
