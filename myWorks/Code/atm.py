money = int(input("Enter your number : "))
if money % 100 ==0:
    print("1000 : {}".format(money//1000))
    print("500 : {}".format(money % 1000 // 500))
    print("100 : {}".format(money % 500 // 100))
else :
    print("invulid number")