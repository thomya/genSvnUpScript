#!/usr/bin/python2.7

import string
import sys

print "This is little tools for getting app svn info ;\n \
Usage : python genSvnUpScript sourcepath destpath "
if(len(sys.argv) < 3):
    print " pls input sourcepath & destpath ,maybe you can refer to Usage : python genSvnUpScript sourcepath destpath "
    exit(1)
sourcepath=sys.argv[1]
print sourcepath
destpath=sys.argv[2]
print destpath
f=open(sourcepath,"r")
f1=open(destpath,"w")
key="http"
i=0
list1=[]

for line in f.readlines():
    if not line.strip():
        continue
    if(line.find(key) != -1):
#        print "svn up -r" + list1[1]  + " " + list1[0]
        list1.append(line.strip("\n"))
        f1.write("svn up -r " + list1[i-1]  + " " + list1[i-2] + "\n")
#        print list1
	i=0
        list1=[]
    else:
        list1.append(line.strip("\n"))
        i=i+1
f.close()
f1.close()

print "====== end ======"
