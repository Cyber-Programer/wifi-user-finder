import sys
from time import sleep as s

class colors:
    RESET = '\033[0m'
    YELLOW = '\033[93m'


class design:
    under= '-'*40

def animation(text,color=colors.RESET):
    for i in text:
        sys.stdout.write(color + i + colors.RESET)
        sys.stdout.flush()
        s(0.02)
    sys.stdout.write('\n')
    
text = '''
The tool attempts to identify connected devices within a network by attempting connections with their respective IP addresses.\nIt reveals active devices upon successful connections, but limitations such as security settings and offline devices may lead to incomplete or inaccurate results.\nIt offers insights into accessible devices but may not provide a comprehensive overview of all connected devices.'''

animation(text,colors.YELLOW)