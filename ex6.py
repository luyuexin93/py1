#!/usr/bin/env python
# -*- coding :utf-8 -*-
# ex5  file I/O


from sys import argv
#input 1 arguments filename
script,filename=argv

print "We're going to erase %r." % filename

print "If you don't want that, hit CTRL-C(^C)"
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."

#openfile and change to 'w' for write mode
target=open(filename,'w')

print "Truncationg the file.Goodbye"
#clean the file
target.truncate()

#get the user input string
print "Now I'm going to ask you for three lines."
line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

#write the strings to the file
print "I'm going to write these to the file"
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally,we close it"
target.close()
