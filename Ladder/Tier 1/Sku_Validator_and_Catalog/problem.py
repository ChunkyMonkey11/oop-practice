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
    
"--------------------------------"
"""The classes above are to be used to solve the new problem. Do not change or even look at them unless absolutely needed."""

# Requirments... 
"""
- Create a catalog class that can validate SKU's. 
    - It can do this by having a list or dictonary. I prefer dictonary with valid key names and 0 or 1 to reperesent return statemnt.

"""