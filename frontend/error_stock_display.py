import tkinter as tk

class StockNameErrorLabel(tk.Label) :
    def __init__(self, master, stockName) :
        error_text = "'" + stockName + "' is not a valid stock."
        tk.Label.__init__(self, master, text=error_text, fg="red")    
    