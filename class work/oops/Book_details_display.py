class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ₹{self.price}/-")

b1=Book("Computer Science","JohnDoe",1799)
b1.display()