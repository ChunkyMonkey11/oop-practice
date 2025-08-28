class Money:
    def __init__(self, cents=0):
        self.cents = cents
    
    # We need three methods from this point on. Add Multipky and str

    def add(self, other : "Money"):
        return Money(self.cents + other.cents)

    def multiply(self,factor):
        return Money(self.cents * factor)    
    def __str__(self):
        return f"{self.cents/100}"


class LineItem:
    def __init__(self, sku, name, unit_price : Money, qty : int):
       if qty <= 0:
           raise ValueError("Quantity must be greater than 0 ")

       self.sku = sku
       self.name = name
       self.unit_price = unit_price
       self.qty = qty

    # Now we need to construct a total method that returns the total of the line item

    def total(self):
        return self.unit_price.multiply(self.qty)



"""
Build a class called Cart. 
- Cart contains a list attribute that holds LineItem objects.
Methods to construct within Cart.
    - add(item)
    - remove(sku)
    - total which returns the total value of the cart.

"""

class Cart:
    def __init__(self):
        self.items = []
    
    def add(self, item : LineItem):
        self.items.append(item)

    def remove(self,sku : str):
        """
        We can go over each item in the list. Keeping track of its index.
        If we find the LineItem with the sku number we are looking for. Remove it.
        """
        for i,item in enumerate (self.items):
            if item.sku ==  sku:
                del self.items[i]
                return
    
    def total(self):
        # To calculate the final total I believe our best bet is to have a variable total that adds all the existing totals of each lineitem.
        total = Money(0)
        for item in self.items:
            total = total.add(item.total())
        return total
    

item1 = LineItem("A1", 'socks', Money(299), 2)
item2 = LineItem("A2", 'underwear', Money(101), 2)

cart = Cart()

cart.add(item1)

print(f"The total after adding item 1 is {cart.total()}")

cart.remove("A1")

print(f"The total of the cart after removing item with SKU A1 is {cart.total()}")