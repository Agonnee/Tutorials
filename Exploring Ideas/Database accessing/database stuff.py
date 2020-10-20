from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title("Learn to Code with Agonnee")
root.geometry("375x650")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# c for cursor because you type it a lot
c = conn.cursor()

# create a table

'''
# c.execute("""CREATE TABLE addresses(
        # first_name text,
        # last_name text,
        # address text,
        # city text,
        # state text,
        # zipcode integer
        # )""")
'''

# Create record deleting function
def delete():
    # Create a database or connect to one INSIDE THE FUNCTION THIS TIME
    conn = sqlite3.connect('address_book.db')
    # c for cursor because you type it a lot INSIDE THE FUNCTION THIS TIME
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + select_box.get())

    # commit Changes to the db
    conn.commit()
    # close connection
    conn.close()

def update():
    # Create a database or connect to one INSIDE THE FUNCTION THIS TIME
    conn = sqlite3.connect('address_book.db')
    # c for cursor because you type it a lot INSIDE THE FUNCTION THIS TIME
    c = conn.cursor()


    record_id = select_box.get()
    # Delete a record
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
         'last': l_name_editor.get(),
         'address': address_editor.get(),
         'city': city_editor.get(),
         'state': state_editor.get(),
         'zipcode': zipcode_editor.get(),

         'oid': record_id
        })

    # commit Changes to the db
    conn.commit()
    # close connection
    conn.close()

    editor.destroy()



# Create an edit Function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Edit a Record")
    editor.geometry("375x210")


    # Create a database or connect to one INSIDE THE FUNCTION THIS TIME
    conn = sqlite3.connect('address_book.db')
    # c for cursor because you type it a lot INSIDE THE FUNCTION THIS TIME
    c = conn.cursor()

    record_id = select_box.get()
    # query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    #create global variable for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create textbox labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)



    # Create save button
    save_btn = Button(editor, text="Edit record", command=update)
    save_btn.grid(row=9, column=0, columnspan=2, pady=20, padx=10, ipadx=135)



    #loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    # commit Changes to the db
    conn.commit()
    # close connection
    conn.close()

# Create Submit Function
def submit():
    # Create a database or connect to one INSIDE THE FUNCTION THIS TIME
    conn = sqlite3.connect('address_book.db')
    # c for cursor because you type it a lot INSIDE THE FUNCTION THIS TIME
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })


    # commit Changes to the db
    conn.commit()
    # close connection
    conn.close()


    # Clear the text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    # Create a database or connect to one INSIDE THE FUNCTION THIS TIME
    conn = sqlite3.connect('address_book.db')
    # c for cursor because you type it a lot INSIDE THE FUNCTION THIS TIME
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # loop through results
    print_records = ' '
    for record in records:
        print_records += str(record[6])+ ". " + str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid_forget()
    query_label.grid(row=11, column=0, columnspan=2, pady=15)


    # commit Changes to the db
    conn.commit()
    # close connection
    conn.close()

#Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
select_box = Entry(root, width=30)
select_box.grid(row=8, column=1)

# Create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
select_box_label = Label(root, text=" Select ID Number")
select_box_label.grid(row=8, column=0)


# Create a Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=10, ipadx=104)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=20, padx=10, ipadx=130)

# Create a delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=20, padx=10, ipadx=135)

# Create an update button
select_btn = Button(root, text="Edit record", command=edit)
select_btn.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=135)


# commit Changes to the db
conn.commit()

#close connection
conn.close()


root.mainloop()
