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


    
"--------------------------------"
"""The classes above are to be used to solve the new problem. Do not change or even look at them unless absolutely needed."""

# Requirments... 
"""
- Create a catalog class that can validate SKU's. 
    - It can do this by having a list or dictonary. I prefer dictonary with valid key names being skus. And their values being 0 or 1
    reperesenting if they are valid or not...
    - If it is valid we should return a LineItem object for that SKU with the quantity also passed in.



"""

class Product:
    def __init__(self,sku: str, name: str, price: Money, in_stock=True):
        self.sku = sku
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def __str__(self):
        return f"{self.sku} - {self.name} ({self.price}) [{'In stock' if self.in_stock else 'Out of stock'}]"

class Catalog:
    def __init__(self):
        # dictionary: sku -> Product
        self.skus: dict[str, Product] = {}

    def add_product(self, product: Product):
        self.skus[product.sku] = product

    def get(self, sku: str) -> Product:
        if sku not in self.skus:
            raise KeyError(f"Unknown SKU {sku}")
        return self.skus[sku]

class Cart:
    def __init__(self):
        self.items = []
        self.catalog = Catalog()
    def add(self, sku : str, qty: int):
        product = self.catalog.get(sku)
        if product:
            self.items.append(LineItem(product.sku, product.name, product.price, qty))
            


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
    
def test():
    # --- test setup ---
    catalog = Catalog()
    catalog.add_product(Product("A1", "Socks", Money(299)))
    catalog.add_product(Product("A2", "Shirt", Money(1299), in_stock=True))
    catalog.add_product(Product("A3", "Hat", Money(599), in_stock=False))

    cart = Cart()

    # Try adding a known, valid SKU
    cart.add("A1", 2)   # 2 x Socks

    # Try adding another valid SKU
    cart.add("A2", 1)   # 1 x Shirt

    # Try adding an out-of-stock SKU
    try:
        cart.add("A3", 1)
    except Exception as e:
        print("Expected error (out of stock):", e)

    # Try adding an unknown SKU
    try:
        cart.add("X9", 1)
    except Exception as e:
        print("Expected error (unknown):", e)

    # Check totals and contents
    print("Cart contains:")
    for item in cart.items:
        print(f" - {item.sku} {item.name} x{item.qty} -> {item.total()}")

    print("Cart total =", cart.total())

test()