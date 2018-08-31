#!/usr/bin/env python
import os
import string
import re
if __name__ =="__main__":
    convertDict = dict()
    convertFile = 'result.txt' 
    fileTable = 'Bit_Map_Num_Table.txt'
    with open(fileTable,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            l_len = len(l)
            number = ""
            string_tmp = ""
            for i in range(0,l.find(" ")):
                string_tmp = string_tmp + str(l[i])
            for i in range(l.find(" ")+1,l_len):
                number = number + str(l[i])
            #convertDict[l[0]] = int(number)
            convertDict[int(number)] = string_tmp
            #print string_tmp
    print "="*30
    print "Read Table Done"
    print "Now convert!!"
    print "="*30
    #print convertDict
    #print convertDict.get(1)
    with open(convertFile,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            s , support_count = l.split(' ',2)
            if len(s) < 13:
                s = "0"*(15-len(s)) + s
            #print s
            temp = ""
            for i in range(0,len(s)):
                if s[i] == '1':
                    if temp == "":
                        temp = temp + convertDict[i+1]
                    else:
                        temp = temp + "," + convertDict[i+1]
            orgin = ""
            for i in range(0,len(temp)):
                if temp[i] != ":":
                    orgin = orgin + temp[i]

            #print "Frequent Itemset is: " + orgin + " Support Count: " + support_count + " Orignal: " + s 
            print orgin + " " + support_count
            

