import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



#Creating GUI Window
root = tk.Tk()
root.geometry('1200x800')
root.title('Capstone Project - Weather Dashboard')
root.attributes('-topmost', True)
root.configure(bg='white')

root.grid_columnconfigure(1, weight=1) 
    


#Title Window
title_label = tk.Label(
    root,
    text = 'Lets Find Some Weather!',
    font = ('Courier', 24, 'bold'),
    bg = 'white',
    fg = 'black')
title_label.grid(row=0, column=0, sticky='nwes', pady=10 )

#Input_Frame
input_frame = tk.LabelFrame(
    root,
    text='Input',
    bg='light gray')
input_frame.grid(
    row=1, 
    column=0, 
    sticky='nwes', 
    pady=10, 
    padx=10
    )



#Input_Label
input_label = ttk.Label(
    input_frame, 
    text='Enter your City here:')
input_label.grid(
    row=0, 
    column=0, 
    sticky='w',
    pady=10
    )

#Input_Entry
entry_var = tk.StringVar(value='--')
entry = ttk.Entry(input_frame, textvariable=entry_var)
entry.grid(row=0 , column=1)


#Drop_Box
drop_box = ttk.Combobox(
    input_frame,
    values=['--','Last 7 days', 'Last 14 Days', 'Last 30 days']
)

drop_box.current(0) #default
drop_box.grid(row=1, 
              column=1, 
              sticky='w', 
              pady=5, padx=5)

#Drop_Box_Label
drop_box_label = ttk.Label(
    input_frame,
    text='Time Range:').grid(
    row=1, column=0,
    sticky = 'w',
    pady=10
      )

#Current_Weather_Frame
weather_frame = tk.LabelFrame(
    root,
    text='Current Weather Conditions',
    padx=10,
    bg='light gray')
weather_frame.grid(
    row=1,
    column=1,
    sticky='nwes',
    pady=10,
    padx=10)


#Current_Weather_Labels
temp_label = tk.Label(
    weather_frame,
    text='Temperature: --')
temp_label.grid(row=0, column=0, 
                sticky='w', 
                pady=5)



root.mainloop()
