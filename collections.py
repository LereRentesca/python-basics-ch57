#Python Collections
#1. Lists- They are used to store multiple items in a single variable 
#and they use square brackets []
# Properties: lists are ordered, changeable and allow duplicates.

empty_list = [] #this is an empty list
thisisalist = ["apple","banana","cherry","orange", "banana"] #this is a list with values by default
#                0        1        2        3        4
print(f"Empty List: {empty_list} | Type: {type(empty_list)}")
print(f"List: {thisisalist} | Type: {type(thisisalist)}")
# thisisalist.insert(0,"watermelon")
# print(f"List Changing Order: {thisisalist} | Type: {type(thisisalist)}")
print(f"List Length: {len(thisisalist)}")
print(f"Accesing ELements: {thisisalist[0]}")
print(f"Accesing Elements by Negative Indexing: {thisisalist[-1]}")
print(f"Accesing Elements by Ranges [n:n]: {thisisalist[1:3]}")
print(f"Accesing Elements by Ranges [:n]: {thisisalist[:2]}")
print(f"Accesing Elements by Ranges [n:]: {thisisalist[2:]}") 

#Adding elements to the list
thisisalist.append("watermelon")
thisisalist.append("stawberry")
print(f"List: {thisisalist} | Type: {type(thisisalist)}")
#Remove elements from the list
thisisalist.remove("banana")
thisisalist.pop(0)
thisisalist.pop()
print(f"List: {thisisalist} | Type: {type(thisisalist)}")
thisisalist[0] = "blackberry"
print(f"List: {thisisalist} | Type: {type(thisisalist)}")


#Dictionary
#Are used to store data values in key:value pairs.
#Properties: ordered, changeable and do not allow duplicates
thisisadict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964,
    "colors" : ["red","white","blue","black"]
}
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
print(f"Accesing items using keys: {thisisadict['colors']}")
print(f"Dictionary Lenght: {len(thisisadict)}")
print(f"Accesing items using get: {thisisadict.get('year')}")
print(f"Only print the keys: {thisisadict.keys()}")
print(f"Only print the values: {thisisadict.values()}")

# thisisadict["type"] = "SUV"
# print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
thisisadict.update({"year":2024})
thisisadict.update({"type":"SUV"})
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
thisisadict.pop("colors")
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")


# In your free time: Search about tuples and sets