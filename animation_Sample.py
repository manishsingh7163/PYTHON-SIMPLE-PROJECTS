import turtle as tl
import random
x = int(input("enter the length"))
colors = ["red", "green", "blue", "brown", "orange", "violet"]
y =90
i = 0
tl.forward(x)
j = x //4
while i < j:
    tl.right(y)
    tl.color(random.choice(colors))
    tl.dot()
    tl.forward(x)
    tl.right(y)
    tl.color(random.choice(colors))
    tl.dot()
    tl.forward(x)
    x -= 4
    i += 1
