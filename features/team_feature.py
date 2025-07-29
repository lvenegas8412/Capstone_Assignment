import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


# Load CSV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots(figsize=(14, 7))  # wider figure for clarity

for i, city in enumerate(cities):
    temps = pivot[city].values
    bars = ax.bar(x + i * width, temps, width=width, label=city)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            person_names.get(city, city),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center',
            va='bottom',
            fontsize=9,
            rotation=90
        )
        ax.annotate(
            f"{height:.1f}°F",  # formatted to 1 decimal place
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, -50),  # move label downward into the bar
            textcoords="offset points",
            ha='center',
            va='top',  # anchor to top so text goes down into the bar
            fontsize=8,
            color='black'  # good contrast for dark bars
        )

ax.set_xticks(x + width * (len(cities) - 1) / 2)
ax.set_xticklabels(holidays, rotation=45, ha='right')


ax.set_ylabel("Temperature (°F)")
ax.set_title("Temperature on Major Holidays (2024)")
ax.legend(title="City")


plt.tight_layout()
plt.show()






# Pivot for plotting
# pivot = holiday_df.pivot(index='holiday', columns='city', values='max_temp_f')

# # Plotting

# # pivot.T.plot(kind='line', marker='o', figsize=(10, 6))
# # plt.xticks(rotation=45)


# pivot.plot(kind='bar', figsize=(10, 6))
# plt.title('Temperature on Major Holidays (2024)')
# plt.ylabel('Temperature (°F)')
# plt.xlabel('Holiday')
# plt.xticks(rotation=45)
# plt.legend(title='City')
# plt.tight_layout()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt

# # Step 1: Read the CSV
# df = pd.read_csv("team_weather_data.csv", parse_dates=['date'])

# # Step 2: Convert max temp to Fahrenheit
# df['max_temp_f'] = df['max_temp'] * 9/5 + 32

# # Step 3: Define holidays
# holidays = {
#     "New Year's Day": '2025-01-01',
#     "Memorial Day": '2025-05-27',
#     "Independence Day": '2024-07-04',
#     "Thanksgiving": '2024-11-28',
#     "Christmas": '2024-12-25'
# }
# holidays = {name: pd.to_datetime(date) for name, date in holidays.items()}

# # Step 4: Filter for holiday rows
# holiday_data = df[df['date'].isin(holidays.values())].copy()

# # Add holiday names to each row
# holiday_data['holiday'] = holiday_data['date'].map({v: k for k, v in holidays.items()})

# # Step 5: Get list of cities and holidays for plotting
# cities = holiday_data['city'].unique()
# holiday_names = list(holidays.keys())

# # Step 6: Plot — grouped bar chart
# import numpy as np

# x = np.arange(len(holiday_names))  # label locations
# width = 0.15  # width of each bar

# fig, ax = plt.subplots(figsize=(10, 6))

# for i, city in enumerate(cities):
#     temps = []
#     labels = []

#     for h in holiday_names:
#         row = holiday_data[(holiday_data['city'] == city) & (holiday_data['holiday'] == h)]
#         if not row.empty:
#             temp_f = row.iloc[0]['max_temp_f']
#             temps.append(temp_f)
#             labels.append(f"{temp_f:.1f}°F")
#         else:
#             temps.append(0)  # Draw a 0-height bar
#             labels.append("N/A")

#     # Plot bars
#     bars = ax.bar(x + i*width, temps, width, label=city)

#     # Add temperature labels on top of bars
#     for bar, label in zip(bars, labels):
#         height = bar.get_height()
#         ax.annotate(
#             label,
#             xy=(bar.get_x() + bar.get_width() / 2, height),
#             xytext=(0, 3),  # 3 points above the bar
#             textcoords="offset points",
#             ha='center', va='bottom',
#             fontsize=8
#         )


# # Final touches
# ax.set_title("Max Temperature (°F) on Major Holidays by City (2024)")
# ax.set_ylabel("Temperature (°F)")
# ax.set_xticks(x + width*(len(cities)-1)/2)
# ax.set_xticklabels(holiday_names, rotation=45)
# ax.legend(title="City")
# plt.tight_layout()
# plt.show()





