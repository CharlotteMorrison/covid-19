import tkinter
from tkinter import Scale
from mapsource import MapSource
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class GUI:
    def __init__(self):
        self.canvas_widget = None
        # create the maps from data source
        self.df = pd.read_csv('datasets/data/time-series-19-covid-combined.txt')
        self.map_source = MapSource(self.df)

        # create main window- start of program
        self.root = tkinter.Tk()

        # user information (titles, instructions)
        self.root.wm_title('COVID-19 Case Growth')
        self.title = tkinter.Label(text="Covid-19 Interactive Data Explorer")
        self.title.pack(side='top')

        # shape of window
        self.root.geometry('800x700+100+100')

        # initialize map
        self.canvas_widget = self.get_map('0')

        # make the date chooser slider
        self.num_of_dates = self.df['Date'].nunique()
        self.dates = self.df['Date'].unique()
        self.scale = Scale(self.root,
                           label='Drag the slider to move forward in time.',
                           showvalue=0,
                           tickinterval=0,
                           from_=0,
                           to=self.num_of_dates,
                           command=lambda value: self.get_map(value),
                           orient='horizontal',
                           length=800)
        self.scale.pack(side='top')

        # bind escape to close program
        # bind a keystroke to a function
        self.root.bind('<Escape>', self.end_run)

        quit_button = tkinter.Button(text='Quit Explorer', command=self.end_run)
        quit_button.pack(side='bottom', fill='both')

        # creates the frame
        self.frame = tkinter.Frame(self.root)
        self.frame.pack(side='bottom')

        # activate the window-once everything is ready
        self.root.mainloop()

    def get_map(self, event):
        # create the drawing canvas to display the map
        if self.canvas_widget:
            self.canvas_widget.destroy()
        fig = self.map_source.date_world_map(event)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        self.canvas_widget = canvas.get_tk_widget()
        self.canvas_widget.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.root.update()
        return self.canvas_widget

    def end_run(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    GUI()
