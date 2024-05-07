number = int(input("Input number : "))

#number: prime number, 1과 자기 자신만을 약수로 가짐.
#1이 아닌 다른 수를 약수로 가질 수 없음.
count = 0
#for i in range(1, number+1):
for i in range(2, number+1):
    if number % i == 0:
        count += 1

if count == 0:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")