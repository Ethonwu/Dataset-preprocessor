#!/usr/bin/env python
import sys
from optparse import OptionParser
def AnalyseInputFile(inputFile):
    with open(inputFile,'r') as f:
        for line in f.readlines():
            l = str(line.strip('\n'))
            print "GO:" + l ,len(l)
            if ' ' in l == True:
                print "Haha"
            #l = str(line.strip('\n')).split()
if __name__ =="__main__":
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
    AnalyseInputFile(inFile)
