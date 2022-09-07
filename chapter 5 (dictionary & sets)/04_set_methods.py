my_set = set()

# add()
my_set.add(4)
my_set.add(4)
my_set.add(7)
my_set.add(5)
# my_set.add([3,5,6]) # we can't add list because it's hashable (mutable , updatable)
my_set.add((3,5,6)) # we can add tuple because it's unhashable we can't update (immutable)

print(my_set)


# len() Return the number of items in a container.
print(len(my_set))

# remove() Removes the 7 from set , throws an error if 7 is not present in set
my_set.remove(7)

print(my_set)

# pop() remove any item from set
print(my_set.pop())

# clear() empty the set
my_set.clear()
print(my_set)


# properties of set
# sets are unordered 
# sets are unindexed
# cannot store duplicate values 