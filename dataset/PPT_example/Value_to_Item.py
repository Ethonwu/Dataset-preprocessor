#!/usr/bin/env python
import os
import string
import re
if __name__ =="__main__":
    convertDict = dict()
    convertFile = 'Frequent_Value.txt'
    #convertFile = 'part-r-00000'
    fileTable = 'Item_Value_Table.txt'
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
#    print convertDict
    #print convertDict.get(11)
    with open(convertFile,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            s , support_count = l.split(" ",1)
            if s[0].isspace():
                continue
            l = ""
            count = ""
            for word in range(0,len(s)):
                if s[word].isspace():
                    for c in range(word+1,len(s)):
                        if s[c].isspace() is False:
                            
                            count = count + s[c]
                    break
                else:
                    l = l + s[word]
            result=[]
            result.append(map(int,l.split(',')))
            cp_l = ""
            for w in range(0,len(result[0])):
                if "," is not result[0][w]:
                    key = int(result[0][w])
                    change = convertDict.get(key)
                    #print change
                if "" is cp_l:
                    cp_l = cp_l + change 
                else:
                    cp_l = cp_l + "," +change
            print "Itemset is: " + cp_l + "  " + count + "Suopport Count is: " + support_count
