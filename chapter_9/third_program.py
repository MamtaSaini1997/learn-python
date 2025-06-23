# create a class called Order which stores item & its price. 
# use Dunder fumction__gt__() to convey that:
#   order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, order2):
        if (self.price > order2.price):
            print("True")
        else:
            print("False")

o1 = Order("book", 20)
o2 = Order("table", 30)
o1 > o2