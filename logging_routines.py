'''
This script contains the logging functions (to be expanded on)
'''

from datetime import datetime

def log(string, newLine):
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    string = '[{}] {}'.format(currentTime, string)
    
    if not newLine:
        print(string, end='')
    else:
        print(string)