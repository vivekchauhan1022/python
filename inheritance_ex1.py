class animal:#parent
    def hunt(self):
        print("animal can hunt")
    def fight(self):
        print("animal can fight")
    
class bird(animal):#child
    def fly(self):
        print("bird can fly")
    def sing(self):
        print("bird can sing")
    def nest(self):
        print("A bird can build a nest")
    def whatcanido(self):  
        super().hunt()
        super().fight()
        
        self.fly()
        self.sing()
        self.nest()
        
a1=animal()
a1.hunt()
a1.fight()
    
b1=bird()
b1.fly()
b1.sing()
b1.nest()
b1.whatcanido()
        