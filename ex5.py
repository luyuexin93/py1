#!/usr/bin/env python
# -*-  coding:utf-8 -*-

from sys import argv

script,filename =argv

#open a file using the file() type return a file object
txt=open(filename)

print "Here's your file %r" % filename
find =txt.readline()
print find,
print txt.read()

print "Type the filename again:"

file_agin=raw_input("> ")

txt_again=open(file_agin)

print txt_again.read()

#close file after that can't read on closed file
txt.close()
