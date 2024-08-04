#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 
import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
import RPi.GPIO as GPIO
import time

from bot import Chatbot

# In[2]:


def read_from_db():
    conn = sqlite3.connect("medicine.db")
    cur = conn.cursor()
    #cur.execute("""
     #   CREATE TABLE medicine (
      #      ID integer PRIMARY KEY,
       #     name text NOT NULL,
        #    price real NOT NULL,
         #   quantity integer NOT NULL
        #)
        #""")
        
   #cur.execute("""
    #    INSERT INTO medicine (name, price, quantity)
     #   VALUES ('catafast', 13, 5)
      #  """)

    #cur.execute("""
     #   INSERT INTO medicine (name, price, quantity)
      #  VALUES ('panadol', 20, 5)
       # """) '''
    cur.execute("SELECT * FROM medicine")
    data = cur.fetchall()
    showData = ''
    for row in data:
        showData += f'{row}\n'
    win = Toplevel()
    dataFrame = Frame(win)
    dataFrame.grid(row=0, column=0)
    dataLabel = Label(dataFrame, text=showData)
    dataLabel.pack()
    scrollbar = Scrollbar(dataFrame)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=dataLabel.yview)
    conn.commit()
    conn.close()


# In[3]:


        
def select():
    select = Toplevel()
    select.title("Zooobaa - Select From Stack ")
    select.attributes("-fullscreen", True)
    select.configure(bg = '#222e50')
    
    items = Label(select, text = 'Items', font = ('Algerian' ,18,'bold'), fg = 'orange', bg ='#222e50' )
    items.place(x =100, y=70) 
    
    listbox = Listbox(select, font=('Arial', 16))
    listbox.place(x = 100, y =100, width=300 , height=350)

    # Connect to the database
    conn = sqlite3.connect("medicine.db")
    # Create a cursor object
    cur = conn.cursor()
    # Execute the select query
    cur.execute("SELECT name, price FROM medicine")
    # Fetch all the rows from the cursor
    rows = cur.fetchall()
    # Close the connection
    conn.close()

    # Create a list of drugs from the rows
    drugs = []
    for row in rows:
        # Format the row as a tuple
        drug = (row[0], row[1])
        # Append the tuple to the list
        drugs.append(drug)

    # Loop through the drugs and insert them into the listbox
    for drug in drugs:
        # Format the drug as a string
        item = f"{drug[0]} - {drug[1]}"
        # Insert the item into the listbox
        listbox.insert(END, item)

    # spinbox for quantity
    quantity = Spinbox(select, from_=1, to=3)
    qty_label = Label(select, text = 'Item quantaty:', font = ('Arial',12,'bold'), fg = 'orange', bg ='#222e50' )
    qty_label.place(x = 400, y=150)
    quantity.place(x = 400, y =200)

    # button for adding to cart
    add_button = Button(select, text='Add to cart')
    add_button.place(x = 450, y =250)

    # label for total cost
    total_label =Label(select, text='Total: $0.00', font = ('Arial', 12,'bold'), fg = 'Black')
    total_label.place(x = 700, y =500)

    # cart dictionary
    cart = {}
    cartmenue = Label(select, text = 'Cart', font = ('Algerian' ,18,'bold'), fg = 'orange', bg ='#222e50' )
    cartmenue.place(x =600, y=70) 
    cart_list = Listbox(select)
    cart_list.place(x = 600, y =100, width=300, height=350)
    qty = int(quantity.get())
    def update_cart():
        # Get the index of the selected item in the listbox
        index = listbox.curselection()[0]
        # Get the drug and price from the drugs list
        drug, price = drugs[index]
        # Get the quantity from the spinbox
        qty = int(quantity.get())
        
        # Update the cart dictionary with the drug and quantity
        if drug in cart:
            cart[drug] += qty
        else:
            cart[drug] = qty

        # Calculate the total cost of the cart items
        total = 0
        for drug, qty in cart.items():
            total += drugs[index][1] * qty

        # Clear the cart list before inserting new items
        cart_list.delete(0, END)

        # Loop through the cart items and insert them into the cart list
        for drug, qty in cart.items():
            cart_list.insert(END, f'{drug}: ${price} {qty}')
            

        # Update the total label with the new total cost
        total_label.config(text=f'Total: ${total:.2f}')
   
    '''To updata quantaty in DB'''       
    # Connect to the database
    conn = sqlite3.connect("medicine.db")
    # Create a cursor object
    cur = conn.cursor()
    # Execute the update query
    diff = quantity.get() * (-1)
    cur.execute("UPDATE medicine SET quantity = quantity + ? WHERE name = 'Antinal'", (diff,  ))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()
    
        
        

    # Bind the button to the update_cart function
    add_button.config(command=update_cart)
    
    
    def show_image(imagefile):
        image = ImageTk.PhotoImage(file = imagefile)
        imagebox.config(image=image)
        imagebox.image = image
        
    checkout = Button(select, text="Checkout", cursor='circle',
                      command=lambda: show_image('QR.jpg'))
    checkout.place(x=300, y=600, 
                   relwidt=0.10, relheight=0.050, anchor=CENTER)
    
    imagebox = Label(select)
    imagebox.place(relx=0.5, rely=0.5)
    def back():
        select.destroy()
    bckimg_open = Image.open('back0.png')
    bckimg = ImageTk.PhotoImage(bckimg_open)
    bck = Button(select, text="Back", command = back, image=bckimg,bg ='#222e50' )
    bck.place(x=100, y=600)
    
    #TO connect AVR
    def signal():
        
        GPIO.setmode(GPIO.BOARD)
        pin_num = 15
        GPIO.setup(pin_num, GPIO.OUT)

        #pin is now outputting LOW by default

        GPIO.output(pin_num, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(pin_num, GPIO.LOW)

        # Clean up the GPIO settings
        GPIO.cleanup()
        
        '''while (cart != 0):
            for i in range(qty):
                if cart[i] == 'panadol' :
                    pin_number = 15

                    # Set up the pin as an output
                    GPIO.setup(pin_number, GPIO.OUT)

                    # Make the pin high
                    GPIO.output(pin_number, GPIO.HIGH)

                    # Wait for one second
                    time.sleep(1)

                    # Make the pin low again
                    GPIO.output(pin_number, GPIO.LOW)

                    # Clean up the GPIO settings
                    GPIO.cleanup()
                
                time.sleep(2)
                if cart[i] == 'antinal' :
                    pin_number = 16

                    # Set up the pin as an output
                    GPIO.setup(pin_number, GPIO.OUT)

                    # Make the pin high
                    GPIO.output(pin_number, GPIO.HIGH)

                    # Wait for one second
                    time.sleep(1)

                    # Make the pin low again
                    GPIO.output(pin_number, GPIO.LOW)

                    # Clean up the GPIO settings
                    GPIO.cleanup()
                
            time.sleep(2)
            if cart[i] == 'catafast' :
                    pin_number = 16

                    # Set up the pin as an output
                    GPIO.setup(pin_number, GPIO.OUT)

                    # Make the pin high
                    GPIO.output(pin_number, GPIO.HIGH)

                    # Wait for one second
                    time.sleep(1)

                    # Make the pin low again
                    GPIO.output(pin_number, GPIO.LOW)

                    # Clean up the GPIO settings
                    GPIO.cleanup()'''
        
                
                
    confirmbtn = Button(select, text= "Confirmation", command = signal  )
    confirmbtn.place(relx=0.7, rely=0.8, 
                   relwidt=0.10, relheight=0.050, anchor=CENTER)
    select.mainloop()
    
def scanner():
    scanner =Toplevel()
    scanner.attributes("-fullscreen", True)
   
    
    scanner.mainloop()
    
i = 0
def wait():
    wait = Toplevel()
    wait.attributes("-fullscreen", True)
    wating = Label(wait, text = "Please wait...")
    wating.place(x = 500, y =250)
    loading = ttk.Style()
    loading.theme_use('clam')
    loading.configure('red.Horizontal.TProgressbar', background = '#108cff')
    loading = ttk.Progressbar(wait, orient = HORIZONTAL, length = 400, mode = 'determinate', style = 'red.Horizontal.TProgressbar')
    loading.place(x = 350 ,y=300)
    
    def top():
        wait.withdraw()
        os.system('Python loadingPage.py')
        wait.destroy()
        
    
    
    
    def load():
        global i 
        if i <= 10:
            txt = 'loading...'+ (str(10*i)+'%')
            wating.config(text = txt)
            wating.after(600, load)
            loading['value'] = 10*i
            i+=0.5
        else:
            top()
            
    load()
    scanner()

def options():
    options = Toplevel()
    options.title("Zooobaa - Options")
    options.attributes("-fullscreen", True)
    options.configure(bg='#ffb703')
    
    scanimg_open = Image.open('scan.png')
    scanimg = ImageTk.PhotoImage(scanimg_open)
    scanbtn = Button(options, image = scanimg ,cursor='circle' , command = wait,bg='#ffb703')
    scanbtn.place(x=200, y=300, anchor=CENTER)
    
    selectimg_open = Image.open('select.png')
    selectimg = ImageTk.PhotoImage(selectimg_open)
    selectbtn = Button(options, image = selectimg, cursor='circle',
                       command = select,bg='#ffb703')
    selectbtn.place(x=800 , y=300,  anchor=CENTER)
    
    cancelimg_open = Image.open('cancel.png')
    cancelimg = ImageTk.PhotoImage(cancelimg_open)
    cancel = Button(options, image= cancelimg, command=lambda: options.destroy(),bg='#ffb703')
    cancel.place(x=70, y=600)
    
    chatimg_open = Image.open('bot.png')
    chatimg = ImageTk.PhotoImage(chatimg_open)
    chatbot = Button(options, command =lambda: Chatbot(options), image = chatimg,bg='#ffb703')
    chatbot.place(x=750, y=550)
    options.mainloop()
   


# Login Bage

# Import tkinter and sqlite3 modules

def LOGIN():
    
    # Create a database connection and a cursor
    conn = sqlite3.connect("medicine.db")
    cur = conn.cursor()

    # Create a table for storing medicine data
    cur.execute("CREATE TABLE IF NOT EXISTS medicine (name TEXT, price REAL, quantity INTEGER)")

    # Define a function to check the user credentials
    def login():
        # Get the username and password from the entry widgets
        username = username_entry.get()
        password = password_entry.get()
        # Check if the username and password are valid
        if username == "admin" and password == "1234":
            # Destroy the login window
            login_window.destroy()
            # Create a new window for adding medicine data
            create_medicine_window()
        else:
            # Show an error message
            error_label.config(text="Invalid username or password")

    # Define a function to create a new window for adding medicine data
    def create_medicine_window():
        # Create a global variable for the medicine window
        global medicine_window
        # Create a new window object
        medicine_window = Tk()
        # Set the window title and size
        medicine_window.title("Add Medicine")
        medicine_window.geometry("300x200")
        # Create labels and entry widgets for medicine name, price and quantity
        name_label = Label(medicine_window, text="Medicine Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        global name_entry
        name_entry = Entry(medicine_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)
        price_label =Label(medicine_window, text="Medicine Price:")
        price_label.grid(row=1, column=0, padx=10, pady=10)
        global price_entry
        price_entry =Entry(medicine_window)
        price_entry.grid(row=1, column=1, padx=10, pady=10)
        quantity_label = Label(medicine_window, text="Medicine Quantity:")
        quantity_label.grid(row=2, column=0, padx=10, pady=10)
        global quantity_entry
        quantity_entry = Entry(medicine_window)
        quantity_entry.grid(row=2, column=1, padx=10, pady=10)
        # Create a button to add the medicine data to the database
        add_button = Button(medicine_window, text="Add", command=add_medicine)
        add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        show_data = Button(medicine_window, text="See the Stack", command=read_from_db)
        show_data.grid(row=4, column=0,columnspan = 2,padx = 10,pady = 10)


    # Define a function to add the medicine data to the database
    def add_medicine():
        conn = sqlite3.connect("medicine.db")
        cur = conn.cursor()
        # Get the medicine name, price and quantity from the entry widgets
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        # Check if the name, price and quantity are not empty
        if name and price and quantity:
            # Insert the medicine data into the table
            cur.execute("INSERT INTO medicine VALUES (?,?,?)", (name, price, quantity))
            conn.commit()
            # Clear the entry widgets
            name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            # Show a success message
            success_label.config(text="Medicine added successfully")
            cur.commit()
            
        else:
            # Show an error message
            success_label.config(text="Please enter all fields")
            # Create a login window object
    login_window = Toplevel()
    # Set the window title and size
    login_window.title("Login")
    login_window.attributes("-fullscreen", True)
    # Create labels and entry widgets for username and password
    username_label = Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry = Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    password_label = Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(login_window)
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    # Create a button to login
    login_button = Button(login_window, text="Login", command=login)
    login_button.grid(row=2, column=0,columnspan = 2,padx = 10,pady = 10)
    
    # cancel button
    cancel_log = Button(login_window, text = "Cancel", command=lambda: login_window.destroy())
    cancel_log.place(relx=0.5, rely=0.2)


    login_window.mainloop()


# In[7]:


"""START BAGE """

home = Tk()
home.title("Zooobaa - HOME")
home.attributes("-fullscreen", True)
home.configure(bg='#22577A')
# get the screen width and height
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()

startImag = PhotoImage(file='srtbtn.png')


startbtn = Button(home, image = startImag, cursor='circle',command = options, bg = '#22577A')
startbtn.place(relx=0.5, rely=0.5, anchor=CENTER)


loginImg = PhotoImage(file = 'login.png')
login = Button(home, image = loginImg, cursor='star', command = LOGIN,bg = '#22577A')
login.place(x=80, y=650)


home.update_idletasks()

 

home.mainloop()


    

