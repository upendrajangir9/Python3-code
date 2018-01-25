"""import sys
sys.setrecursionlimit(2500)
"""


import math


def prime(num):

    def check(num):
    
        if prime.i < 0 :
        
            return True
        
        elif num % prime.l[-prime.i] == 0 :
        
            return False
        
        else :
        
            prime.i -= 1
            return check(num)
    
    if num <= 1 :
        
        return False
    
    elif num <= 3:
        
        return True
    
    else :
        
        prime.l = list(range(2,int(math.sqrt(num)+1)))
        prime.i = len(prime.l)
        return check(num)

def prime_range(start,end):

    prime_range.l = list(range(start,end+1))
    prime_range.i = len(prime_range.l)-1
    
    def chk_range():
   
        if prime_range.i < 0 :

            print("\n\nThanks for using This Program \n\n")

        else :

            no = prime(prime_range.l[-prime_range.i])
    
            if no :

                print(prime_range.l[-prime_range.i],end='     ')
                prime_range.i -= 1
                chk_range()

            else :
                
                prime_range.i -= 1
                chk_range()
        
    chk_range()





def main():

    print("\nPRIME NO".center(100,'*'))
    ch = int(input("\nChoice\n1.Check Prime No\n2.Print Prime Numbers in Range\nyour choice - "))
    
    if ch == 1 :

        num = int(input("\nEnter a no. - "))
        
        if prime(num) :
            
            print("\nGiven no. %s is Prime"%(num))
        
        else :
            
            print("\nGiven no. %s is Not Prime "%(num))
    
    elif ch == 2 :

        start = int(input("\nInput Starting Point - "))
        end = int(input("\nInput Ending Point - "))
        prime_range(start,end)
    
    else :

        print("\n\nWrong Input Try Again \n\n")

    if  input("\n\nPress any Key to continue - "):
       
        main()
        

if __name__ == "__main__" :
        
    main()

