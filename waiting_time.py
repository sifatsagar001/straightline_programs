import math
import stdio
import sys

l = float(sys.argv[1])
t = float(sys.argv[2])

p = math.e**(-l*t)
stdio.writeln(p)
