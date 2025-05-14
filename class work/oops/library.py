class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author

class Library:
  def __init__(self):
    self.booklist=[]
  def add_newbook(self,title,author):
    self.booklist.append(Book(title,author))
    print("Book added successfully!!")
  def view_all(self):
    for i in self.booklist:
      print(f"{i.title} by {i.author}")
  def search_book(self,t):
    for i in self.booklist:
      if i.title==t:
        print(f"{i.title} by {i.author}")
        break
      else:
        print("Book not found")
l=Library()
while True:
  print("1.Add Book\n2.View Books\n3.Search Book\n4.Exit")
  option=int(input("Enter the option from above: "))
  if option==1:
    title=input("Enter Title: ")
    author=input("Enter Author: ")
    l.add_newbook(title,author)
  elif option==2:
    print("Books present in Library : ")
    l.view_all()
  elif option==3:
    k=input("Enter Book name: ")
    l.search_book(k)
  elif option==4:
    break
  else:
    print("Incorrect option, Enter again!!!")