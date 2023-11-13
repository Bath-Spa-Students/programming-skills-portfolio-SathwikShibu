#Exercise 4: Stages of Life :ballot_box_with_check:
'''Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
•If the person is less than 5 years old, print a message that the person is a baby.
•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•If the person is at least 4 years old but less than 15, print a message that the person is a kid.
•If the person is at least 15 years old but less than 20, print a message that the person is a teenager.
•If the person is at least 20 years old but less than 40, print a message that the person is an adult.
•If the person is age 55 or older, print a message that the person is an elder.'''

Age = 18
if Age < 5:
    print("Aww! You're still a baby.")
elif Age < 1:
    print("Hey! You're a toddler.")
elif Age < 14:
    print("Hey! You're a kid.")
elif Age < 18:
    print("Hey! You're a teenager.")
elif Age < 30:
    print("Hey! You're an adult.")
else Age < 55:
    print("Hey! You're an elder.")