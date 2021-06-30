import constants 
import tkinter as tk
from . import error_stock_display as esd

class CompareStocksScreen(tk.Frame) :
    def __init__(self, master) :
        tk.Frame.__init__(self, master)
        self.master = master
        self.start()
        
    def start(self) :
        self.max_row_size = len(constants.TIME_PERIODS)
        
        self.stock_entry = tk.Entry(self.master)
        self.stock_entry.grid(row=1, column=0, sticky=tk.S+tk.N+tk.W+tk.E)

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, self.max_row_size):
            tk.Radiobutton(self.master, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row=i, column=2, sticky=tk.W)
            
        self.build_stock_layout(0, "Stock 1")
        self.build_stock_layout(1, "Stock 2")
        
        compare_button = tk.Button(self.master,
                                   text = "COMPARE",
                                   fg = "green",
                                   command=self.search_ticker).grid(row=3, column=0, columnspan=2,
                                                                   sticky=tk.E+tk.W)
            
    def build_stock_layout(self, col_to_build, label_text) :
        tk.Label(self.master, text=label_text).grid(row=0, column=col_to_build)
        self.stock_entry = tk.Entry(self.master)
        self.stock_entry.grid(row=1, column=col_to_build, sticky=tk.S+tk.N+tk.W+tk.E)
            
    def search_ticker(self) :
        try :
            self.data, self.indicator = si.StockIndicators(self.stock_entry.get(),
                                                          ).stockIndicators()
        except ValueError :
            error_label = esd.StockNameErrorLabel(self.stock_entry.get())
            error_label.grid(row=(self.max_row_size / 2) + 2, column=0)
        