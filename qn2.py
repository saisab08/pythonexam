# 2 What are list,sets and dictionary how can we create them in python give example and use
# case of each (5)

#Ans:lists is an order sequnce of mutable data typesitems and its denotated by []
my_lists=['apple','bananana','cat','dog']
print(my_lists,type(my_lists))
my_lists[2]=5
print(my_lists)

#Sets:
# Ans: A set is an unordered collection of unordered items and it is immutable in nature.
s = {1,2,3,'apple'}
print(s)
print(s,type(s))
s.remove(1)
print(s)

#Dictionary:
#Ans: dictionary are the mutable data types where the key pair of the values are stored.
d={
   'name':"saisab",
   'age': 24
}
print(d,type(d))
print(d)