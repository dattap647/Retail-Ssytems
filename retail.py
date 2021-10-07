from tkinter import *
import ttkthemes as td
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
import time
import pyqrcode
import datetime
import random
import os
import smtplib

rupees=[10000,5000, 15000, 12000, 14000, 20000, 25000, 11000,
        13000, 16000, 17000, 18000, 19000, 8000, 9000, 21000,
        22000, 23000, 24000, 26000, 27000, 4000, 28000, 29000,
        37000, 36000, 30000, 31000, 32000, 33000, 34000, 35000 ]
random.shuffle(rupees)


def email():
    def send():
        ob = smtplib.SMTP('smtp.gmail.com', 587)
        ob.starttls()
        ob.login(gmailidTextEntry.get(), passwordTextEntry.get())
        subject = subjectTextEntry.get()
        body = messageText.get(1.0, END)
        message = '{}\n\n{}'.format(subject, body)

        listofAddress = [customerIdTextEntry.get()]
        ob.sendmail(gmailidTextEntry.get(), listofAddress, message)
        showinfo('Success', 'Bill is successfully sent',parent=root2)

        res=askyesno('Information','Do you want to clear the fields?',parent=root2)
        if res:
            messageText.delete(1.0,END)
            subjectTextEntry.delete(0,END)
            customerIdTextEntry.delete(0,END)
            gmailidTextEntry.delete(0,END)
            passwordTextEntry.delete(0,END)

        else:
            pass

        ob.quit()

    root2 = Toplevel()
    root2.geometry('600x720+100+0')
    root2.title('Send Gmail')
    root2.config(bg='sienna3')
    root2.resizable(0, 0)

    gmailFrame = Frame(root2, bg='whitesmoke', width=570, height=690)
    gmailFrame.place(x=15, y=15)

    fromLabel = Label(gmailFrame, text='From,', font=('arial', 22, 'bold'), bg='whitesmoke', fg='sienna3')
    fromLabel.place(x=5, y=5)

    gmailidLabel = Label(gmailFrame, text='Gmail Id', font=('arial', 20, 'bold'), bg='whitesmoke', fg='sienna3')
    passwordLabel = Label(gmailFrame, text='Password', font=('arial', 20, 'bold'), bg='whitesmoke', fg='sienna3')

    gmailidLabel.place(x=80, y=45)
    passwordLabel.place(x=80, y=105)

    gmailidTextEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), relief=RIDGE, bd=5, width=23)
    passwordTextEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), relief=RIDGE, bd=5, width=23,show='*')

    gmailidTextEntry.place(x=240, y=40)
    passwordTextEntry.place(x=240, y=100)

    toLabel = Label(gmailFrame, text='To,', font=('arial', 22, 'bold'), bg='whitesmoke', fg='sienna3')
    toLabel.place(x=5, y=170)

    customerIdLabel = Label(gmailFrame, text='Gmail Id', font=('arial', 20, 'bold'), bg='whitesmoke', fg='sienna3')
    subjectLabel = Label(gmailFrame, text='Subject', font=('arial', 20, 'bold'), bg='whitesmoke', fg='sienna3')

    customerIdLabel.place(x=80, y=210)
    subjectLabel.place(x=80, y=270)

    customerIdTextEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), relief=RIDGE, bd=5, width=23)
    customerIdTextEntry.insert(END,emailEntry.get())
    subjectTextEntry = Entry(gmailFrame, font=('arial', 18, 'bold'), relief=RIDGE, bd=5, width=23)
    subjectTextEntry.insert(END,'GENERAL BAZAAR BILL')

    customerIdTextEntry.place(x=240, y=205)
    subjectTextEntry.place(x=240, y=265)

    messageLabel = Label(gmailFrame, text='Bill', font=('arial', 20, 'bold'), bg='whitesmoke', fg='sienna3')
    messageLabel.place(x=5, y=310)

    messageText = Text(gmailFrame, font=('arial', 15, 'bold'), relief=SUNKEN, bd=5, width=49, height=11)
    messageText.place(x=10, y=350)

    messageText.insert(END, "\t *** Welcome To General Bazaar ***\n\n ")

    messageText.insert(END,f'\tCustomer Name:\t{customerNameEntry.get()}\n\tPhone No:\t{customerContactEntry.get()}\n'
                        f'\tEmail Id:\t{emailEntry.get()}\n\tDate:\t{time.strftime("%d/%m/%Y")}\n\n', )



    messageText.insert(END, f'\tTotal Products:\t{len(l)}\n')

    messageText.insert(END, f'\tTotal Quantity:\t{s}\n')
    messageText.insert(END, f'\tTotal Price:\t{summ} Rs')




    sendButton = Button(gmailFrame, text='SEND', font=('arial', 15, 'bold'), bg='sienna3', fg='white', command=send)
    sendButton.place(x=485, y=640)

    root2.mainloop()



def find_bill():
    url=filedialog.askopenfilename( defaultextension='.txt',
                                   filetypes=(('Text File', '.txt'), ('All files', '*.*')))
    if url=='':
        return
    else:
        f1=open(url,'r')
        billTextarea.delete(1.0,END)
        for d in f1:
            billTextarea.insert(END, d)
        f1.close()





def clear():
    billTextarea.delete(1.0,END)
    customerContactEntry.delete(0,END)
    customerNameEntry.delete(0,END)
    qrcodeFrame.place_forget()

    emailEntry.delete(0,END)
    billTextarea.config(width=65,height=17)



def save():

    if  customerNameEntry.get()==''or customerContactEntry.get()=='' or emailEntry.get()=='':
        showerror('Error','Nothing to save')

    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '.txt'), ('All files', '*.*')))
        if url == None:
            return
        bill_data = billTextarea.get('1.0', END)
        url.write(bill_data)
        url.close()

def remove():
    delete=listboxarea.curselection()
    if delete==():
        showerror('Error','nothing to remove')
    else:
        for item in delete:

            quantitylist.pop(item)

        listboxarea.delete(delete)

def clearAll():
    listboxarea.delete(0,END)
    quantityEntry.delete(0,END)
    selectcategoryCombobox.set('Select')
    selectsubcategoryCombobox.set('Select')
    productCombobox.set('Select')
    selectsubcategoryCombobox.config(state='disabled')
    productCombobox.config(state=DISABLED)

quantitylist=[]
def add_to_cart():
    global quantitylist
    if productCombobox.get()=='Select':
        showerror('Error', 'No Product Is Selected')

    elif  quantityEntry.get()=='':
        showerror('Error', 'Select Quantity')




    else:
        billTextarea.grid_remove()
        listboxarea.grid()
        listboxarea.insert(END, f'{productCombobox.get()}')
        quantitylist.append(quantityEntry.get())




def product_selection(event):
    def func1(event):
        if selectsubcategoryCombobox.get()=='Laptops':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('Hp','Dell','Lenovo','Asur','Asus','Apple')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get()=='Headphones & Speakers':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('JBL','Skullcandy','Sony','Boat','Mi','Apple')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get()=='Mobiles':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('Samsung','Oppo','Vivo','Realme','Xiomi','Apple')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get()=='Tablets':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('Lenovo','HUAWEI','Samsung','Apple')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)



        elif selectsubcategoryCombobox.get()=='Cameras & Accessories':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('DSLRs','Mirrorless Camera','Digital Camera','Tripods','Camera Bags')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get()=='Printers & Monitors':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('Ink Jet Printers','Laser Printers','Wireless Printers','Philips Monitor','LG Monitor','HP Monitor')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

    def func2(event):
        if selectsubcategoryCombobox.get() == 'Footwear':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Sports Shoes', 'Casual Shoes', 'Formal Shoes', 'Slippers', 'Sandals', 'Heels & Wedges')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get()=='Clothing':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values']=('Tshirts','Shirts','Innerwear','Trousers','Jeans','Shorts','Ethnic Wear'
                                       ,'Suits & Blazers','Kurtas','Sarees','Lehenga Cholis','Gowns')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Watches':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Casio', 'Fossil', 'Titan', 'Seiko', 'Tissot')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Fashion Jewellery':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Jewellery Sets', 'Earings', 'Rings', 'Bangles', 'Chains','Bracelets')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

    def func3(event):
        if selectsubcategoryCombobox.get() == 'Bedroom Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Bed', 'Mattress', 'Wardrobe', 'Dressing Table',)
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Living & Dining Room Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Sofas', 'Recliners', 'Dining Table Set', 'Chair', 'Shoe Rack','Drawers & Cabinets')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Kids Furniture':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('', 'Bean Bag', 'Stool', 'Study Table', 'Wardrobe','Chair')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Kitchen & Dinnerware':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Pressure Cooker', 'Gas Stove', 'Lunch Box', 'Pan & Tawa', 'Water Bottles','Kitchen Tools')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Home Decor':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Painting', 'Clock', 'Wall Shelf', 'Cushion', 'Bedsheets')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

    def func4(event):
        if selectsubcategoryCombobox.get() == 'Televisions':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Realme Smart Tv', 'Nokia 4K UHD TV', 'LG Smart TV', 'Sansui 4K LED', 'Panasonic TV', 'Mi Android TV')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Washing Machines':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Onida 6.2kg', 'Whirlpool 7kg', 'LG 8kg', 'MarQ 7kg', 'Samsung 6.7kg')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Refrigerators':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Whirlpool 3Star', 'Samsung 2Star', 'LG 3Star', 'Godrej Double Door', 'Panasonic 5Star')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Air Conditioners':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('MarQ Inverter AC', 'Voltas Split AC', 'Whirpool Inverter AC', 'Carrier AC', 'Bluestar Split AC')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)



    def func5(event):
        if selectsubcategoryCombobox.get() == 'Face Makeup':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Lakme Face Care Cream', 'Garnier Skin Natural Water', 'Lakme Lipstick', 'Lakme Eyeconic Kajal', 'Nail Polish Set', 'Makeup Kit')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Bath,Body & Skin Care':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Clean & Clear Oil Free Face Wash', 'Lip Balm', 'Body Soap', 'Fair & Handsome face Cream', 'Body Lotion')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Hair Care & Styling':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Hair Gel', 'Hair Oil', 'Hair Dryers', 'Shampoo', 'Condioner')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Fragrances':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Fogg Scent', 'Denver Perfume', 'Engage Men', 'Park Avenue', 'Set Wet Deodorant')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

    def func6(event):
        if selectsubcategoryCombobox.get() == 'Books':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Literature Book', 'E-Learning', 'Young Readers', 'Test Prep & Guide', 'Fiction Book', 'Non-Fiction Book')
            productCombobox.set('Select')
            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Sports':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('', 'Football', 'Badminton', 'Cricket Bat', 'Ball','Carrom','Chess','Skates')
            productCombobox.set('Select')



            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Exercise & Fitness':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Dumbells', 'Gym Bags', 'Treadmill', 'Mini Exercise Cycle', 'Abs Exercise Machine')
            productCombobox.set('Select')

            quantityEntry.config(state=NORMAL)

        elif selectsubcategoryCombobox.get() == 'Car & Bike Accessories':
            productCombobox.config(state=NORMAL)
            productCombobox.config(state='readonly')
            productCombobox['values'] = ('Helmet', 'Car Bluetooth Device', 'Car Mobile Charger', 'Car Lubricants', 'Riding Gloves','Bikers Face Mask','Goggles','Tyres','Arm Sleeves')
            productCombobox.set('Select')

            quantityEntry.config(state=NORMAL)

    if selectcategoryCombobox.get()=='Electronics':

        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values']=('Laptops','Headphones & Speakers','Mobiles',
                                             'Tablets','Cameras & Accessories','Printers & Monitors'
                                             )
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')

        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func1)

    elif selectcategoryCombobox.get()=='Fashion':


        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values']=('Footwear','Clothing','Watches'
                                             ,'Fashion Jewellery')
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')
        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func2)


    elif selectcategoryCombobox.get() == 'Home & Furniture':
        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values'] = ('Bedroom Furniture','Living & Dining Room Furniture','Kids Furniture',
                                               'Kitchen & Dinnerware','Home Decor')
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')
        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func3)



    elif selectcategoryCombobox.get() == 'Tvs & Appliances':
        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values'] = ('Televisions','Washing Machines','Refrigerators','Air Conditioners',
                                                )
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')
        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func4)





    elif selectcategoryCombobox.get() == 'Beauty and Personal Care':
        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values'] = ('Face Makeup','Bath,Body & Skin Care','Hair Care & Styling',
                                               'Fragrances')
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')
        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func5)



    elif selectcategoryCombobox.get() == 'Sports Books and more':
        selectsubcategoryCombobox.config(state=NORMAL)
        selectsubcategoryCombobox.config(state='readonly')

        selectsubcategoryCombobox['values'] = ('Books','Sports','Exercise & Fitness','Car & Bike Accessories',
                                               )
        selectsubcategoryCombobox.set('Select')
        productCombobox.set('Select')
        selectsubcategoryCombobox.bind('<<ComboboxSelected>>',func6)







def generate():
    global qrimage,summ,s,l
    if customerNameEntry.get()=='' or customerContactEntry.get()=='':
        showerror('Error','Please Enter Customer Details')

    else:



        listboxarea.grid_remove()
        l=listboxarea.get(0,END)


        billTextarea.grid()
        billTextarea.config(width=65,height=17)
        billTextarea.delete(1.0, END)
        billTextarea.insert(END, "\t\t ** Welcome To General Bazaar **\n\n ")

        billTextarea.insert(END,f'Customer Name:\t{customerNameEntry.get()}\t\t\t\tPhone No:\t{customerContactEntry.get()}\n\n'
        f'Email Id:\t{emailEntry.get()}\t\t\t\tDate:\t{time.strftime("%d/%m/%Y")}\n',)


        billTextarea.insert(END, f'\n ==========================================================')
        billTextarea.insert(END, f'\n Products\t\t\tQuantity\t\t\tPrice (in Rs)')

        billTextarea.insert(END, f'\n ==========================================================\n')
        summ=0
        for item in range(len(l)):
            billTextarea.insert(END,f'{l[item]}\t\t\t  {quantitylist[item]}\t\t\t  {rupees[0]}\n')
            summ=summ+rupees[0]
            random.shuffle(rupees)

        billTextarea.insert(END, f'\n ----------------------------------------------------------------------------------------------------------\n\n')

        billTextarea.insert(END,f'Total Products:\t\t{len(l)}\n')
        s=0
        for plus in quantitylist:
            s=s+int(plus)
        billTextarea.insert(END,f'Total Quantity:\t\t{s}\n')
        billTextarea.insert(END,f'Total Price:\t\t{summ} Rs')
        billTextarea.insert(END, f'\n ----------------------------------------------------------------------------------------------------------\n\n')

        qrcode()
        qrcodeFrame.place(x=365, y=160)
        qrcodeFrame.config(text='QR Code')
        qrimage = PhotoImage(file='qr.png')

        qrLabel.config(image=qrimage)




def qrcode():
    message=f'GENERAL BAZAAR (FUTURE RETAIL LTD)\nOWNER- FAIZAN KHAN \nCONTACT- +917905112734\n\nCustomer:-\nBill No: {billnumber.get()}\nName: {customerNameEntry.get()}\n' \
            f' Email id: {emailEntry.get()}\nContact: {customerContactEntry.get()}\nBill Amount: {summ} Rs '

    qr=pyqrcode.create(message)
    qr.png('qr.png',scale=3)









def calculator():
    def btnClick(numbers):
        global operator
        operator = operator + str(numbers)
        text_input.set(operator)


    def btnClear():
        global operator
        operator = ''
        text_input.set('')

    def btnAnswer():
        try:
            global operator
            sumup = str(eval(operator))
            text_input.set(sumup)
            operator = ''
        except:
            pass

    #########################Calculator

    textDisplay = Entry(calculatorFrame, width=21, bg='white', bd=3,textvariable=text_input,
                        font=('arial', 14, 'bold'),
                        justify=RIGHT)
    textDisplay.grid(row=0, column=0, columnspan=4, pady=10)
    textDisplay.insert(0, '0')

    button7 = ttk.Button(calculatorFrame,  width=4, text='7',
                      command=lambda: btnClick(7)).grid(row=2, column=0)

    button8 = ttk.Button(calculatorFrame,  width=4, text='8'
                     , command=lambda: btnClick(8)).grid(row=2, column=1,)

    button9 = ttk.Button(calculatorFrame,  width=4, text='9'
                    , command=lambda: btnClick(9)).grid(row=2, column=2, )

    buttonAdd = ttk.Button(calculatorFrame , width=4,
                       text='+'
                       ,  command=lambda: btnClick('+')).grid(row=2, column=3)

    button4 = ttk.Button(calculatorFrame, width=4, text='4'
                     ,  command=lambda: btnClick(4)).grid(row=3, column=0)

    button5 = ttk.Button(calculatorFrame,  width=4, text='5'
                     , command=lambda: btnClick(5)).grid(row=3, column=1)

    button6 = ttk.Button(calculatorFrame,width=4, text='6'
                     ,  command=lambda: btnClick(6)).grid(row=3, column=2)

    buttonsub = ttk.Button(calculatorFrame,  width=4,
                       text='-'
                       ,  command=lambda: btnClick('-')).grid(row=3, column=3)

    button1 = ttk.Button(calculatorFrame,  width=4, text='1'
                     ,  command=lambda: btnClick(1)).grid(row=4, column=0)

    button2 = ttk.Button(calculatorFrame,  width=4, text='2'
                     ,  command=lambda: btnClick(2)).grid(row=4, column=1)

    button3 = ttk.Button(calculatorFrame, width=4, text='3'
                     ,  command=lambda: btnClick(3)).grid(row=4, column=2)

    buttonmult = ttk.Button(calculatorFrame, width=4,
                        text='*'
                        ,  command=lambda: btnClick('*')).grid(row=4, column=3)

    buttonequal = ttk.Button(calculatorFrame, width=4,
                       text='='
                       , command=btnAnswer).grid(row=5, column=0)

    buttondel = ttk.Button(calculatorFrame, width=4,
                         text='Del'
                         ,  command=btnClear).grid(row=5, column=1)

    button0 = ttk.Button(calculatorFrame, width=4, text='0'
                     ,  command=lambda: btnClick(0)).grid(row=5, column=2)

    buttondiv = ttk.Button(calculatorFrame,  width=4,
                       text='/'
                       ,  command=lambda: btnClick('/')).grid(row=5, column=3)


def logout():
    root.destroy()
    import retaillogin

def timer():
    current_time=time.strftime('%H:%M:%S')
    timeLabel.config(text=current_time)
    timeLabel.after(20,timer)


root=td.ThemedTk()
root.get_themes()
root.set_theme('itft1')
root.config(bg='sienna3')


operator=''
text_input=StringVar()
billnumber = StringVar()
x = random.randint(1000, 9999)
billnumber.set(str(x))


root.title('Retail Management System created by Dattatray patil')
root.geometry('1350x720+0+0')

mainFrame=Frame(root,width=1320,height=690)
mainFrame.place(x=15,y=15)

titleLabel=Label(mainFrame,text='Retail System',font=('arial',40,'bold'),fg='sienna3')
titleLabel.place(x=510,y=10)

timeLabel=Label(mainFrame,font=('chillar',18,'bold'))
timeLabel.place(x=1200,y=25)
timer()
logoutButton=ttk.Button(mainFrame,text='Logout',command=logout)
logoutButton.place(x=15,y=5)

searchButton=ttk.Button(mainFrame,text='Search Bill',command=find_bill)
searchButton.place(x=5,y=45)

customerFrame=LabelFrame(mainFrame,text='Customer Details',font=('times new roman',20,'bold'),fg='sienna3',bd=10)
customerFrame.place(x=5,y=80)

emailLabel=Label(customerFrame,text='Email Id',font=('times new roman',16,'bold'))
emailLabel.grid(row=0,column=2,padx=20)
emailEntry=Entry(customerFrame,font=('times new roman',14,'bold'),width=25,bd=5,relief=GROOVE,)
emailEntry.grid(row=0,column=3)




customerNameLabel=Label(customerFrame,text='\tCustomer Name\t',font=('times new roman',16,'bold'))
customerNameLabel.grid(row=0,column=0,padx=10,sticky='w')
customerNameEntry=Entry(customerFrame,font=('times new roman',14,'bold'),width=15,bd=5,relief=GROOVE)
customerNameEntry.grid(row=0,column=1,padx=10)


customerContactLabel=Label(customerFrame,text='\tContact Number',font=('times new roman',16,'bold'))
customerContactLabel.grid(row=0,column=4)
customerContactEntry=Entry(customerFrame,font=('times new roman',14,'bold'),width=15,bd=5,relief=GROOVE)
customerContactEntry.grid(row=0,column=5,padx=20)


leftFrame=LabelFrame(mainFrame,text='Products',font=('times new roman',20,'bold'),fg='sienna3',bd=10)
leftFrame.place(x=5,y=160)

selectcategoryLabel=Label(leftFrame,text='Select Category',font=('times new roman',16,'bold'))
selectcategoryLabel.grid(row=0,column=0,sticky='w',pady=5)
selectcategoryCombobox=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),justify=CENTER,state='readonly',width=30,)
selectcategoryCombobox['values']=('Electronics','Fashion','Home & Furniture','Tvs & Appliances',
                                  'Beauty and Personal Care','Sports Books and more'
                                  )

selectcategoryCombobox.grid(row=1,column=0)
selectcategoryCombobox.set('Select')

selectsubcategoryLabel=Label(leftFrame,text='Sub Category',font=('times new roman',16,'bold'))
selectsubcategoryLabel.grid(row=2,column=0,sticky='w',pady=5)
selectsubcategoryCombobox=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),justify=CENTER,state='disabled',width=30)

selectsubcategoryCombobox.grid(row=3,column=0)


productLabel=Label(leftFrame,text='Product',font=('times new roman',16,'bold'))
productLabel.grid(row=4,column=0,sticky='w',pady=5)
productCombobox=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),justify=CENTER,state='disabled',width=30)

productCombobox.grid(row=5,column=0)

quantityLabel=Label(leftFrame,text='Quantity',font=('times new roman',16,'bold'))
quantityLabel.grid(row=6,column=0,sticky='w',pady=5)
quantityEntry=Entry(leftFrame,font=('times new roman',14,'bold'),justify=CENTER,state='disabled',bd=5,relief=GROOVE,width=30)

quantityEntry.grid(row=7,column=0,padx=10)



addtocartButton=ttk.Button(leftFrame,text='Add To Cart',command=add_to_cart)
addtocartButton.grid(row=8,column=0,pady=20,sticky='w',padx=30)

RemoveButton=ttk.Button(leftFrame,text='Remove',command=remove)
RemoveButton.place(x=140,y=298)

clearAllButton=ttk.Button(leftFrame,text='Clear All',command=clearAll)
clearAllButton.place(x=230,y=298)

bottomFrame=LabelFrame(mainFrame,text='Bill Options',font=('times new roman',20,'bold'),fg='sienna3',bd=10)
bottomFrame.place(x=5,y=555,width=350)

saveButton=ttk.Button(bottomFrame,text='Save',command=save)
saveButton.place(x=115,y=26)

generateButton=ttk.Button(bottomFrame,text='Generate',command=generate)
generateButton.grid(row=0,column=0,padx=20,pady=26)

clearButton=ttk.Button(bottomFrame,text='Clear',command=clear)
clearButton.place(x=270,y=26)

emailButton=ttk.Button(bottomFrame,text='Email',command=email)
emailButton.place(x=190,y=26)

calculatorFrame=LabelFrame(mainFrame,text='Calculator',font=('times new roman',20,'bold'),fg='sienna3',bd=10)
calculatorFrame.place(x=365,y=460)
calculator()





billareaFrame=LabelFrame(mainFrame,text='Bill Details',font=('times new roman',20,'bold'),fg='sienna3',bd=10)
billareaFrame.place(x=630,y=160)
shopnameLabel=Label(billareaFrame,text='DSP BAZAAR (WHOLESALE RETAIL LTD)\nGOA-403401\n'
                                       'EMAIL:dattap647@gmail.com\nMOBILE NO:8668298946\n'
                                       'TEL NO:0832-234577\nHELPLINE:1800-101-1800\n',font=('arial',10,'bold'))
shopnameLabel.grid(row=0,column=0)



scroll_y = Scrollbar(billareaFrame, orient=VERTICAL)
billTextarea=Text(billareaFrame,font=('times new roman',14,'bold'),width=65,height=17,yscrollcommand=scroll_y.set)
scroll_y.grid(row=2,column=1)
scroll_y.config(command=billTextarea.yview)
billTextarea.grid(row=2,column=0)

scroll_yy = Scrollbar(billareaFrame, orient=VERTICAL)
listboxarea=Listbox(billareaFrame,font=('times new roman',14,'bold'),width=65,height=17,yscrollcommand=scroll_yy.set,justify=CENTER,bg='white')
scroll_yy.grid(row=2,column=1)
scroll_yy.config(command=listboxarea.yview)
listboxarea.grid(row=2,column=0)
listboxarea.grid_remove()


qrcodeFrame=LabelFrame(mainFrame,font=('times new roman',20,'bold'),fg='sienna3',bd=10)
qrcodeFrame.place(x=365,y=160)
qrcodeFrame.place_forget()


qrLabel = Label(qrcodeFrame, font=('times new roman', 16, 'bold'))
qrLabel.grid(row=0, column=0)


selectcategoryCombobox.bind('<<ComboboxSelected>>',product_selection)
root.mainloop()