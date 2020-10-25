#Nathan Pang
#108660184
#25/09/2020
#optional requirements: version and supporting both Windows and Unix Style command line args

import sys
import urllib3
import re
http = urllib3.PoolManager()
from colorama import init, Fore
init(convert=True)

regex = 'https?:\/\/[=a-zA-Z0-9\_\/\?\&\.\-]+'

x = 0
if len(sys.argv) == 1:
    print(Fore.RED + "No arguments, please enter either -file (filename), -url (link), or -v"+ Fore.RESET)
    print(Fore.RED + "Windows and Unix style commands also work, --v, /v, etc"+ Fore.RESET)

elif len(sys.argv) == 3 or len(sys.argv) == 4:

    g = 0
    if (len(sys.argv) == 4):
        if (sys.argv[3]) == "--good":
            g = 1
        elif (sys.argv[3]) == "--bad":
            g = 2

    if(sys.argv[1] == "-file" or sys.argv[1] == "--file" or sys.argv[1] == "/file"):
        print("File Checker")
        try:
            with open(sys.argv[2], 'r') as f:
                lines = [line.rstrip('\n') for line in f.readlines()]

            for line in lines:

                #Using regex to find urls then slicing off the first and last 2 characters to only display URL
                if ('http://' in line or 'https://' in line):
                    if(g == 0 or g == 1):
                        print(Fore.GREEN + str(re.findall(r'https?://[^\s<>"].[^\s<>"]+', line))[2:-2] + " is a valid link" + Fore.RESET)
                elif ('www.' in line and '://' not in line):
                  
                    if(g == 0 or g == 2):
                        print(Fore.RED + str(re.findall(r'www.[^\s<>"].[^\s<>"]+', line))[2:-2] + " is not a valid link" + Fore.RESET)
                        x = 1
                else:
                    if ("<" and ">" in line): #covers situation involving urls within html tags with misspelled http/https
                        if(g == 0 or g == 2):
                            print(Fore.RED + str(re.findall(r'>(.*?)<', line))[2:-2] + " is not a valid link" + Fore.RESET)
                            x = 1
                    else:
                        if(g == 0 or g == 2):
                            print(Fore.RED + line + " is not a valid link" + Fore.RESET)
                            x = 1
        except:
            print(Fore.RED + "Sorry, file not found" + Fore.RESET)
            x = 1
          
    elif(sys.argv[1] == "-url" or sys.argv[1] == "--url" or sys.argv[1] == "/url"):
        print("URL Checker")
        try:
            response = http.request('HEAD', sys.argv[2])
            if response.status == 200:
                print(sys.argv[2], ": good")
            elif response.status == 400 or response == 404:
                print(sys.argv[2], ": bad")
                x = 1
            else:
                print(sys.argv[2], ": unknown")
                x = 1
        except:
             print(Fore.RED + "Sorry, the link is broken, please fix it and try again!" + Fore.RESET)
             x = 1

    if(sys.argv[1] == "-ignore" or sys.argv[1] == "--ignore" or sys.argv[1] == "/ignore"):
        print("File Ignore")
        ignoreURLs = []
        try:
            with open(sys.argv[2], 'r') as fi:
                lines = [line.rstrip('\n') for line in fi.readlines()]
            for line in lines:
                if line[0] == '#':
                    pass
                #Using regex to find urls then slicing off the first and last 2 characters to only display URL
                elif ('http://' in line or 'https://' in line):
                    if(g == 0 or g == 1):
                        str = re.findall('https?://[^\s<>"].[^\s<>"]+', line)
                        ignoreURLs += str       
        except:
            print(Fore.RED + "Sorry, file not found" + Fore.RESET)
            x = 1
        try:
            with open(sys.argv[3], 'r') as f:
                #find urls in test.txt
                lines = re.findall(regex, f.read())
            #find all to be ignored urls
            tobeIgnored = [j for i in ignoreURLs for j in lines if i in j or j in i]
            
            #find all not ignored urls
            notIgnored = [x for x in lines if x not in tobeIgnored]
            for ni in notIgnored:
                print(Fore.GREEN + ni + " is a valid link" + Fore.RESET)
        except:
            print(Fore.RED + "Sorry, file not found" + Fore.RESET)
            x = 1

#Version Option                  
elif(sys.argv[1] == "-v" or sys.argv[1] == "--v" or sys.argv[1] == "/v"):
    print("This is version 0.3 of the PYLinkChecker")
    
elif len(sys.argv) == 2:
    print(Fore.RED + "Not enough entered, please enter the name of a file or a url" + Fore.RESET)
    x = 1

if(x == 1):
    sys.exit(1)
else:
    sys.exit(0)