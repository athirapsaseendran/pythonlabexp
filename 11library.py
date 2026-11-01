def add_book():
    with open("library.txt", "a") as f:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        f.write(title + "," + author + "\n")
    print("Book added successfully")

def search_book():
    key = input("Enter title or author to search: ").lower()
    with open("library.txt", "r") as f:
        for line in f:
            if key in line.lower():
                print(line.strip())

def report():
    with open("library.txt", "r") as f:
        books = f.readlines()
    print("Total books:", len(books))

while True:
    print("\n1.Add Book  2.Search Book  3.Report  4.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        add_book()
    elif ch == '2':
        search_book()
    elif ch == '3':
        report()
    else:
        break