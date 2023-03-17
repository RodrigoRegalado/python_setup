def hello():
    print("hello user")

def pack(first, second, third):
    return [first, second, third]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")


hello()
print(pack("first", "second", "third"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["sandwich", "apple", "yogurt", "chocolate"])