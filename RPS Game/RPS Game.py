import random
Choices={"R" : "Rock", "P" : "Paper" , "S" : "Scissors"}
print("  * R for Rock * P for Paper * S for Scissors * ")
User_Count=0
Ties=0
Comp_Count=0
while True:
    Usr=input("Enter Choice :").upper()
    if Usr not in Choices:
        print("Invalid Choice")
    else:
        Usrinp= Choices[Usr]
        Comp=random.choice(["R","P","S"])
        Compch=Choices[Comp]
        print("User's Choice     : ",Usrinp)
        print("Computer's Choice : ",Compch)
        if Usrinp == Compch:
            print("its a Tie")
            Ties+=1
        elif (Usrinp=="Rock" and Compch=="Scissors"):
            print("***User Won***")
            User_Count+=1
        elif (Usrinp=="Paper" and Compch=="Rock"):
            print("***User Won***")
            User_Count+=1
        elif (Usrinp=="Scissors" and Compch=="Paper"):
            print("***User Won***")
            User_Count+=1
        else:
            print("***Computer Won***")
            Comp_Count+=1
    Con=input("Do You Want To Continue\n y for Yes \t n for no :\n")
    if Con.lower() != "y":
        print(f"Your result is\n User      {User_Count} \n Computer  {Comp_Count} \n Tie       {Ties}\n")
        print("Thank You!")
        break
        
    