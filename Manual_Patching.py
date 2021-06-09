from tkinter import *
 
def RelativeToVirtual():
    res=int(e1.get(),16)-(int(e2.get(),16)+ int(e3.get(),16)) + int(e4.get(),16)
    myText.set(hex(res))
 
master = Tk()
myText=StringVar()
Label(master, text="Byte_VA").grid(row=0, sticky=W)
Label(master, text="IMage_Base").grid(row=1, sticky=W)
Label(master, text="Section_RVA").grid(row=2, sticky=W)
Label(master, text="PointerToRawData").grid(row=3, sticky=W)
Label(master, text="Byte_Offest:").grid(row=4, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=4,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
 
b = Button(master, text="Calculate", command=RelativeToVirtual)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
