from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Database")
root.iconbitmap("C:/Users/Olivetti/Downloads/minecrafticon.ico")
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create a cursor
cursor = conn.cursor()

# Create table
# cursor.execute("""CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    country text,
#    number integer
#    )""")


def edit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create a cursor
    cursor = conn.cursor()

    record_id = delete_box.get()
    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name= :last,
        address= :address,
        city= :city,
        country= :country,
        number = :number

        WHERE oid = :oid""",
                   {"first": f_name_editor.get(),
                    "last": l_name_editor.get(),
                    "address": address_editor.get(),
                    "city": city_editor.get(),
                    "country": country_editor.get(),
                    "number": number_editor.get(),

                    "oid": record_id
                    })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    editor.destroy()

# Create a delete function for database


def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create a cursor
    cursor = conn.cursor()

    # Delete a record
    cursor.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create update function
def update():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap("C:/Users/Olivetti/Downloads/minecrafticon.ico")
    editor.geometry("400x300")

    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create a cursor
    cursor = conn.cursor()

    record_id = delete_box.get()

    # Query the database
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cursor.fetchall()

    # Create Global Variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global country_editor
    global number_editor

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    country_editor = Entry(editor, width=30)
    country_editor.grid(row=4, column=1)
    number_editor = Entry(editor, width=30)
    number_editor.grid(row=5, column=1)

    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    country_label = Label(editor, text="Country")
    country_label.grid(row=4, column=0)
    number_label = Label(editor, text="Number")
    number_label.grid(row=5, column=0)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        country_editor.insert(0, record[4])
        number_editor.insert(0, record[5])

    # Create an Update Button
    update_button = Button(editor, text="Update Records", command=edit)
    update_button.grid(row=6, column=0, columnspan=2,
                       padx=10, pady=10, ipadx=134)


# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create a cursor
    cursor = conn.cursor()

    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :country, :number)",
                   {
                       "f_name": f_name.get(),
                       "l_name": l_name.get(),
                       "address": address.get(),
                       "city": city.get(),
                       "country": country.get(),
                       "number": number.get()
                   })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)
    number.delete(0, END)


def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create a cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print(records)

    # Loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + \
            str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
country = Entry(root, width=30)
country.grid(row=4, column=1)
number = Entry(root, width=30)
number.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
country_label = Label(root, text="Country")
country_label.grid(row=4, column=0)
number_label = Label(root, text="Number")
number_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_button = Button(root, text="Add record to database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=112)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Delete Button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=138)

# Create an Update Button
update_button = Button(root, text="Edit Records", command=update)
update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=134)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
