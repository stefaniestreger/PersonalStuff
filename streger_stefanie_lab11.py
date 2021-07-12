my_list = ["cat", "dog", "pig", "shark", "parrot", "rabbit"] #list of items
for x in my_list:
    print(x) #iterates over list

print('                       ') #adds a line of white space to make it look nice :)
my_list.append("bear") #adds a new item to the list
print(len(my_list))  #prints the length of the list with appended item (should be 7 count)
del my_list[2] #deletes the third item in the list (position 2) (should be "pig" that is deleted)
print(len(my_list)) #prints the length of the list with deleted item (should be 6 count)