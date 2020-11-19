
# Bookshelf를 상속받아 Book을 구현하면 Quantity를 인위적으로 숨겨야 한다.

# 생기는 문제
# 1. Conceptual : 상속은 Bookshelf + something more란 의미가 되는데, 둘은 다르다. Bookshelf의 속성을 사용하지 않는다. (quantity)
# 2. Technical : 사용하지 않을건데 상속을 할 이유가 없다.

# 그래서 Bookshelf의 인자를 *books로 바꿔준다.  Book은 quantity가 필요없고 상속을 받지 않아도 된다.

class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = Bookshelf(book, book2)

print(shelf)