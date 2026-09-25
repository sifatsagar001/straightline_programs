import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
if ((x + y) >= z) and ((x + z) >= y) and ((y + z) >= x):
    stdio.writeln("True")
else:
    stdio.writeln("False")