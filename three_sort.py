import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

min = min(x,y,z) 
max = max(x, y, z)
mid = (min + max) - (x + y + z) 

stdio.writeln(f"{min} {mid} {max})
