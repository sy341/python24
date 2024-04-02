# ISHS Cafe
# caffe latte: 2500, americano: 1500

beverage = ["Americano", "Caffe latte", "Iced tea"]
price = [1500, 2500, 2300]
total_price = 0
quantity = [0, 0, 0]

menu_lists = ''
for m in range(len(beverage)):
    menu_lists = menu_lists + f"{m+1} {beverage[m]} {price[m]won}  "

while True: #주문 종료 시까지 돌리는 게 키오스크.
    menu = input(menu_lists + "m+1"") end order : ")
    if menu == '4':
        print ("Exit program")
        break
    elif menu == '3':
        print("You ordered caffe latte. The price is 2300 won.")
        total_price = total_price + price[2]
        quantity[2] = quantity[2] + 1
    elif menu == '2':
        print ("You ordered caffe latte. The price is 1500 won.")
        total_price = total_price + price[1]
        quantity[1] = quantity[1] + 1
    elif menu == '1':
        print("You ordered americano. The price is 2500 won.")
        total_price = total_price + price[0]
        quantity[0] = quantity[0] + 1
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")

for i in range (len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\n\t{price[i]}\tx{quantity[i]}\t{price[i] * quantity[i]}")

#if quantity[0] != 0:
   #print(f"{beverage[0]}\n\t{price[0]}\tx{quantity[0]}\t{price[0] * quantity[0]}")
#if quantity[1] != 0:
    #print(f"{beverage[1]}\n\t{price[1]}\tx{quantity[1]}\t{price[1] * quantity[1]}")
#if quantity[2] != 0:
    #print(f"{beverage[2]}\n\t{price[2]}\tx{quantity[2]}\t{price[2] * quantity[2]}")

#print(f"{beverage[0]}\n\t{price[0]}\tx{quantity[0]}\t{price[0] * quantity[0]}")
#print(f"{beverage[1]}\n\t{price[1]}\tx{quantity[1]}\t{price[1] * quantity[1]}")
#print(f"{beverage[2]}\n\t{price[2]}\tx{quantity[2]}\t{price[2] * quantity[2]}")
#print(f"Your order has veen accepted. The total amount is {total_price} won.")