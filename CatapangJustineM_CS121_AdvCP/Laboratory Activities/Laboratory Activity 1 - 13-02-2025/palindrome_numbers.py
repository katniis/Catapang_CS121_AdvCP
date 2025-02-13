number = int(input("Enter a number: "))

reversed_num = str(number)[::-1]
if number == int(reversed_num):
    print("Palindrome")
else: 
    print("Not a Palindrome")