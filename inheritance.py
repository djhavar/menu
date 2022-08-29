class parent:
    
    def __init__(self):
        print("this is a parent class")
        
        def menu(dish):
            if dish=="pizza":
                print("you can add the following toppings")
                print("more cheese|jalapeno")
            elif dish=="cold_coffee":
                print("you can add the following toppings")
                print("chocalate flavour|add caramel flavour")
            else:
                print("please enter valid dish")
                
                def final_amount(dish, addons):
                    if  dish=="pizza" and addons=="cheese":
                        print("you need to pay 250 rs")
                    elif  dish=="pizza" and addons=="jalapeno":
                            print("you need to pay 255 rs")
                            
                    elif  dish=="cold_coffee" and addons=="chocalate flavour":
                                print("you need to pay 175 rs")
                    elif  dish=="cold_coffee" and addons=="caramel flavour":
                                            print("you need to pay 175 rs")

class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
        
    def get_menu(self):
      parent.menu(self.new_dish)
    
    class child2(parent):
        
        def __init__(self,dish):
            self.new_dish = dish
            
        def get_final_amount(self):
         parent.final_amount(self.new_dish,self.add_ons)
        
         child1_object=child1("pizza")
         child1_object.get_menu()
        
    child2_object=child2("pizza","jalapeno")
    child2_object.get_final_amount()
      
      