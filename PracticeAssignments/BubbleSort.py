# Define and use bubble sort algorithm
# Is this similar to the love_island_couples() function?

def bubble_sort(l=[2,5,1,6,3]):
    sorted_list = l
    for low_index in range(len(l)-1): # outer for loop
        for high_index in range(low_index+1, len(l)): # inner for loop
            if sorted_list[low_index] > sorted_list[high_index]: # swap
                greater_val = sorted_list[low_index] # store the greater_value
                sorted_list[low_index] = sorted_list[high_index]
                sorted_list[high_index] = greater_val
            # no need for else block
    return sorted_list

# print(bubble_sort())
print(bubble_sort([4,5,2,3,10,9,7,5,11,6]))