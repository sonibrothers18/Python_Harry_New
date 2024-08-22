marks = {41, 5, 26, 89, 5, 5, "harry"}

marks.add(True) # add element in the set
print(marks)

print(len(marks)) # don't count duplicate values

marks.remove(5) # Updates the set 'marks' and removes 5 from 'marks'
marks.pop() # Removes an arbitrary(random) element from the set and return the element removed
marks.clear() #empties the set
marks.union({8,11}) # Returns a new set with all items from both sets. {1,8,2,3,11}.
marks.intersection({8,11}) # Return a set which contains only item in both sets {8}.