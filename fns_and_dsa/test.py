thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 
del thisdict ["brand"]
#thisdict.clear() #clear all items
print("\n",thisdict.get("model"))

print (type(thisdict))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict.items())
set = {"apple", "banana", "cherry"}