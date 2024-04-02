# IHSH Cafe
# caffe latte: 2500, americano: 1500

beverage = ["Americano", "caffe latte"]
price = [1500, 2500]

while True: #주문 종료 시까지 돌리는 게 키오스크.
    menu = int(input("1) americano  2) caffe latte  3) end order : "))
    if menu == 3:
        print ("Exit program")
        break
    elif menu == 2:
        print ("You ordered caffe latte. The price is 1500 won.")
    elif menu == 1:
        print("You ordered americano. The price is 2500 won.")