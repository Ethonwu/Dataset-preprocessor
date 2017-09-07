#!/usr/bin/env python
import sys
import string
import re
from optparse import OptionParser
def AnalyseInputFile(inputFile,pro_symbol):
    Convert_list = dict()
    i = 1
    with open(inputFile,'r') as f:
        for line in f.readlines():
            s = line.strip('\n')
            l = s.replace(pro_symbol," ")
            cp_l = l
            for w in l:
                if ' ' is not w:
                    if w not in Convert_list:
                        Convert_list[w] = i
                        i = i + 1
                    cp_l = cp_l.replace(w,str(Convert_list[w]))            
            OutputFile(cp_l)
    return Convert_list
def OutputFile(Data):
    f = open('Output.txt', 'a+')
    f.write(Data)
    f.write('\n')
    f.close()
    print Data

def CheckBetweenValue(Datasetfile):
    symbol_list = dict()
    with open(Datasetfile,'r') as f:
        for line in f.readlines():
            if ' ' in line:
                print "====================="
                print "File have space value"
                print "====================="
                #finish_string = str(pre_string).split()
                #value = 1
                s = ' '
                symbol_list[s] = 1
            for pun in string.punctuation:
                if pun in line:
                        print "======================"
                        print "File have symbol value"
                        print "======================"
                        symbol_list[pun] = 1
                        flag = flag + 1
    if len(symbol_list) > 1:
        print "File input error please check input file!!"
        sys.exit()
    symbol = symbol_list.keys()[0]
    return symbol
if __name__ =="__main__":
    get_Table = dict()
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    (options, args) = optparser.parse_args()
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = options.input
    else:
        print options.usage
        sys.exit('Bye bye see you baby <3')
    print "Now do pre process from file.........."
    get_symbol = CheckBetweenValue(inFile)
    get_Table = AnalyseInputFile(inFile,get_symbol)
    print get_Table

    



