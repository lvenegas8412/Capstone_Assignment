import tkinter as tk
from tkinter import ttk

def apply_light_theme(app):
    app.configure(bg='white')
    app.title_label.config(bg='white', fg='black')
    app.weather_frame.config(bg='light gray')
    app.input_frame.config(bg='light gray')
    for label in [app.date_label, app.temp_label, app.wind_label,
                    app.cond_label, app.max_temp_label, app.rain_label, app.snow_label]:
        label.config(bg='light gray', fg='black')

    app.button_frame.config(bg='white')
    app.update_button.config(bg='light gray', fg='black')
    app.clear_button.config(bg='light gray', fg='black')
    app.theme_button.config(bg='light gray', fg='black')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TLabel', background='white', foreground='black')
    style.configure('TButton', background='light gray', foreground='black')

def apply_dark_theme(app):
    app.configure(bg='black')
    app.title_label.config(bg='black', fg='white')
    app.weather_frame.config(bg='gray30')
    app.input_frame.config(bg='gray30')
    for label in [app.date_label, app.temp_label, app.wind_label,
                    app.cond_label, app.max_temp_label, app.rain_label, app.snow_label]:
        label.config(bg='gray30', fg='white')

    app.button_frame.config(bg='black')
    app.update_button.config(bg='gray30', fg='white')
    app.clear_button.config(bg='gray30', fg='white')
    app.theme_button.config(bg='gray30', fg='white')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TLabel', background='black', foreground='white')
    style.configure('TButton', background='gray30', foreground='white')


def toggle_theme(app):
    if getattr(app, 'current_theme', 'light') == 'light':
        app.current_theme = 'dark'
        apply_dark_theme(app)
    else:
        app.current_theme = 'light'
        apply_light_theme(app)


