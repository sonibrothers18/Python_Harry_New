
# ! Strings are immutable (can't change)

a = 'mayur'
b = "mayur"
c = '''mayur'''

print("Value at index 1 of 'a' is",a[1])

split = a[1:3] # split string 'a' from index 1 to index 2
print(split)

d = "abcdefghijklmnopqrstuvwxyz"
split_2 = d[1::4] # split string 'd' from index 1 to index last and access every 4th element
print(split_2)