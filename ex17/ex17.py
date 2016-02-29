from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying form %s to %s" %(from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indate = infile.read()

print "The input file is %d bytes long" % len(data)
