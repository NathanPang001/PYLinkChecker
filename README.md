# PYLinkChecker

Hello, this is PYLinkChecker, a tool coded in python designed to check the validity of links by either enter the name of a file or by entering a url.

To use this tool, you need to install python, and urllib3 (https://pypi.org/project/urllib3/).

This tool checks if the links in the file contains http:// or https:// and determines if they are valid through that check.
It checks if URL's are valid by sending a request to the url and using the response sent from the website, a status of 200 means that it is considered good, a status of 400/404 means that it is considered bad, and any other status means that it is considered unknown.

The optional requirements are that this tool has an option for version and it supports both Windows and Unix Style command line arguments

The commands are:

-file (filename) / --file (filename) / /file (filename)

-url (link) / --url (link) / /url (link)

-v / --v / /v

An example of running this code is:
"PYLinkChecker.py -file test.txt"
and the output is shown in the file PYTest-File.jpg
