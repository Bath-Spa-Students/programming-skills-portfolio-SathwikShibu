
#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 10:
        print("Your ticket is free")
    elif age < 13:
        print("Your ticket is $10") 
    else:
        print("Your ticket is $15")