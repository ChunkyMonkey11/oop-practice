class Money:
    def __init__(self, cents=0):
        self.cents = cents
    
    # We need three methods from this point on. Add Multipky and str

    def add(self,amount):
        return Money(self.cent + amount)

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






item = LineItem("A1", 'socks', Money(299), 2).total()
print(item)
