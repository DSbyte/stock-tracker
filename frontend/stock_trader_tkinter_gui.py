import tkinter as tk
from backend import stock_display as sd
import constants
from . import stock_indicators_screen as sis
from . import compare_stocks_screen as css
from . import error_stock_display as esd
from . import sizing_helper as sh
    
# TODO: put this into a new file
class TrackStockScreen(tk.Frame) :
    def __init__(self, master) :
        super().__init__(master)
        self.master = master
        self.start()
        for i in range(0, 3) :
            self.master.rowconfigure(i, weight=1)
        self = sh.reconfigure_grid_cols_rows(self)

        
    def start(self) :
        self.max_row_size = len(constants.TIME_PERIODS)
        
        self.stock_entry = tk.Entry(self)
        self.mid = int((self.max_row_size / 2)) - 1;
        self.stock_entry.grid(row=self.mid, column=0, sticky=constants.CENTERED)

        self.var = tk.StringVar()
        self.var.set(0)
        for i in range(0, self.max_row_size):
            tk.Radiobutton(self, text=constants.TIME_PERIODS[i], 
                           variable=self.var, value=i).grid(row=i, column=1, sticky=tk.W)
            
        search_button = tk.Button(self,
                                 text = "GO",
                                 fg = "green",
                                 command=self.search_ticker)
        search_button.grid(row=self.mid + 1, column=0, sticky=constants.CENTERED)
        
        
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
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.create_widgets()
        self.frame=sh.reconfigure_grid_cols_rows(self.frame)
        
    def create_widgets(self) :
        self.create_menu()
        self.quit = tk.Button(self.frame, text="QUIT", fg = "red",
                             command=self.master.destroy)
        self.quit.grid(row=3, column=0, sticky=constants.CENTERED)
        
    def create_menu(self) :
        padding = 50
        
        self.track_stock_button         = tk.Button(self.frame, text="Track Stock",
                                                    command=self.start_track_stock_menu)
        self.track_stock_button.grid(row=0, column=0, sticky=constants.CENTERED, ipady=padding)
        
        self.stock_indicators_button    = tk.Button(self.frame, 
                                                    text="Stock Indicators",
                                                    command=self.start_stock_indicators_menu)
        self.stock_indicators_button.grid(row=1, column=0, sticky=constants.CENTERED, ipady=padding)
        
        self.compare_stocks_button      = tk.Button(self.frame, 
                                                    text="Compare Stocks",
                                                   command=self.start_compare_stocks_menu)
        self.compare_stocks_button.grid(row=2, column=0, sticky=constants.CENTERED, ipady=padding)
                
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

        