from tkinter import *
root = Tk()
root.config(background="White")
root.title("Temperature Converter")
root.geometry("500x250")
def convert():
    temp=celcius_value.get()
    if(temp.replace('.','').isdigit()):
        temp_far = (float(temp) * 9/5) + 32
        output.config(text = "Temperature in Farenheit:"+str(temp_far))
        error.grid_forget()
    else:
        error.grid(row=1,column=1)

heading=Label(root, text="Celcius ==> Farenheit", font=("times", 28, "bold"))
heading.pack()

frame = Frame(root)
frame.pack(pady = 20)

enter=Label(frame, text="Enter temperature in Celcius:")
enter.grid(row=0,column=0)

celcius_value = Entry(frame)
celcius_value.grid(row = 0, column = 1)

error=Label(frame, text="Please use valid inputs")

output=Label(frame)
output.grid(row=4,column=0)


submit=Button(frame, text="Submit",bg="green", command="convert")
submit.grid(row=3, column=0)

root.mainloop()