# An influencer is a person who can influence other people's behaviour. 
# An influencer communicates with other people using social networking sites.
# Write a program that checks whether a given person is a good influencer, that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram.
# Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. 
# Sample result:

#facebook = True
#twitter = False
#instagram = True
#You are a good influencer!

facebook = input("do you have facebook? (Y/N): ")
twitter = input("do you have twitter? (Y/N): ")
instagram = input("do you have finstagram? (Y/N): ")

if facebook == 'Y' and twitter == 'Y':
    print("Spoko z cb influencer")
elif facebook == 'Y' and instagram == 'Y':
    print("Spoko z cb influencer")
elif twitter == 'Y' and instagram == 'Y':
    print("Spoko z cb influencer")
else:
    print("Chujowa jestes")