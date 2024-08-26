# This is version 1
# Greetings Program

#greetings
#greet = input("Hello, may i know your name..")
#print("Hello ",greet, "!  thanks for choosing us.")


# this is my second version

#Greetings Program




def greet():
    pname = input("Please Enter Your Name ")
    print(f"Hello,{pname}! thanks for choosing us")
## writing a new feature for version 3
# this  is third update
def rating():
    rating = int(input("please rate from 1-5 \n please enter your input in numbers"))
    if rating > 5:
        print("we love your rating :)")
    #this is new feature of rating 
    #this is pushing into newbranch
    elif rating >2:
        print("thanks for your rating. ")
    else:
        print("we are very sorry for your experience",rating)

greet()
rating()