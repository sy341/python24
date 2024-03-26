# def square(n) -> int
   #return n*n

number = int(input())

#for i in range(number+1):
#    print (square(i))

#temp = list()
#for i in range (number+1):
#    temp.append(i)

temp = [i for i in range(number+1)]  # list comprehension
print(list(map(lambda i: i*i, temp)))
print(list(map(sqaure, temp)))