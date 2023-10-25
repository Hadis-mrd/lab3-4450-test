""" Squares the input. """
import sys

if __name__=="__main__":
    assert(len(sys.argv)==2)
    num = int(sys.argv[1])
    print num ** 2
