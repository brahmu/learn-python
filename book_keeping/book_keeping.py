
# class Book:


# Premetive


# class Employee:  # Class
#     isLogin = True  # | False

#     def __init__(self, name, age, salary):  # constructor
#         self.name = name  # "Saboo"
#         self.age = age  # 50
#         self.salary = salary  # 2000000.99
#         print("calling...")

#     def getFullInfo(self):
#         return "{ name: " + self.name + ", age: " + str(self.age) + ", login: " + str(self.isLogin)+ "}"

#     def offline(self):
#       self.isLogin = False

#     def changeState(self, status):
#       self.isLogin = status

# saboo = Employee("Saboo", 50, 2000000.99)  # Object

# # print("Saboo salary: " + str(saboo.salary))
# # print("Saboo name: " + saboo.name)
# # print("Saboo login: " + str(saboo.isLogin))

# print(saboo.getFullInfo())
# saboo.offline()

# print(saboo.getFullInfo())

# saboo.changeState(True)

# print(saboo.getFullInfo())

# Book
class Book:
    name = "UNKNOWN"
    author_name = "UNKNOWN"
    num_pages = 0
    price = 0
    publisher = "UNKNOWN"

    def __init__(self, id, name, author_name, num_pages, price, publisher):
        self.name = name
        if author_name != None:
            self.author_name = author_name
        self.num_pages = num_pages
        self.price = price
        self.id = id
        if publisher != None:
            self.publisher = publisher

    def getPrice(self):
        return "$ " + str(self.price)

    def raisePrice(self, percent):
        self.price = self.price * (100 + percent)/100

    def toString(self):
        return (
            "{ id: " + self.id +
            ", name: " + self.name +
            ", author_name: " + self.author_name +
            ", num_pages: " + str(self.num_pages) +
            ", price: " + str(self.price) +
            ", publisher: " + self.publisher +
            "}"
        )


book1 = Book("01", "Saboo ki kathaye", "Saboo", 3000,
             20.45, None)  # saboo
book2 = Book("02", "Megha ki kathaye", "Megha", 30,
             200.45, "Brahm Publication")  # megha

print(book1.name)

print(book1.toString())

print("Price of the book: " + book2.getPrice())  # 200.45

print(book2.toString())

# Selling price increased

book2.raisePrice(10)

print("Price of the book: " + book2.getPrice())  # 200.45

# print(book2.toString())

class BookManger:
  books = [book1, book2]
  
  # TODO: 
  # constructor
  # bookmanager = BookManger(book1, book2)

  # TODO: 
  # readAll # print all using loop
  # readAll
  # { id: 01, name: Saboo ki kathaye, author_name: Saboo, num_pages: 3000, price: 20.45, publisher: UNKNOWN}
  # { id: 02, name: Megha ki kathaye, author_name: Megha, num_pages: 30, price: 200.45, publisher: Brahm Publication}

# book11 = bookmanager.books[0]
# print(book11) # book1

# print(book11.toString()) # book1


