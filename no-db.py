# This version of Book Nook uses lists only.

books = []
# print_inventory_count(): Displays how many total books there are in a readable format.
def print_inventory_count():
    print("There are " + str(len(books)) + " books in your inventory.")

#add_book(item): Adds a book to the inventory.
def add_book(item):
    books.append(item)
    print(item + " was added successfully.")

#remove_book(item): Removes a book from the inventory.
def remove_book(item):
    if item in books:
        books.remove(item)
        print(item + " was removed successfully.")
    else:
        print("Error: " + item + " not in inventory.")

# display_inventory
def display_inventory():
    count = 1
    for book in books:
        print(str(count) + ". " + book)
        count += 1
    print("\n")

# Welcome message
print("\nWelcome to Book Nook!\n")
while True:
    print("Menu: \n Add book (add)\n Remove book (remove) \n Show inventory (show) \n Show inventory count (count) \n Quit (q)\n")
    user_selection = input("What would you like to do? ").lower()

    if user_selection == "add":
        book = input("What book would you like to add? ")
        add_book(book)
    elif user_selection == "remove":
        book = input("What book would you like to remove? ")
        remove_book(book)
    elif user_selection == "count":
        print_inventory_count()
    elif user_selection == "show":
        print_inventory_count()        
        display_inventory()
    elif user_selection == "q":
        print("Bye bye!")
        break
    else:
        print("Error: That was not an option.\n")

    print("\n")