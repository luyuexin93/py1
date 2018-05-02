#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import argv
from os.path import exists

#need user input two arguments
script ,from_file,to_file=argv

print "Copying from %s to %s" % (from_file,to_file)

#we could do these two on one line too,how?
indata=open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

#if outfile not exist system will auto create a new file
output=open(to_file,'w')
#copy input file content to the output file  
output.write(indata)

print "Alright,all done."
#close Sets data attribute .closed to True.  A closed file cannot be used for
#further I/O operations.  close() may be called more than once without error. 
# Some kinds of file objects (for example, opened by popen())
#may return an exit status upon closing.
#
output.close()
open(from_file).close()

