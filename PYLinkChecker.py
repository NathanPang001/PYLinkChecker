#Nathan Pang
#108660184
#25/09/2020
#optional requirements: version and supporting both Windows and Unix Style command line args

import sys
import argparse
import urllib3
#import requests

http = urllib3.PoolManager()
from colorama import init, Fore
init(convert=True)
#Checking for number of arguments with if/elif
if len(sys.argv) == 1:
    print(Fore.RED + "No arguments, please enter either -file (filename), -url (link), or -v"+ Fore.RESET)
    print(Fore.RED + "Windows and Unix style commands also work, --v, /v, etc"+ Fore.RESET)

elif len(sys.argv) == 3:

    
    
    #File Checker
    if(sys.argv[1] == "-file" or sys.argv[1] == "--file" or sys.argv[1] == "/file"):
        print("File Checker")
        try:
            with open(sys.argv[2], 'r') as f:
                lines = [line.rstrip('\n') for line in f.readlines()]

                for line in lines:
                    if ('http://' in line or 'https://' in line):
                        print (line , Fore.GREEN +  "is a valid link" + Fore.RESET)
                    else:
                        print (line, Fore.RED + "is not a valid link" + Fore.RESET)
        except:
            print(Fore.RED + "Sorry, file not found" + Fore.RESET)
        
     #URL Checker   
    elif(sys.argv[1] == "-url" or sys.argv[1] == "--url" or sys.argv[1] == "/url"):
        print("URL Checker")
        try:
            #testing with requests
            #response = requests.get(sys.argv[2])
            
            #with urllib3
            response = http.request('HEAD', sys.argv[2])
            if response.status == 200:
                print(sys.argv[2], ": good")
            elif response.status == 400 or response == 404:
                print(sys.argv[2], ": bad")
            else:
                print(sys.argv[2], ": unknown")
        except:
             print(Fore.RED + "Sorry, the link is broken, please fix it and try again!" + Fore.RESET)

#Version Option                  
elif(sys.argv[1] == "-v" or sys.argv[1] == "--v" or sys.argv[1] == "/v"):
    print("This is version 0.1 of the PYLinkChecker")
    
elif len(sys.argv) == 2:
    print(Fore.RED + "Not enough entered, please enter the name of a file or a url" + Fore.RESET)

print("END")  
