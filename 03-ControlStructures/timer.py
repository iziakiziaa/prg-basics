###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    print(countdown)
    countdown -= 1
    if countdown ==5:
        countdown = 'five'
    elif countdown ==4:
        countdown = 'four'
    elif countdown ==3:
        countdown = 'three'
    elif countdown ==2:
        countdown = 'tw0'
    elif countdown ==1:
        countdown = 'one'
    time.sleep(1)  # Wait for 1 second
    

print("Time's up!")
