import math
i=0
for i in range(0,345,15):
    a=math.sin(math.radians(i))
    b=math.cos(math.radians(i))
    print(round(a,4),round(b,4))
    
