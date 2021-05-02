class Library:
    def __init__(self,ListofBooks):
        self.Books=ListofBooks


    def displayavailabalebooks(self):
        print("Books present in this library are:")
        for books in self.Books:
            print("\t." + books)
        
    def borrowbook(self,bookname):
        if bookname in self.Books:
            print(f"you have issued {bookname} book.please don't damage it and return it within time.")
            self.Books.remove(bookname)
        else:
            print("sorry this book is issued to someone please wait until he/she returns it,Sorry,for inconvineance.")    

    def returnbook(self,bookname):
        self.Books.append(bookname)
        print("thanks for returning it.,Have a great day ahead!")
class student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of the book you want to return:")
        return self.book    

    

if __name__ == '__main__':
    centralLibrary=Library(["C","DS","ALGO","TOC","CD","Database","OS","CN","DS","DLD"])
    student=student()
    #centralLibrary.displayavailabalebooks()
    while (True):
        
        welcomemsg='''=====welcome to the central library=====
        please pic the option given below:
        1. List all the books
        2. Request a book
        3. Return a book 
        4. Exit to the centralLibrary
        ''' 
        print(welcomemsg)
        a=int(input("Enter a choice:"))
        if a==1:
            centralLibrary.displayavailabalebooks()
        elif a==2:
            centralLibrary.borrowbook(student.requestbook())
        elif a==3:
            centralLibrary.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing this Library. ,Have a good day ahead!")
            exit()
        else:
            print("Wrong key") 
            


