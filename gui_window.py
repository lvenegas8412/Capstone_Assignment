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
root.grid_columnconfigure(0, weight=1)

#Title Window
title_label = tk.Label(
    root,
    text = 'Lets Find Some Weather!',
    font = ('Courier', 24),
    bg = 'white',
    fg = 'black')
title_label.grid(row=0, column=0, sticky='we', pady=10 )

#Input Frame
input_frame = ttk.LabelFrame(root, text='Input', padding=10)
input_frame.grid(row=1, column=0, sticky='we', pady=10, padx=10)
#Input Label
input_label = ttk.Label(input_frame, text='Enter your City here:')
input_label.grid(row=0, column=0)
#Input_Data
entry = ttk.Entry(input_frame)
entry.grid(row=0 , column=1)


# style = ttk.Style()
# style.configure('Custom.TLabelframe', background='gray')
# style.configure('Custom.TLabelframe.Label', background='gray')  # For the label text bg

# input_frame = ttk.LabelFrame(root, text='INPUT', padding=10, style='Custom.TLabelframe')




root.mainloop()
