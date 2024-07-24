from tkinter import *
root = Tk()
root.geometry('500x300')
def getvals():
    print('Accepted')
Label(root,text='Python Registration Form',font='ar 15 bold').grid(row=0,column=3)
#Fields
name = Label(root,text='Name')
phone = Label(root,text='Phone')
gender = Label(root,text='Gender')
emergency = Label(root,text='Emergency')
payment_mode = Label(root,text='Payment Mode')

#Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment_mode.grid(row=5,column=2)

#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
payment_modevalue = StringVar
checkvalue = IntVar

#Creating Entry field
nameentry = Entry(root,textvariable =namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencyentry = Entry(root,textvariable=emergencyvalue)
payment_modeentry = Entry(root,textvariable=payment_modevalue)

#Packing Entry field
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
payment_modeentry.grid(row=5,column=3)


#Creating Checkbox
checkbtn = Checkbutton(text='remember me?',variable = checkvalue)
checkbtn.grid(row=6,column=3)

#Submit button
Button(text='Submit',command=getvals).grid(row=7,column=3)

root.mainloop()


