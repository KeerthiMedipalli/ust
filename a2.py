class BookStore:
    NoOfBooks = 0
    def __init__(self, name, author):
        self.name = name
        self.author = author 
    
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.name} by {self.author}. No of books : {BookStore.NoOfBooks}")
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display() 
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  
