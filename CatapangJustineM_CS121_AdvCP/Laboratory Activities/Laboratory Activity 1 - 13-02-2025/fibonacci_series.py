terms = int(input("Enter the number of terms: "))
print("Fibonacci Series: ", end="")
n1 , n2 = 0, 1
for i in range(terms):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2