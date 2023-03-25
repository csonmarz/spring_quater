from item import Item
class Keyboard(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price:float, quantity=0, broken_phones = 0):
        # Call to super function to have acess to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        
        
        
        # # Run validations to the recieved arguments
        # assert quantity >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        
        # print(f"An Instance created: {name}")
        
        # #Assign to self object
        # self.broken_phones = broken_phones
        
        # # Actions to execute
        # Phone.all.append(self)

