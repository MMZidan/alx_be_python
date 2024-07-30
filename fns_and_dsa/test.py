thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 
del thisdict ["brand"]
#thisdict.clear() #clear all items
print("\n",thisdict.get("model"))
print(thisdict.items())
print (type(thisdict))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()

set = {"apple", "banana", "cherry"}