import constants 
import tkinter as tk
from backend import stock_indicators as si
from . import error_stock_display as esd

class StockIndicatorsScreen(tk.Frame) :
    def __init__(self, master) :
        tk.Frame.__init__(self, master)
        self.master = master
        self.start()
        
    def start(self) :
        self.max_row_size = len(constants.STOCK_INDICATORS)
        self.mid = int(self.max_row_size / 2) - 1
        
        self.stock_entry = tk.Entry(self.master)
        self.stock_entry.grid(row=self.mid, column=0, sticky=tk.S+tk.N+tk.W+tk.E)

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, len(constants.TIME_PERIODS)):
            tk.Radiobutton(self.master, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row = self.mid - 2 + i,
                                                            column=1, sticky=tk.W)
            
        search_button = tk.Button(self.master,
                                 text = "GO",
                                 fg = "green",
                                 command=self.search_ticker).grid(row=self.mid + 1, column=0)
        
        self.stock_indicator = tk.StringVar()
        self.stock_indicator.set(0)
        for i in range(0, self.max_row_size):
            tk.Radiobutton(self.master, text=constants.STOCK_INDICATORS[i].upper(),
                          variable=self.stock_indicator, value=i).grid(row=i, column=2, sticky=tk.W)
            
    def search_ticker(self) :
        try :
            self.data, self.indicators = si.StockIndicators(self.stock_entry.get(),
                                                           self.var,
                                                           self.stock_indicator).stockIndicators()
        except ValueError :
            stock_label = esd.StockNameErrorLabel(self.master, self.stock_entry.get())
            stock_label.grid(row=self.mid + 2,
                             column=0)
        