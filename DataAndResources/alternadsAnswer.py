while True:
    choice = input("Construct or Destruct? (1 or 2): ") # ask the user to destruct or construct
    if (choice != '1' and choice != '2'):
        continue # ask again
    elif (choice == '1'):
        print("Constructing an alternade...")
        while True: # prompting the user for strings until they give something valid
            str1 = input("String 1: ")
            str2 = input("String 2: ")
            if not (str1.isalpha() and str2.isalpha()):
                continue # ask for strings again
            else:
                break # from this nested while loop
        alternade = "" # start with a blank string
        for i in range(min(len(str1), len(str2))): # loop through valid indices
            alternade += str1[i]
            alternade += str2[i]
        print("Alternade:", alternade)
        break # once we have finished constructing, exit
    elif (choice == '2'):
        print("Destructing an alternade...")
        while True:
            alternade = input("Alternade: ")
            if not alternade.isalpha(): # make sure the input is valid
                continue # ask again
            else:
                break # from this nested while loop
        str1 = "" # blank string to populate
        str2 = "" # blank string to populate
        # for i in range(len(alternade)):
        #     if i % 2 == 0:
        #         str1 += alternade[i]
        #     elif i % 2:
        #         str2 += alternade[i]

        # Alternate method:

        for i in range(0,len(alternade),2): # every even index
            str1 += alternade[i]
        for i in range(1,len(alternade),2): # every odd index
            str2 += alternade[i]
        print("Word 1:", str1)
        print("Word 2:", str2)
        break # once we have finished destructing, exit
