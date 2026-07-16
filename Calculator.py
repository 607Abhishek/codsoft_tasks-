def cal():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def multi(a,b):
        return a*b
    def div(a,b):
        if b == 0:
            return "Can't divide by 0"
        else:
            return a/b
    while True:
        try:
            Task=int(input(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n Enter choice : "))
        except ValueError:
            print("Please Enter from given choices")
            continue    
        if Task not in [1,2,3,4]:
            print("Wrong input")
            continue
        try:
            x=int(input("Enter 1st number : "))
            y=int(input("Enter 2nd number : "))
        except ValueError:
            print("Please Enter Valid Numbers!")
            continue
        if Task == 1:
            print(add(x,y))
        elif Task == 2:
            print(sub(x,y))
        elif Task == 3: 
            print(multi(x,y))
        elif Task == 4:
            print(div(x,y))
        ch = input("Do you want to perform another calculation?(y/n) : ")
        if ch.lower() != 'y':
            print("Thank you!")
            break
cal()