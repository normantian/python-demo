def foo(*args): # just use "*" to collect all remaining arguments into a tuple
    numargs = len(args)
    print "Number of arguments: {0}".format(numargs)
    for i, x in enumerate(args):
        print "Argument {0} is: {1}".format(i,x)
