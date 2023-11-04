import math

hypot = lambda a,b : math.sqrt(a * b + b * b)
hypot(3,4)
type(hypot)

to_seconds = lambda hours,minutes : (hours*3600) + (minutes*60)
to_seconds(3,20)

