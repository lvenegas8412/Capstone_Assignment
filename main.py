import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from features.simple_stats import get_data
from features.theme_switcher import toggle_theme
from features.history_tracker import fetch_weather_history
from config import weatherbit_api_url, wbapi_key
from features.team_feature import team_feature



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

        # Store city suggestions (this can be a predefined list or fetched from an API)
        self.city_suggestions = ["New York City", "Los Angeles", "Oxnard", "Chicago", "San Francisco", "Boston", "Dallas", "Miami", "Seattle", "St. Louis"]


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
        self.input_frame = tk.LabelFrame(self, text='DASHBOARD', bg='light gray')
        self.input_frame.grid(row=1, column=0, sticky='nwes', pady=10, padx=10)

        self.input_label = ttk.Label(self.input_frame, text='Select City:')
        self.input_label.grid(row=0, column=0, sticky='w', pady=5)

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.input_frame, textvariable=self.entry_var)
        self.entry.grid(row=1, column=0, sticky='we',pady=5)

        self.suggestion_listbox = tk.Listbox(self.input_frame, height=1, width=15)
        self.suggestion_listbox.grid(row=0, column=2, pady=5, padx=5, sticky='w')
        self.suggestion_listbox.grid_forget()  # Hide it initially

            # Bind the entry widget to update suggestions
        self.entry.bind('<KeyRelease>', self.update_suggestions)

        self.drop_box = ttk.Combobox(self.input_frame, values=['--', 'Last 7 days', 'Last 14 Days', 'Last 30 days'])
        self.drop_box.current(0)
        self.drop_box.grid(row=1, column=2, sticky='we', pady=5, padx=5)

        self.drop_box_label = ttk.Label(self.input_frame, text='Time Range:')
        self.drop_box_label.grid(row=0, column=2, pady=5)

        self.plot_label = ttk.Label(self.input_frame, text='Let''s plot it!')
        self.plot_label.grid(row=0, column=3, pady=10)

        self.compare_label = ttk.Label(self.input_frame, text='Weather on holidays for each team member')
        self.compare_label.grid(row=0, column=4, pady=10,)
        self.compare_label.columnconfigure(4, weight=1)
        

        # Weather Frame
        self.weather_frame = tk.LabelFrame(self, text='CURRENT WEATHER STATS', bg='light gray', padx=10)
        self.weather_frame.grid(row=2, column=1, sticky='nwes', pady=10, padx=10)

        # Weather Labels
        self.city_name_label = self.make_weather_label('City: --', 0)
        self.date_label = self.make_weather_label('Date: --', 1)
        self.temp_label = self.make_weather_label('Current Temperature: --', 2)
        self.wind_label = self.make_weather_label('Wind Speed: --', 3)
        self.cond_label = self.make_weather_label('Conditions: --', 4)
        self.max_temp_label = self.make_weather_label('Max Temp: --', 5)
        self.rain_label = self.make_weather_label('Rain: --', 6)
        self.snow_label = self.make_weather_label('Snow: --', 7)

        # Weather Icon
        self.weather_icon_label = tk.Label(self.weather_frame, bg= 'light gray')
        self.weather_icon_label.grid(row=8, column=0, rowspan=2, padx=10, pady=10)


        # Button Frame
        self.button_frame = tk.Frame(self, padx=10)
        self.button_frame.grid(row=1, column=1, sticky='nwes', pady=10, padx=10)
        self.button_frame.grid_columnconfigure(0, weight=1)

        self.update_button = tk.Button(
            self.input_frame, text='Update', bg='light gray',
            command=self.update_weather
        )
        self.update_button.grid(row=1, column=3, sticky='w', pady=10, padx=10)

        self.clear_button = tk.Button(
            self.button_frame, text='Refresh', bg='light gray', command=self.refresh_fields
        )
        self.clear_button.grid(row=1, column=0, sticky='we', pady=10, padx=10)

        self.theme_button = tk.Button(
            self.button_frame, text='Change Theme: (Dark/Light)', bg='light gray',
            command=self.toggle_theme 
        )
        self.theme_button.grid(row=2, column=0, sticky='we', pady=10, padx=10)

        self.team_button = tk.Button(
            self.input_frame, text='Compare Weather', bg='light gray',
            command=team_feature
        )

        self.team_button.grid(row=1, column=4, sticky='we', pady=10, padx=10)
        self.input_frame.columnconfigure(4, weight=1)
        

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
        self.city_name_label.config(text='City: --')
        self.temp_label.config(text='Current Temperature: --')
        self.wind_label.config(text='Wind Speed: --')
        self.cond_label.config(text='Conditions: --')
        self.max_temp_label.config(text='Max Temp: --')
        self.rain_label.config(text='Rain: --')
        self.snow_label.config(text='Snow: --')
        self.date_label.config(text='Date: --')
        self.weather_icon_label.config(image='')
        self.plot.clear()

    def update_suggestions(self, event):
        city = self.entry_var.get().lower()

        # Only show suggestions if there's at least 2 characters typed
        if len(city) < 2:
            self.suggestion_listbox.grid_forget()  # Hide suggestions if input is too short
            return

        # Filter city suggestions based on input
        suggestions = [city_name for city_name in self.city_suggestions if city in city_name.lower()]

        # Update suggestion listbox
        self.suggestion_listbox.delete(0, tk.END)

        for suggestion in suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

        if suggestions:
            self.suggestion_listbox.grid(row=2, column=0, pady=10, padx=5, sticky='w')  # Show suggestions
        else:
            self.suggestion_listbox.grid_forget()  # Hide if no suggestions

        # Bind an event for selecting a suggestion
        self.suggestion_listbox.bind("<ButtonRelease-1>", self.select_suggestion)

    def select_suggestion(self, event):
        # Set entry text to the selected suggestion
        selected_city = self.suggestion_listbox.get(self.suggestion_listbox.curselection())
        self.entry_var.set(selected_city)
        self.suggestion_listbox.grid_forget()  # Hide suggestions after selection

    def update_weather(self):

        # Update current weather in Simple Stats
        get_data(self.entry, self.city_name_label, self.temp_label, self.cond_label,
                self.wind_label, self.max_temp_label,
                self.rain_label, self.snow_label, self.date_label, self.weather_icon_label)

        city = self.entry_var.get()
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

        if not history:
            print("Invalid city or no data found.")
            return  # 👈 This stops further execution
        print(history)
        
        self.update_plot_data(history)


            

    def create_plot(self):
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_plot_data(self, weather_history: list):
        city = self.entry_var.get()
        self.plot.clear()
        dates = [entry['date'] for entry in weather_history]
        temps = [entry['temp'] for entry in weather_history]

        self.plot.plot(dates, temps, marker='o', linestyle='-', color='blue')
        self.plot.set_title(f'Historical Temperature - {city}')
        self.plot.set_xlabel('Date')
        self.plot.set_ylabel('Temperature (°F)')
        self.plot.tick_params(axis='x', rotation=45)
        self.plot.grid(True)
        self.figure.tight_layout()
        self.canvas.draw()

        


if __name__ == "__main__":
    app = WeatherDashboard()
    app.mainloop()

