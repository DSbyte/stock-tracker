import tkinter as tk

class StockTraderTkinterGui(tk.Frame) :
    def __init__(self, master=None) :
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self) :
        self.create_menu()
        
        self.quit = tk.Button(self, text="QUIT", fg = "red",
                             command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def create_menu(self) :
        self.track_stock_button         = tk.Button(self, text="Track Stock",
                                           command=self.start_track_stock_menu)
        self.track_stock_button.pack()
        
        self.stock_indicators_button    = tk.Button(self, text="Stock Indicators",
                                                   command=
                                                    self.start_stock_indicators_menu) 
        self.stock_indicators_button.pack()
        
        self.compare_stocks_button      = tk.Button(self, text="Compare Stocks",
                                                   command=
                                                   self.start_compare_stocks_menu)
        self.compare_stocks_button.pack();
        
    def start_track_stock_menu(self) :
        print("stub")
        
    def start_stock_indicators_menu(self) :
        print("stub")
        
    def start_compare_stocks_menu(self) :
        print("stub")
        

        