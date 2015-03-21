import math

i = 0.0000001 # amount to increment by
e = 0.000001 # margin of error (absolute)
z = 0 # starting angle or desired value
f = math.atan(196 / (400 * (2.2 * math.cos(z) -1)))

while (abs(f - z) >= e):
	# print f, ' is not within ', e, ' radians of ', f
	z +=i
	f = math.atan(196 / (400 * (2.2 * math.cos(z) -1)))

f = f / (2 * math.pi) * 360 # converting radians to degrees for the function output
z = z / (2 * math.pi) * 360 # converting radians to degrees for the angle

print 'Success, ', f, ' is close to ', z
