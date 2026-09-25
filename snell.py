import math
import stdio
import sys

t1 = math.radians(float(sys.argv[1]))
n1 = math.radians(float(sys.argv[2]))
n2 = math.radians(float(sys.argv[3]))

t2 = math.asin((math.sin(t1)*n1)/n2)
t2 = math.degrees(t2)
stdio.writeln(t2)
