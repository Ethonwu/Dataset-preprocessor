#!/usr/bin/env python
import sys
import string
import re
import os
from optparse import OptionParser
def AnalyseInputFile(inputFile,pro_symbol):
    Convert_list = dict()
    i = 1
    with open(inputFile,'r') as f:
        for line in f.readlines():
            s = line.strip('\n')
            l = s.replace(pro_symbol,",")
            cp_l = l
            for w in l:
                if "," is not w:
                    if w not in Convert_list:
                        Convert_list[w] = i
                        i = i + 1
                    cp_l = cp_l.replace(w,str(Convert_list[w]))            
            OutputFile(cp_l)
    return Convert_list
def OutputFile(Data):
    f = open(filename, 'a+')
    f.write(Data)
    f.write('\n')
    f.close()
def CheckBetweenValue(Datasetfile):
    symbol_list = dict()
    check = 0
    with open(Datasetfile,'r') as f:
        for line in f.readlines():
            if ' ' in line:
                if check == 0:
                    print "====================="
                    print "File have space value"
                    print "====================="
                    check = 1
                #finish_string = str(pre_string).split()
                #value = 1
                s = ' '
                symbol_list[s] = 1
            for pun in string.punctuation:
                if pun in line:
                    if check == 0:
                        print "======================"
                        print "File have symbol value"
                        print "======================"
                        check = 1
                    symbol_list[pun] = 1
    if len(symbol_list) > 1:
        print "File input error please check input file!!"
        sys.exit()
    symbol = symbol_list.keys()[0]
    return symbol
if __name__ =="__main__":
    get_Table = dict()
    global filename
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>"+"-o <output covert dataset path>"+"-O <output convert dataset to HDFS>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    optparser.add_option('-o','--output',dest='output',help='Output filename',default='Output.txt')
    optparser.add_option('-D','--outputHDFS',dest='output',help='Output filename',default='Output.txt')
    (options, args) = optparser.parse_args()
    if options.input is None:
        print sys.usage
        sys.exit()
    elif options.input is not None:
        inFile = options.input
    else:
        print options.usage
        sys.exit('Bye bye see you baby <3')
    filename = options.output
    dictfile = 'Table.txt'
    if os.path.exists(filename) or os.path.exists(dictfile):
        print "Here already have file"
        sys.exit()
    print "Now do pre process from file.........."
    get_symbol = CheckBetweenValue(inFile)
    get_Table = AnalyseInputFile(inFile,get_symbol)
    d = open(dictfile,'a+')
    print "Your dataset list table is:"
    for key, value in sorted(get_Table.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)
        d.write(key + " " + str(value) + '\n')
    d.close()
    print "Convert Successfully!!!"
