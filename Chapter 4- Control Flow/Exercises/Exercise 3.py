#Exercise 3: Alien Colors #3 :ballot_box_with_check:
'''Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
•	 If the alien is red, print a message that the player earned 15 points.
•	 If the alien is blue, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 20 points.
•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_color = "Red"
if alien_color == "Red":
    print("You have earned 15 points!")
elif alien_color == "Blue":
    print("You have earned 10 points!")
else:
    print("You have earned 20 points!")