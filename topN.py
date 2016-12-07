#!/usr/bin/python

import sys, getopt

number = 0
top = []
list = []

def returnList( list,n ):
    for line in list:
        if len(top) < int(n):
            if len(top) == 0:
               top.append(line)
               continue
            for item in top:
                if line == item:
                    continue
                else:
                    if len(top) == int(n):
                        continue
                    top.append(line)
        else:
          count = 0
          applied = 0
          for item in top:
              if line == item:
                 continue
              if applied == 1:
                  continue
              elif int(line) > int(item):
                  top[count] = line
                  applied = 1
              count += 1

def main(argv):
   inputfile = ""
   try:
      opts, args = getopt.getopt(argv,"hf:n:",["ifile=","number="])
   except getopt.GetoptError:
      print 'test.py -f <inputfile> -n <N>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -f <inputfile> -n <N>'
         sys.exit()
      elif opt in ("-f", "--ifile"):
         inputfile = arg
      elif opt in ("-n", "--number"):
         number = arg
   with open(inputfile) as f:
    for line in f:
        list.append(line)
   f.close()
   returnList(list,number)
   returnList(list,number)
   returnList(list,number)
   print top

if __name__ == "__main__":
   main(sys.argv[1:])
