from tkinter import *


def clear():
    global invest
    global interest
    global years
    global total
    invest.destroy()
    interest.destroy()
    years.destroy()
    total.destroy()
    invest = Entry(window)
    invest.place(x=170, y=20)
    invest.config(width=15)
    interest = Entry(window)
    interest.place(x=170, y=60)
    interest.config(width=15)
    years = Entry(window)
    years.place(x=170, y=100)
    years.config(width=15)
    total = Entry(window)
    total.place(x=170, y=220)
    total.config(width=15)


def evaluate():
    global total
    x = float(invest.get())
    y = float(interest.get())
    z = float(years.get())
    formula = x * pow((1 + (y/100)), z)

    total.insert(0, formula)



print("Interest Has To Be A Whole Number Out Of 100")
window = Tk()
window.title("Money Calculator")
window = Canvas(window, width=300, height=300)
window.pack()
invest = Entry(window)
invest.place(x=170, y=20)
invest.config(width=15)
investlbl = Label(window, text="Investment: ", font=("Ariel", 15))
investlbl.place(x=50, y=14)
interest = Entry(window)
interest.place(x=170, y=60)
interest.config(width=15)
interestlbl = Label(window, text="Interest: ", font=("Ariel", 15))
interestlbl.place(x=65, y=54)
years = Entry(window)
years.place(x=170, y=100)
years.config(width=15)
yearslbl = Label(window, text="Num Of Years: ", font=("Ariel", 15))
yearslbl.place(x=20, y=94)
bttn = Button(window, text="Evaluate", command=evaluate, bg="black", fg="white")
bttn.place(x=115, y=147)
total = Entry(window)
total.place(x=170, y=220)
total.config(width=15)
totallbl = Label(window, text="Final Amount: ", font=("Ariel", 15))
totallbl.place(x=30, y=213)
line = window.create_line(0, 200, 400, 200)
window.mainloop()
