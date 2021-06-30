import constants 
import tkinter as tk
from backend import stock_display as sd
from . import error_stock_display as esd

class CompareStocksScreen(tk.Frame) :
    def __init__(self, master) :
        tk.Frame.__init__(self, master)
        self.master = master
        self.start()
        
    def start(self) :
        self.max_row_size = len(constants.TIME_PERIODS)
        self.mid = int(self.max_row_size / 2) - 1

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, self.max_row_size):
            tk.Radiobutton(self.master, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row=i, column=2, sticky=tk.W)
            
        self.stockThis = self.build_stock_layout(0, "Stock 1")
        self.stockOther = self.build_stock_layout(1, "Stock 2")
        
        compare_button = tk.Button(self.master,
                                   text = "COMPARE",
                                   fg = "green",
                                   command=self.search_ticker).grid(row=self.max_row_size - 1, 
                                                                    column=0, columnspan=2,
                                                                    sticky=tk.E+tk.W)
            
    def build_stock_layout(self, col_to_build, label_text) :
        label = tk.Label(self.master, text=label_text).grid(row=0, column=col_to_build)
        stock_entry = tk.Entry(self.master)
        stock_entry.grid(row=self.mid, column=col_to_build, sticky=tk.S+tk.N+tk.W+tk.E)
        return stock_entry
            
    def search_ticker(self) :
        stock_name_this = self.stockThis.get()
        try :
            data = sd.StockDisplay(stock_name_this, constants.TIME_PERIODS[0])
        except ValueError :
            stock_error_label = esd.StockNameErrorLabel(self.master, stock_name_this)
            stock_error_label.grid(row=self.mid+1, column=0)
        
        stock_name_other = self.stockOther.get()
        try :
            data = sd.StockDisplay(stock_name_other, constants.TIME_PERIODS[0])
        except ValueError :
            stock_error_label = esd.StockNameErrorLabel(self.master, stock_name_other)
            stock_error_label.grid(row=self.mid+1, column=1)
        