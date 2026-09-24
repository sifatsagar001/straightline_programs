import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

small = min(x,y,z) 
large = max(x, y, z)
mid = (x + y + z) - small - large

stdio.writeln(f"{small} {mid} {large}")
