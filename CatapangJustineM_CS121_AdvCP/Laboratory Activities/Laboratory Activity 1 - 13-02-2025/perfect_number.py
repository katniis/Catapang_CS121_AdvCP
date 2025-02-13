number = int(input("Enter a number: "))
divosor_sum = 0
for i in range(1, number):
    if number % i == 0:
        divosor_sum += i
if divosor_sum == number:
    print(f"{number} is a perfect number")
else: 
    print(f"{number} is not a perfect number")
