# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.

# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.


def song_ninetynine(n = 99, drink = "beer"):
    # deal with plurals
    for i in range(n,2,-1): # 99 - 3
        print(f"{i} bottles of {drink} on the wall, {i} bottles of {drink}.\nTake one down and pass it around, {i-1} bottles of {drink} on the wall.\n")
    print(f"2 bottles of {drink} on the wall, 2 bottles of {drink}.\nTake one down and pass it around, 1 bottle of {drink} on the wall.\n")
    print(f"1 bottle of {drink} on the wall, 1 bottle of {drink}.\nTake one down and pass it around, no more bottles of {drink} on the wall.\n")
    print(f"No more bottles of {drink} on the wall, no more bottles of {drink}.\nGo to the store and buy some more, {n} bottles of {drink} on the wall.")

# invoking the function
# song_ninetynine() # exact lyrics of the original song
song_ninetynine(n=50, drink = "Pepsi")