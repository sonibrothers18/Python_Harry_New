# Store the multiplication tables generated in question 64 in a file named Tables.txt.

n = int(input("Enter your number: "))

table = [n*i for i in range(1, 11)]
with open("067.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")