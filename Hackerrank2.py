#Given an integer, , perform the following conditional actions:
#if  is odd, print Weird
#f  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Input Format



def number(no):
    if not no%2 == 0:
        print("Weird")
    else:
        if no>=2 and no<=5:
            print("not weird")
        elif no>=6 and no<=20:
            print("weird")
        elif no>20:
            print("not weird")
            
no = int(input("enter the number: "))

number(no)





        



    
    

        


    







