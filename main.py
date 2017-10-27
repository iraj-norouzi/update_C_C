#!/usr/bin/python3.6
# -*- coding: utf-8
import subprocess
import time
key =  subprocess.check_output('cat /etc/default/IBSng',shell = True)
#print (key)
key = key.split()
#print(key)
def start():
    select = raw_input('Will an update be done?(Y/N) : ')
    if select == 'y' or select == 'Y':
        print('Start to Update! ')
        time.sleep(2)
        keys(key)
    else:
        print('Exited !')
        exit()
def keys(key):
    if key[0] == 'hardware':
        print('your key is a Software ! ')
        return True
    else:
        print('your key is a Hardware ! ')
        return False
start()
