import socket
import random
import sys
import os
import compileall
#colors
#RED     = '\033
#GREEN   = '\033[32m'
#YELLOW  = '\033[33m'
#BLUE    = '\033[34m'
print('''
____  ___
\   \/  /
 \     / 
 /     \ 
/___/\  \
      \_/

[1] get host URL
[2] soon
[00] abut
''')
 
 
 
chinput = input('select number :')

if chinput =='1':
  print('ENTER YOUR DNS')
  hostname = input()
  ip=socket.gethostbyname(hostname)
  print('HOST NAME IS :' ,hostname, 'TARGET IP IS' ,ip)
  

         
if chinput == '2':
  name = input ("Name is file :")
  compileall.compile_dir(name)
  print('encrypt file :' +name)
  
  
  
  
  
         
         
         
         
         

 
 
           
         
         
         