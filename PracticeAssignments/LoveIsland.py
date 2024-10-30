def love_island_couples(l):
    couples_list = []
    for i in range(len(l)-1): # i: 0 -> 2
        for k in range(i+1,len(l)):
            couples_list.append((l[i],l[k]))
    return couples_list

print(love_island_couples(["Jack", "Jane", "June", "John"]))