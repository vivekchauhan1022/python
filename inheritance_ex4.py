class foot():
    def __init__(self,inch):
        self.inch=inch
        print("constructor called...")
    
    def getfoot(self):
        
        foot = self.inch / 12
        return foot
        
class meter(foot):
    def __init__(self,inch):
        super().__init__(inch)
        print("constructor called...")
        
    def getmeter(self):
        meter = super().getfoot() * 0.3024
        return meter
        
class kilometer(meter):
    def __init__(self,inch):
        super().__init__(inch)
    def getkilometer(self):
        kilometer = super().getmeter() / 1000
        return kilometer


inch=int(input("enter inch : "))

k1 = kilometer(inch)
    
kilometer = k1.getkilometer()
meter = k1.getmeter()
foot = k1.getfoot()

print("kilometer =",kilometer)
print("meter = ",meter)
print("foot = ",foot)

    