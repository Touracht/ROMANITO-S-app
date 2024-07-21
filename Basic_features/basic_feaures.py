
class Pizza:
    print("Here is our pizza list:")
    Our_pizza_list = ["Roma chicken", "Roma beef", "Roma bbq", "Roma rib" ]
    for pizza in Our_pizza_list:
        print(pizza)

    Roma_chicken = 50
    Roma_beef = 50
    Roma_bbq = 50
    Roma_rib = 50
    def __init__(self):
        # self.pizza = pizza
        self.cart = []
        
    def purchase(self):
        flavour_choice = input("Enter the favour you want: ")
        if flavour_choice == "Roma chicken".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_chicken)
            print(f"You have requested {quantity} {self.Roma_chicken}")
            Pizza.Roma_chicken -= quantity
        elif flavour_choice == "Roma Beef".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_beef * quantity)
            Pizza.Roma_beef -= quantity
        elif flavour_choice == "Roma bbq".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_bbq * quantity)
            Pizza.Roma_bbq -= quantity
        elif flavour_choice == "Roma rib".lower():
            quantity = int(input("quatity: "))
            self.cart.append(self.Roma_rib * quantity)
            Pizza.Roma_rib -= quantity
        else:
            print("Item not in our menu")
    
    def view_cart(self):
        viewing_cart = input("View cart? ")
        if viewing_cart == "yes".lower():
            for items in self.cart:
                print(items)
        elif viewing_cart == "no":
            print()

    @classmethod
    def our_pizzas(cls):
        print(f"Roma chicken: {cls.Roma_chicken}")
        print(f"Roma beef: {cls.Roma_beef}")
        print(f"Roma bbq: {cls.Roma_bbq}")
        print(f"Roma rib: {cls.Roma_rib}")

    
       
            
        
        
