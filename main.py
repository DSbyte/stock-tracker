import frontend.stock_trader_tkinter_gui as gui
import tkinter as tk
import constants

#TODO: window and element size
root = tk.Tk()
root.geometry("{}x{}".format(constants.WIDTH, constants.HEIGHT))
app = gui.StockTraderTkinterGui(master=root)
app.mainloop()