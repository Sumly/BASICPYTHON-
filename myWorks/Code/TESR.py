import math
wight1 = int(input("Enter weight1 "))
wight2 = int(input("Enter weight2 "))
wight3 = int(input("Enter weight3 "))
wight_all =(wight1 + wight2 + wight3) / 3
int(wight_all)
if wight_all <= 25 :
    print("Aveage weight is "+ str( wight_all)+" cat")
elif wight_all >=25 and wight_all <=30 :
    print("Aveage weight is "+ str( wight_all)+" bird")
elif wight_all  >=31 and wight_all <=45  :
    print("Aveage weight is "+ str( wight_all)+" horse")
else :
    print("thank you")