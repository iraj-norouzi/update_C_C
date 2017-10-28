import subprocess
import time
import datetime
key = 'test'
t = str(datetime.datetime.now())
########################################################
###########Main function################################
########################################################
def start():
    subprocess.call('clear')
    select = raw_input('Will an update be done?(Y/N) : ')
    time.sleep(1)
    if select == "y" or select == "Y":
        print('Wellcom to update IBSng Date is ' + t )
        print('Start to Update! ')
        execute()
    else:
        print ('Exited !')
        exit()
#########################################################
def execute():
    subprocess.call('clear')
    fh = open("/var/log/tools/ibs_install.log", "a+")
    update_IBSng_file = 'Update IBSng:\n'
    fh.write('Update IBSng:\n')
    fh.close()
    sel = raw_input('Are You Sure To Update IBSng ?[ Y/N ] : ')
    time.sleep(1)
    if sel == 'y' or sel == 'Y':
        fh = subprocess.call('echo 2 > /usr/local/IBSng/LAST_TAG',shell=True)
        fh = open("/etc/default/IBSng")
        key = fh.read()[0:-1]
        if  keys(key):
            print('Start Update IBSng With Out Usb')
            fh = open("/var/log/tools/ibs_install.log", "a+")
            fh.write(" start Update IBSng With Out Usb " + t)
            fh.close()
            print('START UPDATE NOW ! ')
            subprocess.call('install_ibs --no-usb',shell=True)
        update()
        else:
            print('Start Update IBSng With Out Usb')
            fh = open("/var/log/tools/ibs_install.log" , "a+")
            fh.write(" start Update IBSng With  Usb" + t)
            fh.close()
        print('START UPDATE NOW ! ')
        time.sleep(2)
        subprocess.call('install_ibs ',shell=True)
        update()
    elif sel == 'n' or sel == 'N':
        print('exir to update  ')
        exit()
#######################################################
#############software or hardware key##################
#######################################################
def keys(key):
    if key == "#starter_args= usb":
        print('your key is a Software ! ')
        time.sleep(1)
        return True
    elif key == "starter_args=' usb'":
        print('your key is a Hardware ! ')
        time.sleep(1)
        return False
    else:
        print('please check /etc/default/IBSng file content!!!!!')
        exit()
###############################################################
def update():
    subprocess.call('cp -rp /usr/local/IBSng /usr/local/IBSng-old2',shell=True)
    subprocess.call('cp -rp /usr/local/src /usr/local/src-old',shell=True)
    subprocess.call('ibs_backup_custom',shell=True)
    print('Press Any Key ...')
    fh = open("dependensi.sh","w+")
    fh.write('#!/bin/bash\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.33_upgrade.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.34_upgrade.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.35_upgrade.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.36_upgrade.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/defs.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/table.sql\n')
    fh.write('psql -U ibs IBSng < /usr/local/IBSng/db/function.sql\n')
    fh.write('python /usr/local/IBSng/scripts/python_dependency_setup.py install\n')
    fh.close()
    subprocess.call('chmod 777 dependensi.sh',shell=True)
    subprocess.call('bash dependensi.sh',shell=True)
    subprocess.call('python /usr/local/IBSng/scripts/python_dependency_setup.py install',shell=True)
    subprocess.call('/etc/init.d/IBSng restart',shell=True)
    ##################################################################
start()
