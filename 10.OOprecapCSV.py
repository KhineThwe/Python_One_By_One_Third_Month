#csv = comma separated value
import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"Price{price} is not greater than or equal to zero!"
        assert quantity>=0,f"Quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        if self.quantity>0:
            return self.price * self.quantity
        return self.price
    def apply_discount(self):
        self.price = self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv","r") as f:
            reader = csv.DictReader(f)#dict
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

# item1 = Item("Phone",1000,2)
# item2 = Item("Laptop",1000,3)
# item3 = Item("Cable",1000,1)
# item4 = Item("Mouse",1000,3)
# item5 = Item("Glass",1000,1)
# item6 = Item("Keyboard",1000,3)
# print(Item.all)
# for i in Item.all:
#     print(i)

Item.instantiate_from_csv()
print(Item.all)
