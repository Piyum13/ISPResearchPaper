from git import Repo
import random
from subprocess import call
import os

otp=random.randrange(100000,1000000)
print(otp)

user=int(input('Enter the OTP:'))
if otp==user:
    commitmessage=str(input('Enter commit message:'))
    call('git add .', shell = True)
    call('git commit -m "'+ commitmessage +'"', shell = True)
    print('Change committed successfully!')
else:
    print('Enter Correct OTP')
    
