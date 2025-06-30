import tkinter as tk

window = tk.Tk()

# Configure the window
window.title("Capstone Project")  # Set the window title
window.geometry("2000x1000")  # Set the window size (width x height)
window.resizable(True, True)  # Allow the window to be resized
window.attributes('-topmost', True)

#label
welcome_label = tk.Label(
    window,  # The parent window
    window.configure(bg="black"), #default dark theme
    text="Welcome to my app!",  # The text to display
    font=("Arial", 24),  # Font family and size
    fg="white",  # Text color
    bg="black"
)

# Display the label in the window
welcome_label.pack(pady=50) 

# Create a button that closes the application
exit_button = tk.Button(
    window,
    text="Exit Application",
    bg="black",
    fg="white",
    font=("Arial", 18),  # Font family and size
    command=window.destroy  # This function will be called when the button is clicked
)

exit_button.pack(pady=20)

window.mainloop()

