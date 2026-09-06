"""
tracker = TemperatureTracker()

tracker.add(30)
tracker.add(25)
tracker.add(35)

print(tracker.average())   # 30.0
print(tracker.maximum())   # 35
print(tracker.minimum())   # 25
print(tracker)             # TemperatureTracker(avg=30.0, min=25, max=35, n=3)
"""

class TemperatureTracker:
    def __init__(self):
        self.temp = list()
        self.n = len(self.temp)
    
    def add(self,value):
        self.temp.append(value)
        self.n = len(self.temp)
    
    def average(self):
        self.x = sum(self.temp)
        return self.x / self.n
    
    def maximum(self):
        return max(self.temp)
    
    def minimum(self):
        return min(self.temp)
    
    def __repr__(self):
        return f"print average {self.average()} , {self.maximum()} , {self.minimum()}"


if __name__ == "__main__":
    t = TemperatureTracker()
    t.add(20)
    t.add(30)
    t.add(40)
    print(t)
    print(t.average())
    print(t.maximum())
    print(t.minimum())





