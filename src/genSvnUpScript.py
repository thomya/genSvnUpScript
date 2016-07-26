#!/usr/bin/python2.7

import string

print "This is little tools for getting app svn info"

f=open("../releasenote_V049.txt","r")
f1=open("svnup.sh","w")
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
        print list1
	i=0
        list1=[]
    else:
        list1.append(line.strip("\n"))
        i=i+1
f.close()
f1.close()

print "====== end ======"
