import constants

def reconfigure_grid_cols_rows(frame) :
    grid_size = frame.grid_size()
    for x in range(0, grid_size[0]) :
        frame.grid_columnconfigure(x, weight=1)
    for y in range(0, grid_size[1]) :
        frame.grid_rowconfigure(y, weight=1)
    frame.grid(sticky=constants.CENTERED)
    return frame