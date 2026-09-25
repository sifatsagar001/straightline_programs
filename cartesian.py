import math
import stdio
import sys

r = float(sys.argv[1])
t_degree = float(sys.argv[2])
t = math.radians(t_degree)

x = r * math.cos(t)
y = r * math.sin(t)
stdio.writeln(f"{x} {y}")
