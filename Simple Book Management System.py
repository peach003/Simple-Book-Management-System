def add_book(book_list, title, author):
    for existing_title, existing_author in book_list:
        if existing_title == title and existing_author == author:
            print("Book already exists in the collection.")
            return
    book_list.append((title, author))
    print(f"Book '{title}' by {author} added successfully.")

def remove_book(book_list, title):
    for book_title, _ in book_list:
        book_list.remove(book_title, _)
        print(f"Book '{title}' removed successfully.")
        return
    print("Book not found in the collection.")

def search_book(book_list, title):
    for book_title, author in book_list:
        if book_title == title:
            print(f"Book found: '{title}' by {author}")
            return
    print("Book not found in the collection.")

def main():
    book_list = []
    while True:
        command = input("Enter command (ADD title, author / REMOVE title / SEARCH title): ").split()
        if len(command) < 2:
            print("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")
            continue
        if command[0] == 'ADD':
            if len(command) < 3:
                print("Invalid input. Please provide both title and author for adding a book.")
                continue
            title = ' '.join(command[1:-1])
            author = command[-1]
            add_book(book_list, title, author)
        elif command[0] == 'REMOVE':
            title = ' '.join(command[1:])
            remove_book(book_list, title)
        elif command[0] == 'SEARCH':
            title = ' '.join(command[1:])
            search_book(book_list, title)
        else:
            print("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

if __name__ == "__main__":
    main()









