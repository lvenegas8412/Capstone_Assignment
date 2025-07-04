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
root.after(100, lambda: root.attributes('-topmost', False)) 
root.configure(bg='white')

root.grid_columnconfigure(1, weight=1) 
root.rowconfigure(2, weight=1)
    


#Title Window
title_label = tk.Label(
    root,
    text = 'Lets Find Some Weather!',
    font = ('Courier', 24, 'bold'),
    bg = 'white',
    fg = 'black')
title_label.grid(row=0, column=0, columnspan=3, sticky='ew', pady=10 )
root.grid_columnconfigure(0, weight=1)

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
entry_var = tk.StringVar()
entry = ttk.Entry(input_frame, textvariable=entry_var)
entry.grid(row=0 , column=1)


#DROP_BOX
drop_box = ttk.Combobox(
    input_frame,
    values=['--','Last 7 days', 'Last 14 Days', 'Last 30 days']
)

drop_box.current(0) #default
drop_box.grid(row=1, 
              column=1, 
              sticky='w', 
              pady=5, padx=5)

#DROP_BX_LABEL
drop_box_label = ttk.Label(
    input_frame,
    text='Time Range:').grid(
    row=1, column=0,
    sticky = 'w',
    pady=10
      )

#CURRENT_WEATHER_FRAME
weather_frame = tk.LabelFrame(
    root,
    text='Current Weather Conditions',
    padx=10,
    bg='light gray')
weather_frame.grid(
    row=2,
    column=1,
    sticky='nwes',
    pady=10,
    padx=10)


#CURRENT_WEATHER_LABELS
temp_label = tk.Label(
    weather_frame,
    text='Temperature: --', bg='light grey')
temp_label.grid(row=0,column=0,
                sticky='w', 
                pady=5)

precip_label = tk.Label(
    weather_frame,
    text='Precipitation: --', bg='light grey')
precip_label.grid(row=1, column=0,
    sticky='w', 
    pady=5)

cond_label = tk.Label(
    weather_frame,
    text='Conditions: --', bg='light grey')
cond_label.grid(row=2,column=0, 
    sticky='w', 
    pady=5)

#BUTTONS
button_frame = tk.Frame(root, padx=10)
button_frame.grid(row=1, column=1,
                  sticky = 'nwes',
                  pady=10,
                  padx=10) 
button_frame.grid_columnconfigure(0,weight=1)

update_button = tk.Button(button_frame, text='Update', bg='light gray')
update_button.grid(row=0, column=0, columnspan=2,sticky='we', pady=10, padx=10)

clear_button = tk.Button(button_frame, text='Clear', bg='light gray')
clear_button.grid(row=1, column=0, sticky='we', pady=10, padx=10)

theme_button = tk.Button(button_frame, text='Change Theme: (Dark/Light)', bg='light gray')
theme_button.grid(row=2, column=0, sticky='we', pady=10, padx=10)

#VISUALIZATION
viz_frame = ttk.LabelFrame(root, text='Wheather History Tracker')
viz_frame.grid(row=2, column=0, sticky='nwes', padx=10, pady=10)

figure = Figure(figsize=(8, 4), dpi=100)
plot = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, viz_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)





root.mainloop()
