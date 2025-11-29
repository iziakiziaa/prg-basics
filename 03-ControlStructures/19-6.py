#    Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. 
#    Write a program that prints a survey consisting of three questions.
#    Save the answers to logical type variables. 
#    Then view the survey result. Sample result:

#  SURVEY Are you interested in computer science? (y/n): y
#  Do you like playing computer games? (y/n): n
#  Do you have an Instagram account? (y/n): y

# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes


survey = input("SURVEY!!!!! Are you interested in computer science? (y/n): ")
computer = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you have an Instagram account? (y/n): ")

if survey == 'y':
    survey = 'yes'
elif survey == 'n':
    survey = 'no'
else:
    print("Invalid answer")

if computer == 'y':
    computer = 'yes'
elif computer == 'n':
    computer = 'no'
else:
    print("Invalid answer")

if instagram == 'y':
    instagram = 'yes'
elif instagram == 'n':
    instagram = 'no'
else:
    print("Invalid answer")

print("SURVEY RESULT!!!!")
print(f'Are you interested in computer science: {survey}')
print(f'Do you like playing computer games?: {computer}')
print(f'Do you have an instagram account?: {instagram}')