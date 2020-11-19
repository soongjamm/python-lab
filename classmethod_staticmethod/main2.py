
# ==> hardcover뿐만 아닌, paperback 등 다 가능하게 하고 싶음.
# book_type과 같은 튜플을 global이 아닌 클래스에 굳이 넣는 이유는 Book클래스와 관련성을 보여주거나 Book안에서만 사용하거나 등의 이유가 있다. 
# 클래스 메소드도 마찬가지다.

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)