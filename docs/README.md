# Capstone Assignment - Weather Dashboard
```Welcome to my first real app! This app is designed to allow user to retrieve not only current weather data, but also track historical weather patterns. Want to know what the last 7 days have looked like? HOw about in the last month? This wasy to use interface simplifies searches.```


## Overview
```I have built out a GUI using examples and learning methods from class and assignments.```

## Learninig Objectives

## Assignmet Tasks

``` Feature 1```
SIMPLE STATS

  My first feature is getting current data from a city of your choosing. This request will give us the current temperature, wind speed, conditions, the max temperature of that day, how much rain and/or snow.

``` Feature 2```
LIGHT/DARK THEME SWITCHER

  I chose light/dark theme switcher because I use this often in my own personal use. I feel that being able to switch colors adds a little personalization

``` Feature 3```  HISTORY TRACKER

  I wanted to show patterns of weather data from the last month. I used matplotlib to display the line-graph that can display data from 7 days, 14 days, or 30 days. 

  ``` Team Feature ``` 
  CITY COMPARSIONS FOR TEAM -  

  This bar chart shows comparisons from each of my team member's city for major holidays during the 2024-2025 year. This is a fun visualization to show what each of us was feeling, weather wise, on the same Holiday


## Project File Structure

```
Capstone_Assignment/
│   config.py
│   data.txt
│   main.py
│   requirements.txt
│   
│
├── docs/
│     README.md
│     week_11_reflection.md
│
├── features/
│     history_tracker.py
│     simple_stats.py
│     theme_switcher.py
      team_feature
│
├── screenshots/
│     diagram.pdf
```

## How to Run the Program

3. **Run the Application**
   - In the terminal, execute: This will launch the Weather Dashboard GUI.
     ```
     python main.py
     ```
   - There are 2 input fields and 4 total buttons to chose from
   - For Feature 1:  Simple Stats
     ```
      a. Input a City Name under "Select City"
      b. Hit the Update Button
      c. Current Weather will be displayed on the right side under "Current Weather Stats"
     ```
   - For Feature 2 - History Tracker:
     ```
      a. In addition to selcting a city from Feature 1, select between time range of
         7, 14, or 30 days.
      b. Hit the Update Button under "Let's Plot"
      c. Plot of weather history will be displayed.
     ```
   - For Feature 3 - Theme Switcher:
     ```
     a. Hit the Change Theme button on the upper right hand corner of the GUI
     b. Theme will switch between Light and Dark Mode
     ```  
   - For Team Feature - City Comparison:
     ```
     a. Hit the Compare Weather button under "Weather on holidays for each team member"
     b. A pop-up window will display the bar graph comparing temperature of each person's 
        city on major holidays.
     ```
    
  

## Notes
- All source code is in the root and `features/` directories.
- Documentation and reflections are in the `docs/` folder.
- Screenshots and diagrams are in the `screenshots/` folder.

