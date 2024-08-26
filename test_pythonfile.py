# This is version 1
# Greetings Program

#greetings
#greet = input("Hello, may i know your name..")
#print("Hello ",greet, "!  thanks for choosing us.")


# this is my second version

#Greetings Program






# here i made little changes @some_0_n_e
def greet_n_rate():
    def greet():
        pname = input("Please Enter Your Name ")
        print(f"Hello,{pname}! thanks for choosing us")
        
    def rating():
        rating = int(input("please rate from 1-5 \n please enter your input in numbers"))
        if rating > 5:
            print("Invalid rating. Please rate between 1-5.")
        else:
            print(f"Thanks for rating us {rating}!")
#ADDING A SMILE FACE            
    
            
    greet()
    rating()
    print("   ** -- **   ")

greet_n_rate()