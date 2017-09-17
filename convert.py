#!/usr/bin/env python
import os
import string
import re
if __name__ =="__main__":
    convertDict = dict()
    convertFile = 'Output.txt'
    fileTable = 'Table.txt'
    with open(fileTable,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            l_len = len(l)
            number = ""
            for i in range(2,l_len):
                number = number + str(l[i])
            #convertDict[l[0]] = int(number)
            convertDict[int(number)] = l[0]
    print "="*30
    print "Read Table Done"
    print "Now convert!!"
    print "="*30
    print convertDict
    with open(convertFile,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            result=[]
            result.append(map(int,l.split(',')))
            cp_l = l
            for w in range(0,len(result[0])):
                if "," is not result[0][w]:
                    n = result[0][w]
                    for k in convertDict:
                        compare = int(convertDict[k])
                        if compare == n:
                            change = k
                cp_l = cp_l.replace(str(result[0][w]),change)
            print cp_l
