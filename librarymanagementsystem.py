# 1. Library Management System (Parbat, Sohan, Rahul)
# Question:
# Write a menu driven Python program for a Library Management System that performs the following operations.
# ===== LIBRARY MANAGEMENT SYSTEM =====
# 1. Add Book
# 2. View All Books
# 3. Search Book
# 4. Issue Book
# 5. Return Book
# 6. Exit
# Description
#  Add Book : Enter book name, author, and quantity.
#  View Books : Display all books available in library.
#  Search Book : Search book by name.
#  Issue Book : Reduce quantity when a book is issued.
#  Return Book : Increase quantity when book is returned.
#  Exit : End the program.


def addnew_book():
    b_name = input("Enter the book name: ")
    author = input("Enter the author name: ")
    quantity = input("Enter the quantity of books: ")

    with open ("book.txt", "a") as f:
        f.write(b_name + "," + author + "," + quantity + "\n")
        print("Details added successfully!")
        return

def addex_book():
    try:
        add_ex = input("Enter the book name: ")

        with open("book.txt", "r") as f:
            data = f.readlines()

        with open("book.txt", "w") as f:
            if not data:
                print("Books not found")
                return

            found = False
            for line in data:
                b_name, author, quantity = line.strip().split(",")
                quantity = int(quantity)
                if b_name.lower() == add_ex.lower():
                        x = int(input("Enter the book quantity to add: "))
                        quantity = x + quantity
                        print("Book issued successfully!")
                else:
                        print("Book out of stock")
                f.write(f"{b_name},{author},{quantity}\n")
    except FileNotFoundError:
        print("Book not found")


def view_book():
    try:
        with open("book.txt", "r") as f:
            data = f.readlines()

            if not data:
                print("record not found")
                return
            print("\n======Available Books======\n")
            for line in data:
                b_name, author, quantity = line.strip().split(",")
                print(f"Book Name: {b_name}, Author: {author}, Quantity: {quantity}")
                print()
    except FileNotFoundError:
        print("File not found")

def search_book():
    try:
        search = input("Enter the book name: ")

        with open("book.txt", "r") as f:
            data = f.readlines()

            if not data:
                print("Books not found")
                return
            found = False
            print("\n=====Book Details=====\n")
            for line in data:
                b_name, author, quantity = line.strip().split(",")
                if b_name.lower() == search.lower():
                    print(f"Book Name: {b_name}, Author: {author}, Quantity: {quantity}")
                    print()
    except FileNotFoundError:
        print("Records not found")
        
def issue_book():
    try:
        issue = input("Enter the book name: ")

        with open("book.txt", "r") as f:
            data = f.readlines()

        with open("book.txt", "w") as f:
            if not data:
                print("Books not found")
                return

            found = False
            for line in data:
                b_name, author, quantity = line.strip().split(",")
                quantity = int(quantity)
                if b_name.lower() == issue.lower():
                    if quantity > 0:
                        quantity -=1
                        print("Book issued successfully!")
                    else:
                        print("Book out of stock")
                f.write(f"{b_name},{author},{quantity}\n")
    except FileNotFoundError:
        print("Book not found")

def return_book():
    try:
        b_return = input("Enter the book name: ")

        with open("book.txt", "r") as f:
            data = f.readlines()

        with open("book.txt", "w") as f:
            if not data:
                print("Books not found")
                return

            found = False
            for line in data:
                b_name, author, quantity = line.strip().split(",")
                quantity = int(quantity)
                if b_name.lower() == b_return.lower():
                    quantity +=1
                    print("Book returned successfully!")
                    found = True
                    
                f.write(f"{b_name},{author},{quantity}\n")
    except FileNotFoundError:
        print("book not in library")

while True:
    print("\n====Library Management System====\n")
    print("1. Add New Book")
    print("2. Add Existing Book")
    print("3. View Book")
    print("4. Search Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")
    choice = input("Enter the choice: ")

    if(choice=="1"):
        addnew_book()
    elif(choice=="2"):
        addex_book()
    elif(choice=="3"):
        view_book()
    elif(choice=="4"):
        search_book()
    elif(choice=="5"):
        issue_book()
    elif(choice=="6"):
        return_book()
    elif(choice=="7"):
        print("See You Later!")
        break
    else:
        print("Invalid choice!")
    