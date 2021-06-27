import frontend.stock_trader_tkinter_gui as gui
import tkinter as tk

#TODO: window and element size
root = tk.Tk()
app = gui.StockTraderTkinterGui(master=root)
app.mainloop()