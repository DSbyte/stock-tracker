import constants 
import tkinter as tk

class StockIndicatorsScreen(tk.Frame) :
    def __init__(self, master) :
        tk.Frame.__init__(self, master)
        self.master = master
        self.start()
        
    def start(self) :
        max_row_size = len(constants.STOCK_INDICATORS)
        
        self.stock_entry = tk.Entry(self.master)
        self.stock_entry.grid(row=int(max_row_size / 2) - 1, 
                              column=0, sticky=tk.S+tk.N+tk.W+tk.E)

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, len(constants.TIME_PERIODS)):
            tk.Radiobutton(self.master, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row=int(max_row_size / 2) - 2 + i,
                                                            column=1, sticky=tk.W)
            
        search_button = tk.Button(self.master,
                                 text = "GO",
                                 fg = "green",
                                 command=self.search_ticker).grid(row=int(max_row_size / 2) + 1, 
                                                                  column=0)
        
        self.stock_indicator = tk.StringVar()
        self.stock_indicator.set(0)
        for i in range(0, len(constants.STOCK_INDICATORS)):
            tk.Radiobutton(self.master, text=constants.STOCK_INDICATORS[i].upper(),
                          variable=self.stock_indicator, value=i).grid(row=i, column=2, sticky=tk.W)
            
    def search_ticker(self) :
        # TODO: implement the plotting
        print("stub")
        
        