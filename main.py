from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from tkinter import filedialog as fd

# importing pillow

from PIL import Image, ImageTk

# importing Tkcalendar

from tkcalendar import Calendar, DateEntry
from datetime import date

# importing view

from view import *

# colors -------------------------------------------------------------------------------------------------------------------------

co0 = "#2e2d2b" # black
co1 = "#feffff" # white
co2 = "#4fa882" # green
co3 = "#38576b" # value
co4 = "#403d3d" # letter
co5 = "#e06626" # profit
co6 = "#038cfc" # blue
co7 = "#ADD8E6" # light blue
co8 = "#263238" # + green
co9 = "#e9edf5" # + green

# making window ------------------------------------------------------------------------------------------------------------------

window = Tk()
window.title('')
window.geometry('900x620')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")

# functions ----------------------------------------------------------------------------------------------------------------------

global tree

# add function

def add():

    global image, image_string, l_image

    name = e_name.get()
    place = e_place.get()
    description = e_description.get()
    brand = e_brand.get()
    date = e_cal.get()
    price = e_price.get()
    series = e_series.get()
    image = image_string

    insert_list = [name, place, description, brand, date, price, series, image]

    for i in insert_list:
        if i=='':
            messagebox.showerror('Error', 'Fill all fields')
            return
    insert_form(insert_list)

    messagebox.showinfo('Sucess', 'The data was inserted successfully')

    e_name.delete(0,'end')
    e_place.delete(0,'end')
    e_description.delete(0,'end')
    e_brand.delete(0,'end')
    e_cal.delete(0,'end')
    e_price.delete(0,'end')
    e_series.delete(0,'end')

    show()

# update function

def update():
    global image, image_string, l_image
    try:
        treev_data = tree.focus()
        treev_dictionary = tree.item(treev_data)
        treev_list = treev_dictionary['values']

        value = treev_list[0]

        e_name.delete(0,'end')
        e_place.delete(0,'end')
        e_description.delete(0,'end')
        e_brand.delete(0,'end')
        e_cal.delete(0,'end')
        e_price.delete(0,'end')
        e_series.delete(0,'end')
        
        id = int(treev_list[0])

        e_name.insert(0, treev_list[1])
        e_place.insert(0, treev_list[2])
        e_description.insert(0, treev_list[3])
        e_brand.insert(0, treev_list[4])
        e_cal.insert(0, treev_list[5])
        e_price.insert(0,treev_list[6])
        e_series.insert(0, treev_list[7])
        image_string = treev_list[8]

        def to_update():
            global image, image_string, l_image

            name = e_name.get()
            place = e_place.get()
            description = e_description.get()
            brand = e_brand.get()
            date = e_cal.get()
            price = e_price.get()
            series = e_series.get()
            image = image_string

            if image == '':
                image = e_series.insert(0, treev_list[7])


            update_list = [name, place, description, brand, date, price, series, image, id]

            for i in update_list:
                if i=='':
                    messagebox.showerror('Error', 'Fill all fields')
                    return
            
            update_form(update_list)
            messagebox.showinfo('Sucess', 'The data was updated successfully')

            e_name.delete(0,'end')
            e_place.delete(0,'end')
            e_description.delete(0,'end')
            e_brand.delete(0,'end')
            e_cal.delete(0,'end')
            e_price.delete(0,'end')
            e_series.delete(0,'end')

            b_confirm_update.destroy()

            show()

        b_confirm_update = Button(mainframe, command=to_update, width=13, text='confirm update'.upper(), overrelief=RIDGE, font=('Ivi 8 bold'), bg=co2, fg=co1)
        b_confirm_update.place (x=330, y=185)

    except IndexError:
        messagebox.showerror('Error', 'Select a data from the table') 

# delete function

def delete():
    try:
        treev_data = tree.focus()
        treev_dictionary = tree.item(treev_data)
        treev_list = treev_dictionary['values']

        value = treev_list[0]
       
        delete_form([value])

        messagebox.showinfo('Sucess', 'The data was deleted successfully')

        show()

    except IndexError:
        messagebox.showerror('Error', 'Select a data from the table')


# choose image function

global image, image_string, l_image

def choose_image():

    global image, image_string, l_image
    image = fd.askopenfilename()
    image_string = image

    # item image

    image = Image.open(image)
    image = image.resize((170,170))
    image = ImageTk.PhotoImage(image)

    l_image = Label(mainframe, image=image, bg=co1, fg=co4)
    l_image.place(x=700, y=10) 

# see image

def see_image():

    global image, image_string, l_image

    treev_data = tree.focus()
    treev_dictionary = tree.item(treev_data)
    treev_list = treev_dictionary['values']

    value = [int(treev_list[0])]

    item = read_item(value)

    image = item[0][8]

    image = Image.open(image)
    image = image.resize((170,170))
    image = ImageTk.PhotoImage(image)

    l_image = Label(mainframe, image=image, bg=co1, fg=co4)
    l_image.place(x=700, y=10)  

# making frames ------------------------------------------------------------------------------------------------------------------

# upper frame

upperframe = Frame(window, width=1043, height=50, bg=co1, relief=FLAT)
upperframe.grid(row=0, column=0)

# main frame

mainframe = Frame(window, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
mainframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# lower frame

lowerframe = Frame(window, width=1043, height=300, bg=co1, pady=20, relief=FLAT)
lowerframe.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# working on upper frame ---------------------------------------------------------------------------------------------------------

# app logo

app_img = Image.open('inventory.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(upperframe, image=app_img, text=' Factory Inventory', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)  

# working on main frame ----------------------------------------------------------------------------------------------------------

# making entries fields in main frame

# name fields

l_name = Label(mainframe, text='Name', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_name.place(x=10, y=10)

e_name = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_name.place (x=130, y=11)

# place fields

l_place = Label(mainframe, text='Place', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_place.place(x=10, y=40)

e_place = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_place.place (x=130, y=41)

# description fields

l_description = Label(mainframe, text='Description', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_description.place(x=10, y=70)

e_description = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_description.place (x=130, y=71)

# brand fields

l_brand = Label(mainframe, text='Brand', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_brand.place(x=10, y=100)

e_brand = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_brand.place (x=130, y=101)

# calendar fields

l_cal = Label(mainframe, text='Purchase date', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)

e_cal = DateEntry(mainframe, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal.place (x=130, y=131)

# price fields

l_price = Label(mainframe, text='Price', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_price.place(x=10, y=160)

e_price = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_price.place (x=130, y=161)

# series fields

l_series = Label(mainframe, text='Series', height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_series.place(x=10, y=190)

e_series = Entry(mainframe, width=30, justify=LEFT, relief=SOLID)
e_series.place (x=130, y=191)

# item image field

l_image = Label(mainframe, text='Item image', width=30, height=(1), anchor=NW, font=('Ivi 10 bold'), bg=co1, fg=co4)
l_image.place(x=10, y=220)


# making buttons in main frame

# load image button

b_load = Button(mainframe, command=choose_image, width=25, text='load image'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivi 8 bold'), bg=co1, fg=co0)
b_load.place (x=130, y=221)

# add item button

img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_add = Button(mainframe, command=add, image=img_add, width=95, text='  add item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=co1, fg=co0)
b_add.place (x=330, y=10)

# update button

img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(mainframe, command=update, image=img_update, width=95, text='  update'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=co1, fg=co0)
b_update.place (x=330, y=50)

# delete button

img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(mainframe, command=delete, image=img_delete, width=95, text='  delete'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=co1, fg=co0)
b_delete.place (x=330, y=90)

# see image button

img_see = Image.open('see.png')
img_see = img_see.resize((20,20))
img_see = ImageTk.PhotoImage(img_see)

b_see = Button(mainframe, command=see_image, image=img_see, width=95, text='  see image'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=co1, fg=co0)
b_see.place (x=330, y=221)

# working on lower frame ---------------------------------------------------------------------------------------------------------

# creating tabel

# show function 

def show():
    global tree

    # creating a treeview with dual scrollbars
    
    tabel_head = ['#Item','Name',  'Place', 'Description', 'Brand', 'Purchase date','Price', 'Series']
    
    itens_list = read_form()
    
    tree = ttk.Treeview(lowerframe, selectmode="extended",columns=tabel_head, show="headings")
    
    # vertical scrollbar
    
    vsb = ttk.Scrollbar(lowerframe, orient="vertical", command=tree.yview)
    
    # horizontal scrollbar
    
    hsb = ttk.Scrollbar(lowerframe, orient="horizontal", command=tree.xview)
    
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    lowerframe.grid_rowconfigure(0, weight=12)
    
    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0
    
    for col in tabel_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
    
    # adjust the column's width to the header string
    
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
    
    # add itens in the total cost field and total quantity field on the upper frame --------------------------------------------------
    
    for item in itens_list:
       tree.insert('', 'end', values=item)
    
    quantity = [8888,88]

show()

window.mainloop()