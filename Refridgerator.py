class Refridgerator: 

    fridgelist = [];
    def __init__(self, capacity):
        self.capacity = capacity; 
        self.fridgelist = [capacity];

    def addItem(self, produce, amount): 
        for amount in produce.amount(); 
        self.fridgelist.append(produce); 

    def check_for_expired(self): 
        for items in self.fridgelist: 
            print(items, items.get_days_until_expiration());
            if(self.items.get_days_until_expiration() ==


    
