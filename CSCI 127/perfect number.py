##Name: Douglas Rollman
##Email: DOUGLAS.ROLLMAN07@myhunter.cuny.edu    
# Program #45: Correct the errors in the program to output the correct results.


def isPerfect(num):   
    total=0  
    for i in range(1,num):  
        if (num%i==0):  
            total=total+i  
    if(total==num):  
        return True 
    else:  
        return False 
        
def main():
    perfect_num = False
    num=int(input("Enter a perfect number: "))
    perfect_num = isPerfect(num)
    if perfect_num == True:
        print("Congratulations! ",num, " is a perfect number")
    else:   
        while perfect_num == False:
            print(num," is not a perfect number. Re-enter: ")
            num=int(input())
            perfect_num = isPerfect(num)
            if  perfect_num == True:
                break
    print("Congratulations! ",num, " is a perfect number")

if __name__ == "__main__":
    main()
