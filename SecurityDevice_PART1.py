tempArray = []
code = [2, 2, 0, 8, 7]
locked = True

while 1:
    if (locked):
        print("SYSTEM STATUS: Locked")
    else:
        print("SYSTEM STATUS: Unlocked")

    print("Enter the code (one digit at a time)")
    key = input()

    if (key.isdigit()):
        lenArray = len(tempArray)

        if (lenArray > 5):
            tempArray.pop(0)

        tempArray.append(int(key[0]))
        first4Elements = tempArray[0:5]

        if (first4Elements == code):

            lastElement = tempArray[-1]

            if (lastElement == 1 and locked):
                print("***** System UNLOCKED *****")
                locked = False
            elif (lastElement == 4 and not locked):
                print("***** System LOCKED *****")
                locked = True