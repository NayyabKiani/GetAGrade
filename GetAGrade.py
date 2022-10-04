print("Today we will find out what grade you got on your exam!")
answer = input("Do you want to continue? ")
if answer == 'no' :
    print("You have now exited the program!")
    quit
elif answer == 'yes':
    Mark = int(input("Enter your mark: "))
if Mark < 40:
    print("You got an F!!!")
elif Mark >=40 and Mark <50:
    print("You got a D!!!")
elif Mark >=50 and Mark <60:
    print("You got a C!!!")
elif Mark >=60 and Mark <70:
    print("You got a B!!!")
else:
    print("You got an A")