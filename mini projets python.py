import random

#we take range from user as input
start_range=int(input("Enter you range where you want to start= "))
end_range=int(input("Enter your ending range where you want to end= "))
print("your range in between","[",start_range,":",end_range,"]")

#after take input from user
num=random.randint(start_range,end_range)
#randemly picked number by system 
print(num, "random picked number by system ")

#first we check the number is positive or negative 
if(num>0):
    print(num, "positive number picked by system")

    #number is positive then we check number is even or odd
    if(num%2==0):
        print(num , "Even number picked by system")

    #number is postive so we check number is prime or not if number is negative
        #then we do not check prime number 
        if num %2 == 0:
    
            for i in range(2, num):
                 if (num % i) == 0:
                    print(num, "is a composite number")
                    break
            else:
                print(num, "is a prime number")
    else:
        print(num,"odd number picked by system")

    #if number  is odd then we check prime number
    if num %2 != 0:
         for i in range(3,num):
             if (num % i) == 0:
                 print(num, "is a composite number")
                 break
         else:
             print(num, "is a prime number")
        

else:
    print(num,"negative number picked by system")
    if(num%2==0):
        print(num,"Even number picked by system")
    else:
        print(num,"odd number picked by system")
            
