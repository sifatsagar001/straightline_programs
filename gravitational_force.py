import stdio
import sys

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])**2

G = 6.674e-11

f= float(G*((m1*m2)/r))

stdio.writeln(f)