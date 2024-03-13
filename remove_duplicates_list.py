def unique(item_list=[]):
    update_list=[]
    for item in item_list:
        if item not in update_list:
            update_list.append(item)
    return update_list

print(unique([1,1,4,5,1]))
print(unique(['Suresh','Ramesh','Jayesh','Suresh']))

            
        