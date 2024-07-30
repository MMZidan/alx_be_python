name=input("Please Enter your name: ").lower()
length=int(input("Please length of rectangle: "))
width=int(input("Please width of rectangle: "))

def get_name(name):
    print(f"Hello {name.capitalize()}!")

def area_rec(length,width):
    area_rec=length*width
    x= length%2
    if (x!=0):
        print("Length is Odd")
    else:
        print("Length is Even")
    return area_rec

get_name(name)

print(area_rec(length,width))
