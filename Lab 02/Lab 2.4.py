# Student ID   : 1201200039
# Student Name : Tan Jiue Hong 

print("Invoice for Fruit Purchase")
print("-------------------------------------")

banana=float(input("Enter the quantity (comb) of bananas bought : "))
grape=float(input("Enter the quantity (kg) of grapes bought :  "))

price_b=banana*1.5
price_g=grape*5.6
total=price_b+price_g

print("Item                   QTY         PRICE     TOTAL")
print("BANANA(COMBS)          {}         RM1.50    RM{:.2F} ".format(banana,price_b))
print("GRAPE(KG)              {}         RM5.60    RM{:.2F} ".format(grape,price_g))
print("\nTotal:RM{:.2f}".format(total))