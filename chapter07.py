import random

numbers = list()
for _ in range(7):
    numbers.append(random.randint(1, 6))

numbers [random.randint(1,6) for _ in range(7)]
    print(numbers)

rps = ["rock", "scissors", "paper"]
#pick = [ random.choice(rps) for _ in range(2)]
pick = []
pick.append("scissors")
pick.append("rock")
print (pick)

numbers.append(pick)
print(numbers)

numbers.append(pick)
print(numbers, numbers[7][0])

print(numbers.pop())
#print(numbers.remove(pick))
print(numbers)