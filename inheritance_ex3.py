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
        
class superbird(bird):
    def dive(self):
        print("A superbird can dive")
    def zoom(self):
        print("A superbird can zoom")
    def navigate(self):
        print("A superbird can navigate")
    def whaticando(self):
        super().whatcanido()
        self.dive()
        self.zoom()
        self.navigate()
        
s1 = superbird()
s1.dive()
s1.zoom()
s1.navigate()
s1.whaticando()
        
a1=animal()
a1.hunt()
a1.fight()
    
b1=bird()
b1.fly()
b1.sing()
b1.nest()
b1.whatcanido()
        