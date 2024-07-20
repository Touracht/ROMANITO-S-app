class Pizza:
    Roma_chicken = 50
    Roma_beef = 50
    Roma_bbq = 50
    Roma_rib = 50
    def __init__(self,pizza):
        self.pizza = pizza
        self.cart = []
        Pizza.Roma_chicken -= 1
        Pizza.Roma_beef -= 1
        Pizza.Roma_bbq -= 1
        Pizza.Roma_rib -= 1

    def purchase(self):
        flavour_choice = int("Enter the favour you want: ")
        if flavour_choice == "Roma chicken".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_chicken * quantity)
        elif flavour_choice == "Roma Beef".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_beef * quantity)
        elif flavour_choice == "Roma bbq".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_bbq * quantity)
        elif flavour_choice == "Roma rib".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_rib * quantity)
        else:
            print("Item not in our menu")
    
    def view_cart(self):
        for items in self.cart:
            print(items)
        
    @classmethod
    def our_pizzas(cls):
        our_pizzas = ["Roma chicken", "Roma beef", "Roma bbq", "Roma rib"]
        for pizza in our_pizzas:
            print(pizza)
        
        
