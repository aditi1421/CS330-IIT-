tempArray = []
code = [2,2,0,8,7]
lockedStatus = True

import time 
import random

def main():
    digits = [0,1,2,3,4,5,6,7,8,9]
    c = 0
    startTime = time.time()
    while 1: 
        c +=1 
        ranDigit = random.choice(digits) 
        locked = lockedStatus
        key = ranDigit
        

        if(key): 
            lenArray = len(tempArray) 
            
            if(lenArray > 5): 
                tempArray.pop(0) 
                
            tempArray.append((key)) 

            print(tempArray," Itteration: ",c) 
            
            first4Elements = tempArray[0:5] 
            
            
            if(first4Elements == code): 
                
                lastElement = tempArray[-1] 
                
                if(lastElement == 1 and locked): 
                    print("***** System UNLOCKED *****") 
                    break
               
    endTime = time.time()
    
    print("Code Found: ",tempArray[:-1]) 
    
    print("Number of guesses: ", c)
    print("Time spent: ", (endTime-startTime) * 10**3 / 1000," S ")
    
main()