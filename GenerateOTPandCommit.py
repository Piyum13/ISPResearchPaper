from git import Repo
import random
from subprocess import call
import os
import math

def generateOTP():
    string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
    return OTP
var = generateOTP()
print ("OTP",var)
user=str(input('Enter the OTP:'))
if var==user:
    commitmessage=str(input('Enter commit message:'))
    call('git add .', shell = True)
    call('git commit -m "'+ commitmessage +'"', shell = True)
    print('Change committed successfully!')
else:
    print('Enter Correct OTP')
    
