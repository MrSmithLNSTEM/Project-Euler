with open("13.txt","r") as file:
    lines = file.read().splitlines()

sum = 0
for i in lines:
    sum += int(i)
print(i)

#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
newSum = str(sum)[:10]
print(newSum)