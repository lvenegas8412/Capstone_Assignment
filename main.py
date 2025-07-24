import tkinter as tk
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from features.simple_stats import get_data
from features.theme_switcher import toggle_theme
from features.history_tracker import fetch_weather_history
from config import weatherbit_api_url, wbapi_key



class WeatherDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_theme = 'light'
        self.title("Capstone Project - Weather Dashboard")
        self.geometry('1200x800')
        self.configure(bg='white')
        self.attributes('-topmost', True)
        self.after(1000, lambda: self.attributes('-topmost', False))
        self.current_theme = 'light'


        self.create_widgets()
        self.configure_layout()
        self.create_plot()

    def configure_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)



    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self, text="Let's Find Some Weather!", font=('Courier', 24, 'bold'), bg='white')
        self.title_label.grid(row=0, column=0, columnspan=3, sticky='ew', pady=10)

        # Input Frame
        self.input_frame = tk.LabelFrame(self, text='Input', bg='light gray')
        self.input_frame.grid(row=1, column=0, sticky='nwes', pady=10, padx=10)

        self.input_label = ttk.Label(self.input_frame, text='Enter your City here:')
        self.input_label.grid(row=0, column=0, sticky='w', pady=10)

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.input_frame, textvariable=self.entry_var)
        self.entry.grid(row=0, column=1)

        self.drop_box = ttk.Combobox(self.input_frame, values=['--', 'Last 7 days', 'Last 14 Days', 'Last 30 days'])
        self.drop_box.current(0)
        self.drop_box.grid(row=1, column=1, sticky='w', pady=5, padx=5)

        self.drop_box_label = ttk.Label(self.input_frame, text='Time Range:')
        self.drop_box_label.grid(row=1, column=0, sticky='w', pady=10)

        # Weather Frame
        self.weather_frame = tk.LabelFrame(self, text='CURRENT WEATHER STATS', bg='light gray', padx=10)
        self.weather_frame.grid(row=2, column=1, sticky='nwes', pady=10, padx=10)

        # Weather Labels
        self.date_label = self.make_weather_label('Date: --', 0)
        self.temp_label = self.make_weather_label('Current Temperature: --', 1)
        self.wind_label = self.make_weather_label('Wind Speed: --', 2)
        self.cond_label = self.make_weather_label('Conditions: --', 3)
        self.max_temp_label = self.make_weather_label('Max Temp: --', 4)
        self.rain_label = self.make_weather_label('Rain: --', 5)
        self.snow_label = self.make_weather_label('Snow: --', 6)

        # Weather Icon
        self.weather_icon_label = tk.Label(self.weather_frame, bg= 'light gray')
        self.weather_icon_label.grid(row=7, column=0, rowspan=2, padx=10, pady=10)


        # Button Frame
        self.button_frame = tk.Frame(self, padx=10)
        self.button_frame.grid(row=1, column=1, sticky='nwes', pady=10, padx=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.update_button = tk.Button(
            self.button_frame, text='Update', bg='light gray',
            command=self.update_weather
        )
        self.update_button.grid(row=0, column=0, columnspan=2, sticky='we', pady=10, padx=10)

        self.clear_button = tk.Button(
            self.button_frame, text='Clear', bg='light gray', command=self.refresh_fields
        )
        self.clear_button.grid(row=1, column=0, sticky='we', pady=10, padx=10)

        self.theme_button = tk.Button(
            self.button_frame, text='Change Theme: (Dark/Light)', bg='light gray',
            command=self.toggle_theme 
        )
        self.theme_button.grid(row=2, column=0, sticky='we', pady=10, padx=10)

        # Visualization Frame
        self.viz_frame = ttk.LabelFrame(self, text='Weather History Tracker')
        self.viz_frame.grid(row=2, column=0, sticky='nwes', padx=10, pady=10)

    def toggle_theme(self):
        toggle_theme(self)
        
    def make_weather_label(self, text, row):
        label = tk.Label(self.weather_frame, text=text, bg='light grey')
        label.grid(row=row, column=0, sticky='w', pady=5)
        return label

    def refresh_fields(self):
        self.drop_box.current(0)
        self.entry.delete(0, tk.END)
        self.temp_label.config(text='Current Temperature: --')
        self.wind_label.config(text='Wind Speed: --')
        self.cond_label.config(text='Conditions: --')
        self.max_temp_label.config(text='Max Temp: --')
        self.rain_label.config(text='Rain: --')
        self.snow_label.config(text='Snow: --')
        self.date_label.config(text='Date: --')
        self.weather_icon_label.config(image='')

    def update_weather(self):

        # Update current weather
        get_data(self.entry, self.temp_label, self.cond_label,
                self.wind_label, self.max_temp_label,
                self.rain_label, self.snow_label, self.date_label, self.weather_icon_label)

        city = self.entry_var.get().strip()
        if not city:
            print("City is empty.")
            return

        # Time range mapping
        time_range_map = {
            'Last 7 days': 7,
            'Last 14 Days': 14,
            'Last 30 days': 30
        }

        selected = self.drop_box.get()
        days = time_range_map.get(selected)

        if not days:
            print("Invalid or no time range selected.")
            return

        # Fetch weather history and plot
        history = fetch_weather_history(city, days)
        if history:
            self.update_plot_data(history)
        else:
            print("No data to plot.")

            

    def create_plot(self):
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_plot_data(self, weather_history: list):
        self.plot.clear()
        dates = [entry['date'] for entry in weather_history]
        temps = [entry['temp'] for entry in weather_history]

        self.plot.plot(dates, temps, marker='o', linestyle='-', color='blue')
        self.plot.set_title('Historical Temperature')
        self.plot.set_xlabel('Date')
        self.plot.set_ylabel('Temperature (°C)')
        self.plot.tick_params(axis='x', rotation=45)
        self.plot.grid(True)
        self.figure.tight_layout()
        self.canvas.draw()

        


if __name__ == "__main__":
    app = WeatherDashboard()
    app.mainloop()

