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


def add_book():
    b_name = input("Enter the book name: ")
    author = input("Enter the author name: ")
    quantity = input("Enter the quantity of books: ")

    with open ("book.txt", "a") as f:
        f.write(b_name + "," + author + "," + quantity)
        print("Details added successfully!")

def view_book():
    
    
while True:
    print("\n====Library Management System====\n")
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter the choice: ")

    if(choice=="1"):
        add_book()
    elif(choice=="2"):
        view_book()
    elif(choice=="3"):
        search_book()
    elif(choice=="4"):
        issue_book()
    elif(choice=="5"):
        return_book()
    elif(choice=="6"):
        print("See You Later!")
        break
    else:
        print("Invalid choice!")
    