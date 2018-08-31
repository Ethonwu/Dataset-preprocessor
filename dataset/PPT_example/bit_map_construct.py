#!/usr/bin/env python
from optparse import OptionParser
import os
import sys
import numpy as np
import csv
def ReadFile(filename):
    Table = dict()
    i = 1
    with open(filename,'r') as f:
        for line in f.readlines():
            l = line.strip('\n')
            for item in l.split(','):
                if item not in Table:
                    Table[item] = i
                    i = i + 1
    #for key, value in sorted(Table.iteritems(), key=lambda (k,v): (v,k)):
     #   print "%s: %s" % (key, value)
    return Table
def BitMapInit(filename,Tables,OutputFile):
    getFileLines = len(open(filename).readlines())
    getTablesElements = len(Tables.keys())
    x , y = getTablesElements , getFileLines
    BitMap = np.full((y,x),0,dtype='i')
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
                     key = Tables[str(tmp_l[0][Items])]
                     BitMap[y_line,key-1] = 1
            y_line = y_line + 1
    #print BitMap
    f = open(OutputFile,'a+')
    np.savetxt(f,BitMap,fmt="%d")
if __name__ == "__main__":
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>"+"-t <input T_Table>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    optparser.add_option('-o','--output',dest='output',help='Output filename',default='BitMap.txt')
    (options, args) = optparser.parse_args()
    if options.input is None:
        print sys.usage
        sys.exit()
    elif options.input is not None:
        inputFile = options.input
        exportFile = options.output
    if os.path.exists(exportFile):
        print "Here already have file"
        sys.exit()
    TableInfo = dict()
    TableInfo = ReadFile(inputFile)
    #print TableInfo
#    d = open('BitMap_Table.txt','a+')
    for key, value in sorted(TableInfo.iteritems(), key=lambda (k,v): (v,k)):
         print "%s: %s" % (key, value)
         #d.write(key + str(value) + '\n')
         #d.close()
    BitMapInit(inputFile,TableInfo,exportFile)
