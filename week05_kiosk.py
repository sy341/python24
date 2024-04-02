# ISHS Cafe
# caffe latte: 2500, americano: 1500

beverage = ["Americano", "caffe latte"]
price = [1500, 2500]
total_price = 0

while True: #주문 종료 시까지 돌리는 게 키오스크.
    menu = input("1) americano  2) caffe latte  3) end order : ")
    if menu == '3':
        print ("Exit program")
        break
    elif menu == '2':
        print ("You ordered caffe latte. The price is 1500 won.")
        total_price = total_price + price[0]
    elif menu == '1':
        print("You ordered americano. The price is 2500 won.")
        total_price = total_price + price[1]
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")
print(f"Your order has veen accepted. The total amount is {total_price} won.")