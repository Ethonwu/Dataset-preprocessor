#!/usr/bin/env python
from optparse import OptionParser
import os
import sys
import numpy as np
import csv
def GetDictionery(filetable):
    convertDict = dict()
    convertFile = 'Output.txt'
    #convertFile = 'part-r-00000'
    fileTable = 'Table.txt'
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
    print "="*30
    print "Read Table Done"
    print "Now convert!!"
    print "="*30
    #print convertDict
    return convertDict
def BitMapInit(filename,Tables,OutputFile):
    getFileLines = len(open(filename).readlines())
    getTablesElements = len(Tables.keys())
    x , y = getTablesElements , getFileLines
    BitMap = np.full((y,x),0,dtype='i')
    BitMap[0,3] = 9
    #print BitMap
    y_line = 0
    with open(filename,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            if l[0].isspace():
                continue
            tmp_l = []
            tmp_l.append(map(int,(l.split(','))))
            for Items in range(0,len(tmp_l[0])):
                 if "," is not tmp_l[0][Items]:
                     key = int(tmp_l[0][Items])
                     BitMap[y_line,key-1] = 1
            y_line = y_line + 1
    print BitMap
    f = open(OutputFile,'a+')
    np.savetxt(f,BitMap,fmt="%d")
if __name__ == "__main__":
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>"+"-t <input T_Table>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    optparser.add_option('-t', '--inputTableFile',dest='table',help='filename',default=None)
    optparser.add_option('-o','--output',dest='output',help='Output filename',default='BitMap.txt')
    (options, args) = optparser.parse_args()
    if options.input and options.table is None:
        print sys.usage
        sys.exit()
    elif options.input and options.table is not None:
        inputFile = options.input
        table = options.table
        exportFile = options.output
    if os.path.exists(exportFile):
        print "Here already have file"
        sys.exit()
    TableInfo = dict()
    TableInfo = GetDictionery(table)
    BitMapInit(inputFile,TableInfo,exportFile)
