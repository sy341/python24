# ISHS Cafe
# caffe latte: 2500, americano: 1500
def select_menu(index):

# beverage = ["Americano", "Caffe latte", "Iced tea"]
# price = [1500, 2500, 2300]
beverage_price = {'Americano': 1500, 'Caffe latte': 2500, 'Iced tea': 2300}
quantity = [0, 0, 0]

total_price = 0


menu_lists = ''
for m in range(len(beverage)):
    menu_lists = menu_lists + f"{m+1} {beverage[m]} {price[m]}won "
menu_lists =  menu_lists + f"{len(beverage)+1}) end order : "
while True: #주문 종료 시까지 돌리는 게 키오스크.
    menu = input(menu_lists)
    if menu == '4':
        print ("Exit program")
        break
    elif menu == '3':
        print("You ordered", {beverage[2]},". The price is", {price[2]}, "won.")
        total_price = total_price + price[2]
        quantity[2] = quantity[2] + 1
    elif menu == '2':
        print ("You ordered", {beverage[1]},". The price is", {price[1]}, "won.")
        total_price = total_price + price[1]
        quantity[1] = quantity[1] + 1
    elif menu == '1':
        print("You ordered", {beverage[0]},". The price is", {price[0]},"won.")
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