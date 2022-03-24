from tkinter import *
window=Tk()


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='grey')


def calculate_interest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i, 2)
    #Showlabel.destroy()
    result.destroy()
   # msg=""


    output_message=Label(result_frame,text="Interest "+str(p)+"at rate of interest"+str(r)+" for"+str(t)+"years is"+str(interest), bg = "grey", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()
    

app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "grey", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "grey", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

principle=Label(window, text="Enter Principle", fg= "red", bg= "orange", font=("Calibri", 12))
principle.place(x=20, y=140)

principle=Entry(window, text= "", bd=2, width=15)
principle.place(x=150, y=142)

rate=Label(window, text="Enter Rate", fg= "red", bg= "orange", font=("Calibri", 12))
rate.place(x=20, y=185)

rate=Entry(window, text= "", bd=2, width=15)
rate.place(x=150, y=187)

time=Label(window, text="Enter Time", fg= "red", bg= "orange", font=("Calibri", 12))
time.place(x=20, y=230)

time=Entry(window, text= "", bd=2, width=15)
time.place(x=150, y=232)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20, y=260)


result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result=Label(result_frame,text="Your result will be placed here ", bg = "grey", font=("Calibri", 12), width=55)
result.place(x=20,y=20)
result.pack()

window.mainloop()