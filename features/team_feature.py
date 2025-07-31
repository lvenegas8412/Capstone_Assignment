import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np



def team_feature():

    df = pd.read_csv('team_weather_data.csv', parse_dates=['date'])
    df['max_temp_f'] = df['max_temp'] * 9/5 + 32

    holidays = {
        'New Year\'s Day': '2025-01-01',
        'Independence Day': '2024-07-04',
        'Thanksgiving': '2024-11-28',
        'Christmas': '2024-12-25',
        'Memorial Day': '2025-05-27'
    }
    holidays = {name: pd.to_datetime(date) for name, date in holidays.items()}

    holiday_temps = []
    for holiday, date in holidays.items():
        day_data = df[df['date'] == date].copy()
        day_data['holiday'] = holiday
        holiday_temps.append(day_data)

    holiday_df = pd.concat(holiday_temps)

    pivot = holiday_df.pivot(index='holiday', columns='city', values='max_temp_f')

    holidays = pivot.index.tolist()
    cities = pivot.columns.tolist()

    x = np.arange(len(holidays))

    # 1. Set bar width based on number of cities so they fit nicely
    width = 0.8 / len(cities)  # total group width ~0.8, divide among cities

    person_names = {
        'Selmer': 'Andrea',
        'Oxnard': 'Luis',
        'Atlanta': 'Brett',
        'Bronx': 'Mark',
        'Queens': 'Merhanda',
        'Clearwater': 'Sarina'
    }

    fig, ax = plt.subplots(figsize=(14, 10))  # wider figure for clarity

    for i, city in enumerate(cities):
        temps = pivot[city].values
        bars = ax.bar(x + i * width, temps, width=width, label=city)

        for j, bar in enumerate(bars):
            height = bar.get_height()
            ax.annotate(
                person_names.get(city, city),  # get the person's name
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center',
                va='bottom',
                fontsize=9,
                rotation=90,
                color='black'
            )

    ax.set_xticks(x + width * (len(cities) - 1) / 2)
    ax.set_xticklabels(holidays, rotation=45, ha='right')

    ax.set_ylabel("Temperature (°F)")
    ax.set_title("Temperature on Major Holidays for Each Team Members City (2024-2025)")
    ax.legend(title="City")

    plt.tight_layout()
    plt.show()









