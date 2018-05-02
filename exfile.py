from sys import argv

script,filename=argv


#""" 
# w  wirte only,if the file exists ,use this mode the file will be truncated the content The file will be created if it doesn't exist
#    when opened for writing or appending; it will be truncated when
#    opened for writing.
# r  read only , the file must exist
# a  appending mode 
# add a '+' for r/w mode ,the file must exist  
# rb+ wb+ ab+ b for binary mode 
#""" 

while True:
    print "input your choice w for write and r for read and press CTRL-C for break"
    choice=raw_input()
    if choice == 'r':
        file1=open(filename,'r+')
        print file1.read()
        file1.close()
    if choice == "w":
        file1=open(filename,'a')
        data=raw_input("please input your sentence")
        file1.write(data)
        file1.close
    print "Do you want to truncate your file make choice y/n"
    choice2=raw_input()
    if choice2=="y":
        file1=open(filename,'a+')
        file1.truncate()
        file1.close()
    if choice2=='n':
        continue
    elif choice2 not in ("y","n"):
        break
    
    
    
        
    
