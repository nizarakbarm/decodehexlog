#!/usr/bin/python2
### Developed by Nizar Akbar Meilani ###
### Simple utility script for parsing logs ###
#### Decode all hex from log and replace hex string in apache log with it's plain string form ####
#### You can use this script or develop this script in your project, but please respect me too by mention my name :v ####
import sys
import re
from binascii import unhexlify
for line in sys.stdin:
    decoded=[]
    linex=""
    m=re.findall(r'0x([0-9a-f]+)',line)
    if m:
       for i in m:
           if len(i)%2 is not 0:
               i="{}0".format(i)
           txt=unhexlify(i)
           #decoded.append(txt)
           #print '{}={}'.format(i,txt)
           linex=re.sub('0x{}'.format(i),txt,line)
           #print linex
           line=linex
       #print decoded
       #line="{} hex decoded:{}".format(line,decoded)
       print linex
       #print line
       #print "{} [hex decoded]".format(line)


