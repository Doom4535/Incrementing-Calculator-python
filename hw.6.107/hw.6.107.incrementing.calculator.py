import math

# initial value of d
d = 0.5
# setting the result to be something guarenteed to be bigger than d
r = abs( 2 * d )
# Defining function
f = 36 * d **4 - 36 * d **3 - 26 * d **2 + 36 * d - 9
# Looping variable
s = True
# Size of increments
d_incr = 0.000001
d_de_incr = d_incr / 2
# used to keep track of fails to successes (to determine when to break the loop).
f = 0
# used to count fails
c = 1
m = 100 # number of failures allowed before finishing

while (s == True):
	if (f <= 0.0001 or f >= -0.0001 ):
		if (d < r and d > 0):
			print 'Success, ', d, ' is a possible solution.'
			r = d
			d = d + d_incr
			f = f - 1
			d_incr = d_incr * 0.8
		else:
			print 'We already have a better solution than ', d, ' .'	
			d = d - d_de_incr
			f += 1
			f = f * c #  Controls the weighted value of successful f values where the d value is still greater than the established r
	else:
		print 'Fail, ', d, ' is not a possible solution.'
		d = d + d_incr
		f = f + 1
	print 'Fail count: ', f
	if (c > m):
		s = False

