# Import necessary modules for GUI creation, image processing, making HTTP requests, and handling JSON data
from tkinter import Tk, ttk  # Tkinter for GUI
from tkinter import *  # Additional Tkinter components
from PIL import Image, ImageTk  # Image processing
import requests  # HTTP requests
import json  # JSON data handling

# Define color constants for maintaining a consistent color scheme throughout the application
clr0 = "#FFFFFF"  # White
clr1 = "#000000"  # Black
clr2 = "#4B0082"  # Indigo

# Create the main window with specific dimensions, title, and background color
window = Tk()
window.geometry('300x320')
window.title('Converter')
window.configure(bg=clr0)
window.resizable(height=False, width=False)

# Set up frames within the main window: 'top' for the application title and 'main' for the converter interface
top = Frame(window, width=300, height=60, bg=clr2)  # Frame for the application title
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=clr0)  # Frame for the converter interface
main.grid(row=1, column=0)

# Function to handle currency conversion process
def convert():
    # Define the URL for the currency conversion API
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    # Retrieve selected currencies and amount from user input
    currency_1 = combo1.get()  # Source currency
    currency_2 = combo2.get()  # Target currency
    amount = value.get()  # Amount to convert

    # Construct the query string with selected currencies and amount
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    # Assign appropriate currency symbol based on the target currency
    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'

    # Set up headers for the HTTP request
    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
    }

    # Send a GET request to the currency conversion API with the query string and headers
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract the converted amount from the response
    converted_amount = data["result"]["convertedAmount"]

    # Format the converted amount with the appropriate currency symbol and display it
    formatted = symbol + " {:,.2f}".format(converted_amount)
    result['text'] = formatted

    # Print the converted amount and formatted result for debugging purposes
    print(converted_amount, formatted)

# Set up the top frame to display the application title with an icon and text
icon = Image.open('images/icon.png')  # Load the application icon
icon = icon.resize((50, 50))  # Resize the icon to fit
icon = ImageTk.PhotoImage(icon)  # Convert the icon to a Tkinter-compatible format
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=45, padx=15, pady=20, anchor=CENTER, font=('Arial 16 bold'), bg=clr2, fg=clr0)
app_name.place(x=0, y=5)  # Position the title within the top frame

# Set up the main frame to contain the converter interface elements
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=clr0, fg=clr1)
result.place(x=60, y=10)  # Position the result label within the main frame

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']  # List of supported currencies

# Label and Combobox for selecting the source currency
from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=clr0, fg=clr1)
from_label.place(x=48, y=90)  # Position the 'From' label within the main frame
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))  # Combobox for source currency selection
combo1['values'] = (currency)  # Populate the Combobox with currency options
combo1.place(x=50, y=115)  # Position the Combobox within the main frame

# Label and Combobox for selecting the target currency
to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=clr0, fg=clr1)
to_label.place(x=158, y=90)  # Position the 'To' label within the main frame
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))  # Combobox for target currency selection
combo2['values'] = (currency)  # Populate the Combobox with currency options
combo2.place(x=160, y=115)  # Position the Combobox within the main frame

# Entry widget for inputting the amount to convert
value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)  # Position the Entry widget within the main frame

# Button to trigger the conversion process
button = Button(main, text="Convert", width=19, padx=5, height=1, bg=clr0, fg=clr1, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)  # Position the button within the main frame

# Start the GUI event loop to display the application window
window.mainloop()
