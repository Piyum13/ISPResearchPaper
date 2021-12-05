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
user=int(input('Enter the OTP:'))
if var==user:
    Approval=str(input('Is the Code Approved?:'))
    if Approval=='Approved':
     call('git push origin main', shell = True)
     print('Change pushed successfully!')
    if Approval!='Approved':
     print('Changes are not approved. Please connect with Approver')
else:
    print('Enter Correct OTP')
