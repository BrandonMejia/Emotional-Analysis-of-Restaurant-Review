import nlu
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

score = '-'
sentiment = '-'

def analyze(text):
    global score, sentiment
    response = nlu.getSentiment(text)
    score = response['sentiment']['document']['score']
    sentiment = response['sentiment']['document']['label']
    scoreValue.configure(text=score)
    sentimentValue.configure(text=sentiment)

def clear():
    textarea.delete("1.0", tk.END)
    scoreValue.configure(text='-')
    sentimentValue.configure(text='-')

root.title("Analisis de Sentimiento de comentarios de restaurante")
root.geometry("800x600")
title = tk.Label(root, text="Comente sobre nuestra comida")
textarea = tk.Text(root, height=10, width=100)
actionsFrame = ttk.Frame(root)
analyzeBtn = tk.Button(actionsFrame, text="Analizar", width=10, command=lambda: analyze(textarea.get("1.0", tk.END)))
clearBtn = tk.Button(actionsFrame, text="Limpiar", width=10, command=clear)
resultHeader = tk.Label(root, text="Resultado")
resultFrame = ttk.Frame(root)
scoreLabel = tk.Label(resultFrame, text="Puntaje: ")
scoreValue = tk.Label(resultFrame, text=score)
sentimentLabel = tk.Label(resultFrame, text="Etiqueta: ")
sentimentValue = tk.Label(resultFrame, text=sentiment)

authors = tk.Text(root, state='disabled', width=44, height=7)
authors .configure(state='normal')
authors .insert('end', ' \t  -- Integrantes -- \n 1) Ruiz Castro Renzo \n 2) Rojas Miñan Alexis Luis \n 3) Mamani Acurio Alex Sebastian \n 4) Martinez Bravo Martin Aaron \n 5) Mejia Tarazona Brandon')
authors .configure(state='disabled')
authors.place

title.pack()
textarea.pack()
actionsFrame.pack()
analyzeBtn.grid(row=0, column=0, padx=5, pady=10)
clearBtn.grid(row=0, column=1, padx=5, pady=10)

resultHeader.pack()
resultFrame.pack()
scoreLabel.grid(row=0, column=0)
scoreValue.grid(row=0, column=1)
sentimentLabel.grid(row=1, column=0)
sentimentValue.grid(row=1, column=1)

authors.pack(pady=30)

root.mainloop()