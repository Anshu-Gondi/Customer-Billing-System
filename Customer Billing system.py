from email.mime import application
from tkinter import *
from tkinter import ttk
import random
import time
import tkinter.messagebox
from datetime import datetime

class Customer:
    def __init__(self,root):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background= '#060270')

        ABC = Frame(self.root,bg="#FFDE59", bd=20, relief=RIDGE)
        ABC.grid()
        
        ABC1 = Frame(ABC,bg="#FFDE59", bd=14, relief=RIDGE, width=1350, height=100, padx=10)
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)

        ABC2 = Frame(ABC,bg="#FFF311", bd=14, relief=RIDGE, width=450, height=488, padx=10)
        ABC2.grid(row=1, column=0, sticky=W)

        ABC3 = Frame(ABC,bg="#FFF311", bd=14, relief=RIDGE, width=450, height=488, padx=10)
        ABC3.grid(row=1, column=1, sticky=W)
        
        ABC4 = Frame(ABC,bg="#FFF311", bd=14, relief=RIDGE, width=460, height=488, padx=10)
        ABC4.grid(row=1, column=2, sticky=W)

        ABC5 = Frame(ABC4,bg="#FFF311", bd=14, relief=RIDGE, width=370, height=340, padx=10)
        ABC5.grid(row=0, column=0, sticky=W)

        ABC6 = Frame(ABC4,bg="#FFF311", bd=14, relief=RIDGE, width=370, height=120, padx=10)
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H:%M:%S"))

        #================================================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def Reset():
            E_Latta.set("0")
            E_Espresso.set("0")
            E_Iced_Latte.set("0")
            E_Vale_Coffee.set("0")
            E_Cappuccino.set("0")
            E_Africian_Coffee.set("0")
            E_American_Coffee.set("0")
            E_Iced_Cappuccino.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationaility.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")

            self.txtLatta.configure(state=DISABLED)
            self.txtEspresso.configure(state=DISABLED)
            self.txtIced_Latte.configure(state=DISABLED)
            self.txtVale_Coffee.configure(state=DISABLED)
            self.txtCappuccino.configure(state=DISABLED)
            self.txtAfrician_Coffee.configure(state=DISABLED)
            self.txtAmerican_Coffee.configure(state=DISABLED)
            self.txtIced_Cappuccino.configure(state=DISABLED)

        #================================================================================================================
        def chkLatta():
            if (var1.get() == 1):
                self.txtLatta.configure(state=NORMAL)
                self.txtLatta.focus()
                self.txtLatta.delete('0',END)
                E_Latta.set("")
            elif var1.get() == 0:
                self.txtLatta.configure(state=DISABLED)
                self.txtLatta.set("0")
        
        def chkEspresso():
            if (var2.get() == 1):
                self.txtEspresso.configure(state=NORMAL)
                self.txtEspresso.focus()
                self.txtEspresso.delete('0',END)
                E_Espresso.set("")
            elif var2.get() == 0:
                self.txtEspresso.configure(state=DISABLED)
                self.txtEspresso.set("0")

        def chkIced_Latte():
            if (var3.get() == 1):
                self.txtIced_Latte.configure(state=NORMAL)
                self.txtIced_Latte.focus()
                self.txtIced_Latte.delete('0',END)
                E_Iced_Latte.set("")
            elif var3.get() == 0:
                self.txtIced_Latte.configure(state=DISABLED)
                self.txtIced_Latte.set("0")

        def chkVale_Coffee():
            if (var4.get() == 1):
                self.txtVale_Coffee.configure(state=NORMAL)
                self.txtVale_Coffee.focus()
                self.txtVale_Coffee.delete('0',END)
                E_Vale_Coffee.set("")
            elif var4.get() == 0:
                self.txtVale_Coffee.configure(state=DISABLED)
                self.txtVale_Coffee.set("0")
        
        def chkCappuccino():
            if (var5.get() == 1):
                self.txtCappuccino.configure(state=NORMAL)
                self.txtCappuccino.focus()
                self.txtCappuccino.delete('0',END)
                E_Cappuccino.set("")
            elif var5.get() == 0:
                self.txtCappuccino.configure(state=DISABLED)
                self.txtCappuccino.set("0")

        def chkAfrician_Coffee():
            if (var6.get() == 1):
                self.txtAfrician_Coffee.configure(state=NORMAL)
                self.txtAfrician_Coffee.focus()
                self.txtAfrician_Coffee.delete('0',END)
                E_Africian_Coffee.set("")
            elif var6.get() == 0:
                self.txtAfrician_Coffee.configure(state=DISABLED)
                self.txtAfrician_Coffee.set("0")

        def chkAmerican_Coffee():
            if (var7.get() == 1):
                self.txtAmerican_Coffee.configure(state=NORMAL)
                self.txtAmerican_Coffee.focus()
                self.txtAmerican_Coffee.delete('0',END)
                E_American_Coffee.set("")
            elif var7.get() == 0:
                self.txtAmerican_Coffee.configure(state=DISABLED)
                self.txtAmerican_Coffee.set("0")

        def chkIced_Cappuccino():
            if (var8.get() == 1):
                self.txtIced_Cappuccino.configure(state=NORMAL)
                self.txtIced_Cappuccino.focus()
                self.txtIced_Cappuccino.delete('0',END)
                E_Iced_Cappuccino.set("")
            elif var8.get() == 0:
                self.txtIced_Cappuccino.configure(state=DISABLED)
                self.txtIced_Cappuccino.set("0")

        #================================================================================================================

        def Costofitem():
            CustomerRef.set(random.randint(19800, 9875648))
            Item1 = float(E_Latta.get())
            Item2 = float(E_Espresso.get())
            Item3 = float(E_Iced_Latte.get())
            Item4 = float(E_Vale_Coffee.get())
            Item5 = float(E_Cappuccino.get())
            Item6 = float(E_Africian_Coffee.get())
            Item7 = float(E_American_Coffee.get())
            Item8 = float(E_Iced_Cappuccino.get())

            PriceofDrinks = (Item1 * 1.2) + (Item2 * 2.05) + (Item3 * 3.05) + (Item4 * 1.89) + (Item5 * 1.99)  + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)
            SubTotalofITEMS = "$", str('%.2f'% PriceofDrinks)
            SubTotal.set(SubTotalofITEMS)
            TaxAmount = PriceofDrinks * 0.15
            Tax = "$" + str('%.2f' % TaxAmount)
            PaidTax.set(Tax)
            TTax = ((PriceofDrinks) * 0.15)
            TCost = "$", str('%.2f'% (PriceofDrinks + TTax))
            TotalCost.set(TCost)

            self.txtReceipt.insert(END,'Items\t\t\t\t' + "Cost of items \n")
            self.txtReceipt.insert(END,'Customer Ref:\t\t\t\t' + CustomerRef.get() + "\n")
            self.txtReceipt.insert(END,'Latta: \t\t\t\t' + E_Latta.get() + "\n")
            self.txtReceipt.insert(END,'Espresso:\t\t\t\t' + E_Espresso.get() + "\n")
            self.txtReceipt.insert(END,'Iced Latte:\t\t\t\t' + E_Iced_Latte.get() + "\n")
            self.txtReceipt.insert(END,'Vale Coffee:\t\t\t\t' + E_Vale_Coffee.get() + "\n")
            self.txtReceipt.insert(END,'Cappuccino:\t\t\t\t' + E_Cappuccino.get() + "\n")
            self.txtReceipt.insert(END,'African Coffee:\t\t\t\t' + E_Africian_Coffee.get() + "\n")
            self.txtReceipt.insert(END,'American Coffee:\t\t\t\t' + E_American_Coffee.get() + "\n")
            self.txtReceipt.insert(END,'Iced Cappuccino:\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")

            self.txtReceipt.insert(END,'\nTax Paid:\t\t\t\t' + PaidTax.get() + "\n")
            self.txtReceipt.insert(END,'\nSubTotal:\t\t\t\t' + str(SubTotal.get()) + "\n")
            self.txtReceipt.insert(END,'\nTotal Cost:\t\t\t\t' + str(TotalCost.get()))

        #================================================================================================================

        self.IblTitle = Label(ABC1, textvariable=Date1, font=('Arial',30,'bold'), pady=9,
                              bd=5, bg="#2E3BC7", fg="Cornsilk").grid(row=0, column=0)
        self.IblTitle = Label(ABC1, text="\tCustomer Billing System\t\t", font=('Arial',30,'bold'), pady=9,
                              bd=5, bg="#2E3BC7", fg="Cornsilk").grid(row=0, column=1)
        self.IblTitle = Label(ABC1, textvariable=Time1, font=('Arial',30,'bold'), pady=9,
                              bd=5, bg="#2E3BC7", fg="Cornsilk").grid(row=0, column=2)
        
        #================================================================================================================
        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationaility = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        CustomerRef.set(random.randint(19800, 9875648))

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        E_Latta = StringVar()
        E_Espresso = StringVar()
        E_Iced_Latte = StringVar()
        E_Vale_Coffee = StringVar()
        E_Cappuccino = StringVar()
        E_Africian_Coffee = StringVar()
        E_American_Coffee = StringVar()
        E_Iced_Cappuccino = StringVar()


        E_Latta.set("0")
        E_Espresso.set("0")
        E_Iced_Latte.set("0")
        E_Vale_Coffee.set("0")
        E_Cappuccino.set("0")
        E_Africian_Coffee.set("0")
        E_American_Coffee.set("0")
        E_Iced_Cappuccino.set("0")

        #================================================================================================================

        self.IblCus_Ref = Label(ABC2,font=("arial", 12, "bold"), text="Customer Ref:", padx=2, fg="white", bg="#041EE2")
        self.IblCus_Ref.grid(row=0, column=0, sticky=W)
        self.txtCus_Ref = Entry(ABC2,font=("arial", 12, "bold"), textvariable=CustomerRef, width=20)
        self.txtCus_Ref.grid(row=0, column=1, pady=3, padx=20)

        self.IblFirstname = Label(ABC2,font=("arial", 12, "bold"), text="Firstname:", padx=2, fg="white", bg="#041EE2")
        self.IblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(ABC2,font=("arial", 12, "bold"),textvariable=Firstname, width=20)
        self.txtFirstname.grid(row=1, column=1, pady=3, padx=20)

        self.IblSurname = Label(ABC2,font=("arial", 12, "bold"), text="Surname:", padx=2, fg="white", bg="#041EE2")
        self.IblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(ABC2,font=("arial", 12, "bold"), textvariable=Surname, width=20)
        self.txtSurname.grid(row=2, column=1, pady=3, padx=20)

        self.IblAddress = Label(ABC2,font=("arial", 12, "bold"), text="Address:", padx=2, fg="white", bg="#041EE2")
        self.IblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(ABC2,font=("arial", 12, "bold"), textvariable= Address, width=20)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)

        self.IblPCode = Label(ABC2,font=("arial", 12, "bold"), text="Post Code:", padx=2, fg="white", bg="#041EE2")
        self.IblPCode.grid(row=4, column=0, sticky=W)
        self.txtPCode = Entry(ABC2,font=("arial", 12, "bold"), textvariable=PostCode, width=20)
        self.txtPCode.grid(row=4, column=1, pady=3, padx=20)

        self.IblMobile = Label(ABC2,font=("arial", 12, "bold"), text="Mobile:", padx=2, fg="white", bg="#041EE2")
        self.IblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(ABC2,font=("arial", 12, "bold"), textvariable=Mobile, width=20)
        self.txtMobile.grid(row=5, column=1, pady=3, padx=20)

        self.IblEmail = Label(ABC2,font=("arial", 12, "bold"), text="Email:", padx=2, fg="white", bg="#041EE2")
        self.IblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(ABC2,font=("arial", 12, "bold"), textvariable=Email, width=20)
        self.txtEmail.grid(row=6, column=1, pady=3, padx=20)

        self.IblN = Label(ABC2, font=("arial", 12, 'bold'), text="Nationality:", padx=2, pady=2, fg="white", bg="#041EE2")
        self.IblN.grid(row=7, column=0,sticky=W)
        self.cboN = ttk.Combobox(ABC2, textvariable=Nationaility, state='readonly', font=("arial", 12, 'bold'),
                                 width=18)
        self.cboN['value']=('','British','Kenya','India','Iran','Morocco','Canada','France','Norway')
        self.cboN.current(0)
        self.cboN.grid(row=7, column=1, pady=3, padx=20)

        self.IblDOB = Label(ABC2,font=("arial", 12, "bold"), text="Date of Birth:", padx=2, fg="white", bg="#041EE2")
        self.IblDOB.grid(row=8, column=0, sticky=W)
        self.txtDOB = Entry(ABC2,font=("arial", 12, "bold"), textvariable=DOB, width=20)
        self.txtDOB.grid(row=8, column=1, pady=3, padx=20)

        self.IblIDType = Label(ABC2, font=("arial", 12, 'bold'), text="Type of ID:", padx=2, pady=2, fg="white", bg="#041EE2")
        self.IblIDType.grid(row=9, column=0,sticky=W)
        self.cboIDType = ttk.Combobox(ABC2, textvariable=IDType, state='readonly', font=("arial", 12, 'bold'),
                                 width=18)
        self.cboIDType['value']=('','Pilot License','Driving License','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9, column=1, pady=3, padx=20)

        self.IblGender = Label(ABC2, font=("arial", 12, 'bold'), text="Gender:", padx=2, pady=2, fg="white", bg="#041EE2")
        self.IblGender.grid(row=10, column=0,sticky=W)
        self.cboGender = ttk.Combobox(ABC2, textvariable=Gender, state='readonly', font=("arial", 12, 'bold'),
                                 width=18)
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10, column=1, pady=3, padx=20)

        self.IblCheck_In_Date = Label(ABC2,font=("arial", 12, "bold"), text="Check In Date:", padx=2, fg="white", bg="#041EE2")
        self.IblCheck_In_Date.grid(row=11, column=0, sticky=W)
        self.txtCheck_In_Date = Entry(ABC2,font=("arial", 12, "bold"), textvariable=Date1, width=20)
        self.txtCheck_In_Date.grid(row=11, column=1, pady=3, padx=20)

        self.IblCheck_Out_Date = Label(ABC2,font=("arial", 12, "bold"), text="Check Out Date:", padx=2, fg="white", bg="#041EE2")
        self.IblCheck_Out_Date.grid(row=12, column=0, sticky=W)
        self.txtCheck_Out_Date = Entry(ABC2,font=("arial", 12, "bold"), textvariable=Date1, width=20)
        self.txtCheck_Out_Date.grid(row=12, column=1, pady=3, padx=20)

        self.IblMeal = Label(ABC2, font=("arial", 12, 'bold'), text="Meal:", padx=2, pady=2, fg="white", bg="#041EE2")
        self.IblMeal.grid(row=13, column=0,sticky=W)
        self.cboMeal = ttk.Combobox(ABC2, textvariable=Meal, state='readonly', font=("arial", 12, 'bold'),
                                 width=18)
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=20)

        self.IblRoomType = Label(ABC2, font=("arial", 12, 'bold'), text="Room Type:", padx=2, pady=2, fg="white", bg="#041EE2")
        self.IblRoomType.grid(row=14, column=0,sticky=W)
        self.cboRoomType = ttk.Combobox(ABC2, textvariable=RoomType, state='readonly', font=("arial", 12, 'bold'),
                                 width=18)
        self.cboRoomType['value']=('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=20)

        #================================================================================================================
        self.Latta = Checkbutton(ABC3, text="Latta", variable=var1, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkLatta).grid(row=0, sticky=W)
        self.txtLatta = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Latta, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtLatta.grid(row=0, column=1)
        
        self.Espresso = Checkbutton(ABC3, text="Espresso", variable=var2, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkEspresso).grid(row=1, sticky=W)
        self.txtEspresso = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Espresso, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtEspresso.grid(row=1, column=1)

        self.Iced_Latte = Checkbutton(ABC3, text="Iced Latte", variable=var3, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkIced_Latte).grid(row=2, sticky=W)
        self.txtIced_Latte = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Iced_Latte, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtIced_Latte.grid(row=2, column=1)

        self.Vale_Coffee = Checkbutton(ABC3, text="Vale Coffee", variable=var4, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkVale_Coffee).grid(row=3, sticky=W)
        self.txtVale_Coffee = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Vale_Coffee, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtVale_Coffee.grid(row=3, column=1)

        self.Cappuccino = Checkbutton(ABC3, text="Cappuccino", variable=var5, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkCappuccino).grid(row=4, sticky=W)
        self.txtCappuccino = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Cappuccino, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtCappuccino.grid(row=4, column=1)

        self.Africian_Coffee = Checkbutton(ABC3, text="Africian_Coffee", variable=var6, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkAfrician_Coffee).grid(row=5, sticky=W)
        self.txtAfrician_Coffee = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Africian_Coffee, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtAfrician_Coffee.grid(row=5, column=1)

        self.American_Coffee = Checkbutton(ABC3, text="American Coffee", variable=var7, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkAmerican_Coffee).grid(row=6, sticky=W)
        self.txtAmerican_Coffee = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_American_Coffee, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtAmerican_Coffee.grid(row=6, column=1)

        self.Iced_Cappuccino = Checkbutton(ABC3, text="Iced Cappuccino", variable=var8, onvalue=1, offvalue=0,
                                 font=('arial', 12, 'bold'), bg='#5DE2E7', command=chkIced_Cappuccino).grid(row=7, sticky=W)
        self.txtIced_Cappuccino = Entry(ABC3,font=('arial', 12, 'bold'), textvariable=E_Iced_Cappuccino, bd=8,
                              width=20, justify='left', state=DISABLED)
        self.txtIced_Cappuccino.grid(row=7, column=1)

        self.Iblspace = Label(ABC3, text="Tax and Total Sum", font=("arial",18,'bold'), pady=1, bd=9, bg="#1D7405",
                              fg="white", width=26, justify=CENTER).grid(row=10, column=0,columnspan=4)

        #=========================Receipt=======================================================================================
        self.IblPaidTax = Label(ABC3,font=('arial', 12,'bold'), text="Paid Tax", bd=7, bg="#5DE2E7",fg="black")
        self.IblPaidTax.grid(row=11, column=0, sticky=W)
        self.txtPaidTax = Entry(ABC3,font=('arial', 12,'bold'), textvariable=PaidTax, bd=7,bg="white",
                            width=20, justify=LEFT)
        self.txtPaidTax.grid(row=11, column=1)

        self.IblSubTotal = Label(ABC3,font=('arial', 12,'bold'), text="Sub Cost", bd=7, bg="#5DE2E7",fg="black")
        self.IblSubTotal.grid(row=12, column=0, sticky=W)
        self.txtSubTotal = Entry(ABC3,font=('arial', 12,'bold'), textvariable=SubTotal, bd=7,bg="white",
                                width=20, justify=LEFT)
        self.txtSubTotal.grid(row=12, column=1)

        self.IblTotalCost = Label(ABC3,font=('arial', 12,'bold'), text="Total Cost", bd=7, bg="#5DE2E7",fg="black")
        self.IblTotalCost.grid(row=13, column=0, sticky=W)
        self.txtTotalCost = Entry(ABC3,font=('arial', 12,'bold'), textvariable=TotalCost, bd=7,bg="white",
                                width=20, justify=LEFT)
        self.txtTotalCost.grid(row=13, column=1)

        #================================================================================================================
        self.txtReceipt = Text(ABC5, height=19, width=43, bd=10, font=("arial", 9, "bold"))
        self.txtReceipt.grid(row=0, column=0)
        #=======================================Buttons=========================================================================
        self.btnTotal = Button(ABC6, padx=14, pady=7, bd=5, fg="white", font=('Arial',16,'bold'), width=5, height=2,
                               bg='#C12323', text="Total", command=Costofitem).grid(row=0, column=0)
        self.btnReset = Button(ABC6, padx=14, pady=7, bd=5, fg="white", font=('Arial',16,'bold'), width=5, height=2,
                               bg='#FDC911', text="Reset", command=Reset).grid(row=0, column=1)
        self.btnExit = Button(ABC6, padx=14, pady=7, bd=5, fg="white", font=('Arial',16,'bold'), width=5, height=2,
                               bg='#B0FC19', text="Exit", command=iExit).grid(row=0, column=2)
        #================================================================================================================

if __name__ == '__main__':
    root = Tk()
    application=Customer(root)
    root.mainloop() 