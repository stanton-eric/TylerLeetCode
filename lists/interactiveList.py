prompt = "enter items into the list (hit enter when done): "
item = input(prompt)
my_list = []
while item != "":
    my_list.append(item)
    item = input("next item (enter when done): ")
print(my_list)
