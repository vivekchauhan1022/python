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
        

inch=int(input("enter inch : "))
f1 = foot(inch)
foot = f1.getfoot()

print("foot =",foot)

m1=meter(inch)
meter = m1.getmeter()

print("meter =",meter)
    