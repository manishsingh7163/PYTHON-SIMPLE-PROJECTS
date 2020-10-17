class Bike:
    def __init__(self):
       self.name,self.color,self.speed,self.price,self.cc
    def get(self):
        self.name=input("Enter the Name of Bike :  ")
        self.color=input("Enter the Color       :  ")
        self.speed=int(input("Enter the Speed      :  "))
        self.price=int(input("Enter the Price      :  "))
        self.cc=int(input("Enter the CC            :  "))
    def display(self):
        print("%-10s%-10s\t%d\t%d\t%d"%(self.name,self.color,self.speed,self.price,self.cc))
        #print(self.name,"\t",self.color,"\t",self.speed,"\t",self.price,"\t",self.cc)
class Hero(Bike):
    def __init__(self):
        print("Enter the Details of Hero Bike :  ")
class Honda(Bike):
    def __init__(self):
        print("Enter the Details of Honda Bike :  ")
class Bajaj(Bike):
    def __init__(self):
        print("Enter the Details of Bajaj Bike :  ")
class Yamaha(Bike):
    def __init__(self):
        print("Enter the Details of Yamaha Bike :  ")
h1=Hero()
h1.get()
h2=Honda()
h2.get()
h3=Bajaj()
h3.get()
h4=Yamaha()
h4.get()
print("Name      Color     Speed\tPrice\tCC")
h1.display()
h2.display()
h3.display()
h4.display()
input()
