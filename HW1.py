from tkinter import *
import tkinter.font as font
#Function to Convert Celsius to Fahrenheit
def convert():
    temp_celsius = celsius_value.get()
    #string.replace(oldvalue, newvalue, count)
    if(temp_celsius.replace('.','').isdigit()):
        error_msg.grid_forget()
        temp_fahrenheit = (float(temp_celsius) * 2.204623)
        output_fahrenheit.config(text = 'Weight in Pounds : ' + str(temp_fahrenheit))
    else:
        error_msg.grid(row=1, column=1)
my_window = Tk()
my_window.title("Kg to Pound Converter")
#Displaying heading inside window
description = Label(text = 'Kg => Pound', font = font.Font(size = 20), fg = "grey")
description.pack()
frame = Frame(my_window)
frame.pack(pady = 20)
#entry box to enter temperature in celsius
message_one = Label(frame, text = 'Enter Weight in Kg : ', font = font.Font(size = 10))
message_one.grid(row = 0, column = 0)
celsius_value = Entry(frame)
celsius_value.grid(row = 0, column = 1)
#To Display Error Message
error_msg = Label(frame, text = 'Please enter valid input...', font = font.Font(size = 8), fg = 'red')
#To Display the Output
output_fahrenheit = Label(frame, font = font.Font(size = 12))
output_fahrenheit.grid(row = 2, column = 0, columnspan = 2, pady = 10)
#Submit Button
submit_btn = Button(frame, text = 'Convert', width = 30, fg = "black", bg = "light green", bd = 0, padx = 20, pady = 10, command = convert)
submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)
my_window.geometry('500x250')
my_window.mainloop()