# This version of Book Nook uses a database!
import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create a table
# use triple quotes for a multi-line string in python
cursor.execute('''CREATE TABLE IF NOT EXISTS Library
                  (Title TEXT NOT NULL,
                  Description TEXT NULL)''')


# print_inventory_count(): Displays how many total books there are in a readable format.
def print_inventory_count():
    cursor.execute("SELECT COUNT(Title) FROM Library")
    # fetch returns the query result and because COUNT returns one row (the count), we use fetchone
    count = cursor.fetchone()[0]
    print("\nThere are " + str(count) + " books in your inventory.")

#add_book(item): Adds a book to the inventory.
def add_book(item):
    cursor.execute("INSERT INTO Library VALUES ('"+ item +"', NULL)")
    # must commit after every insert query?
    conn.commit()
    print("\n"+ item + " was added successfully.")

#remove_book(item): Removes a book from the inventory.
def remove_book(item):
    cursor.execute("DELETE FROM Library WHERE Title ='"+ item +"'")
    conn.commit()
    print(item + " was removed successfully.")

# display_inventory
def display_inventory():
    # Execute a SELECT query
    cursor.execute("SELECT * FROM Library")
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print("\nTitle:", row[0])
        print("Desc:", row[1])
        if(row[2] == 0):
            print("Checked out:", "False \n")
        else:
            print("Checked out:", "True \n")


#checked out functiion
 
def checked_out(item):

    cursor.execute("SELECT Checked_out FROM library Where Title = '"+ item +"' ")
    row = cursor.fetchone()
    if(row[0] == 1):
        print(" \n already checked out")
    else:
        cursor.execute("UPDATE library SET Checked_out = 1 WHERE Title = '"+ item +"'")
        conn.commit()
        print("You have checked out " + item)


#return book function

def return_book(item):
    cursor.execute("SELECT Checked_out FROM library Where Title = '"+ item +"' ")
    row = cursor.fetchone()
    if(row[0] == 0):
        print("\n already returned")
    else:
        cursor.execute("UPDATE library SET Checked_out = 0 WHERE Title = '"+ item +"'")
        conn.commit()
        print("\nYou have returned " + item)
#genre function
# adding anotha column - varchar(50)

#edit function
#update title

# Welcome message
print("      ______ ______")
print("    _/      Y      \\_")
print("   // BOOK  | ~~ ~  \\\\")
print("  // ~ ~ ~~ |  NOOK  \\\\ ")
print(" //________.|.________\\\\ ")
print("`----------`-'----------'")
print("\nWelcome to Book Nook!\n")
while True:
    print("Menu: \n Add book (add)\n Remove book (remove) \n Show inventory (show) \n Show inventory count (count) \n Check out (check) \n Return book (return) \n Quit (q)\n")
    user_selection = input("What would you like to do? ").lower().strip()

    if user_selection == "add":
        book = input("What book would you like to add? ").strip()
        add_book(book)
    elif user_selection == "remove":
        book = input("What book would you like to remove? ").strip()
        remove_book(book)
    elif user_selection == "count":
        print_inventory_count()
    elif user_selection == "show":
        print_inventory_count()        
        display_inventory()
    elif user_selection == "check":
        display_inventory() 
        book = input("\n Enter the book title that you'd like to check out? ").strip()
        checked_out(book)  
    elif user_selection == "return":
        display_inventory() 
        book = input("\n Enter the book title that you'd like to check out? ").strip()
        return_book(book)       
    elif user_selection == "q":
        print("Bye bye!")
        break
    else:
        print("Error: That was not an option.\n")

    print("\n")

# Close the cursor and connection 
cursor.close()
conn.close()