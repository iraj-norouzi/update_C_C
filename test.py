fh = open ('/root/Downloads/davood_python.csv')
for i in fh.readlines():
    line = fp.readlines()
    print line
    select =  raw_input ('Yes Or no? (Y/N) ')
    
    if select=='y':
        fh2 = open('/root/Downloads/davood_python2.csv', 'a+')
        fh2.write(i)
        fh2.close()   
    else :
        continue