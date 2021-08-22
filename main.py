import subprocess
import json
import sys

name=input("Enter Your Name: ")

import requests

if len(name)==0:
    print('Please Enter Your Name!')
    
else:
    api=requests.get('https://api.genderize.io/?name='+name).content
    out=json.loads(api)
    if out['gender'] == 'male':
        print('You Are A Male!')
        print('\nPlease Upvote(+1) This Code.\nAlso Subscribe Me on Youtube: S Codez')
        
    elif out['gender'] == 'female':
        print('You Are A Female!')
        print('\nPlease Upvote(+1) This Code.\nAlso Subscribe Me on Youtube: S Codez')
    
    else:
        print('Sorry, Failed to Detect!')
