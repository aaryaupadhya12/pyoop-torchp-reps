'''
avg = RunningAverage()

avg.update(10)
avg.update(20)
avg.update(30)

print(avg.average())
# 20.0

print(avg)
# RunningAverage(avg=20.0, n=3)

'''
class RunningAvergage:
    def __init__(self):
        self.total = 0
        self.n = 0
    
    def update(self,value):
        self.total += value
        self.n += 1
    
    def average(self):
        return self.total / self.n
    
    def __repr__(self):
        return f" The average value is {self.average()}"
    


if __name__ == "__main__":
    avg = RunningAvergage()
    avg.update(10)
    avg.update(30)
    avg.update(90)

    print(avg.average())
    print(avg)