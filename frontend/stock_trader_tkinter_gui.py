import tkinter as tk
from backend import stock_display as sd
import constants
from . import stock_indicators_screen as sis
from . import compare_stocks_screen as css
from . import error_stock_display as esd
    
# TODO: put this into a new file
class TrackStockScreen(tk.Frame) :
    def __init__(self, master) :
        tk.Frame.__init__(self, master)
        self.master = master
        self.start()
        
    def start(self) :
        self.max_row_size = len(constants.TIME_PERIODS)
        
        self.stock_entry = tk.Entry(self.master)
        self.mid = int((self.max_row_size / 2)) - 1;
        self.stock_entry.grid(row=self.mid, column=0, sticky=tk.S+tk.N+tk.W+tk.E)

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, self.max_row_size):
            tk.Radiobutton(self.master, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row=i, column=1, sticky=tk.W)
            
        search_button = tk.Button(self.master,
                                 text = "GO",
                                 fg = "green",
                                 command=self.search_ticker).grid(row=self.mid + 1,
                                                                  column=0)
        
        
    def search_ticker(self) :
        stock_name = self.stock_entry.get()
        try :
            self.stock_data = sd.StockDisplay(stock_name, self.var).stockData()
        except ValueError :
            error_label = esd.StockNameErrorLabel(self.master, self.stock_entry.get())
            error_label.grid(row=self.mid + 2, column=0)


# TODO: move menu to a new class instead
# TODO: implement the ability to return to the previous menu
class StockTraderTkinterGui(tk.Frame) :
    def __init__(self, master=None) :
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.create_widgets()
        
    def create_widgets(self) :
        self.create_menu()
        self.frame.grid(row=0, column=3)
        self.quit = tk.Button(self, text="QUIT", fg = "red",
                             command=self.master.destroy)
        
    def create_menu(self) :
        self.frame.grid(row=0, column=0)
        self.track_stock_button         = tk.Button(self.frame, text="Track Stock",
                                           command=self.start_track_stock_menu)
        self.track_stock_button.pack()
        
        self.frame.grid(row=0, column=1)
        self.stock_indicators_button    = tk.Button(self.frame, 
                                                    text="Stock Indicators",
                                                    command=
                                                    self.start_stock_indicators_menu) 
        self.stock_indicators_button.pack()
        
        self.frame.grid(row=0, column=2)
        self.compare_stocks_button      = tk.Button(self.frame, 
                                                    text="Compare Stocks",
                                                   command=
                                                   self.start_compare_stocks_menu)
        self.compare_stocks_button.pack();
                
    def switch_to_frame(self, new_frame) :
        self.frame.destroy()
        self.frame = new_frame
        

    def start_track_stock_menu(self) :
        screen = TrackStockScreen(self.master)
        self.switch_to_frame(screen)
        
    def start_stock_indicators_menu(self) :
        self.switch_to_frame(sis.StockIndicatorsScreen(self.master))
        
    def start_compare_stocks_menu(self) :
        self.switch_to_frame(css.CompareStocksScreen(self.master))

        