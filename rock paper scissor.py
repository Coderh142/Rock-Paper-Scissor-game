import random 

print("\n\t *choose '0' for ROCK & '1' for PAPER & '2' for SCISSOR*\n")

user_points = 0
computer_point = 0


computer = random.randint(0,2)   
user = int(input("Enter your choice: ")) 


def choices():
    if (user > 2):
        print("invalide choice")
    else:
        print(f"COMPUTER:{computer}   YOU:{user}")
        
choices()   # FUNCTION

if (user == computer):
    while True:
         print ("! choose again !")
         computer = random.randint(0,2)   # this is ariginal line
         user = int(input("Enter your choice: "))
         choices()
         if (user != computer):
                 break


    
if (user == 0 and computer == 2):
            user_points =+ 1
            computer_point =+ 0
        

elif (user == 2 and computer == 0):
            user_points =+ 0
            computer_point =+ 1
          


    
elif (user == 0 and computer == 1):
            user_points =+ 0
            computer_point =+ 1
           

elif (user == 1 and computer == 0):
            user_points =+ 1
            computer_point =+ 0
            


    
elif (user == 2 and computer == 1):
            user_points =+ 1
            computer_point =+ 0
        

elif (user == 1 and computer == 2):
            user_points =+ 0
            computer_point =+ 1
            




print("\n\t\t*<<<<<<<<<<<< TOTAL MARKS >>>>>>>>>>>>>* \n")
print(f"\t\t\t  COMPUTER    YOU")
print(f"\t\t\t     {computer_point} \t       {user_points}")


if (user_points > computer_point):
    print("\n\t ~: *You are winner* :~")


else:
    print("\n\t\t\t   ~: *Computer is winner* :~")    