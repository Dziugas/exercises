class Book:
    # discount
    after_2000 = 0.9

    # every book has a title, price and year
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year

# books released after 2000 have a 10% discount
def new_books(self):
    if self.year > 2000:
        self.price = self.price * Book.after_2000

class Basket:
    # discount if total sum is more than 30
    more_30 = 0.95

    def __init__(self, total, items):
        self.total = total
        self.items = items

    #total sum of the basket items
    def sum(self):
        if self.total > 30:
            self.total = self.total * Basket.more_30
            return self.total


book_1 = Book('Moby Dick', 15.20, 1851)
book_2 = Book('The Terrible Privacy of Maxwell Sim', 13.14, 2010)
book_3 = Book('Still Life With Woodpecker', 11.05, 1980)
book_4 = Book('Sleeping Murder', 10.24, 1976)
book_5 = Book('Three Men in a Boat', 12.87, 1889)
book_6 = Book('The Time Machine', 10.43, 1895)
book_7 = Book('The Caves of Steel', 8.12, 1954)
book_8 = Book('Idle Thoughts of an Idle Fellow', 7.32, 1886)
book_9 = Book('A Christmas Carol', 4.23, 1843)
book_10 = Book('A Tale of Two Cities', 6.32, 1859)
book_11 = Book('Great Expectations', 13.21, 1861)

#listas galetu generuotis automatiskai eiti per Book klases instances ir juos appendint i lista
listas = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8, book_9, book_10, book_11]


def print_list():
    print("Hallo, we have:")
    n = 1
    for book in listas:
        print("\n {}. {}".format(n, book.__dict__))
        n = n + 1


print_list()

Book.after_2000 = 0.7

for book in listas:
    if book.year > 2000:
        Book.new_books(book)


def print_list():
    print("With discounts:")
    n = 1
    for book in listas:
        print("\n {}. {}".format(n, book.__dict__))
        n = n + 1


print_list()

pirkiniai = [int(x) for x in input("enter book numbers, with a space in between: ").split()]
print(pirkiniai)

sum = 0
i = 0
#sum atskira funkcija padaryti
for x in pirkiniai:
    if x == 1:
        sum = sum + book_1.price
    elif x == 2:
        sum = sum + book_2.price
    elif x == 3:
        sum = sum + book_3.price
    elif x == 4:
        sum = sum + book_4.price
    elif x == 5:
        sum = sum + book_5.price
    elif x == 6:
        sum = sum + book_6.price
    elif x == 7:
        sum = sum + book_7.price
    elif x == 8:
        sum = sum + book_8.price
    elif x == 9:
        sum = sum + book_9.price
    elif x == 10:
        sum = sum + book_10.price
    elif x == 11:
        sum = sum + book_11.price
    else:
        print("no such book")
    i += 1

print("Total amount is {}".format(sum))

basket = Basket(sum, i)
print(basket.__dict__)

Basket.more_30 = 0.5
print("Amount after discount is {}".format(Basket.sum(basket)))