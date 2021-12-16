import math
light = [int(i) for i in input("Enter n,m : ").split()]
plan = [int(i) for i in input("Enter n,m : ").split()]
man = int(input("Enter man number :  "))

light_cost = 0
for row in range(0, light[0]):
        light_cost += sum ([int(i) for i in input("light: ").split()])

oil_cost = plan[0] * plan[1] * man

ticket_price = (light_cost + oil_cost) / man

print(math.ceil(ticket_price))
