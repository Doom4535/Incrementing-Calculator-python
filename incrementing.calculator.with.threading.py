import math # importing math functions
import thread # importing multithread support
import multiprocessing # another multithreading library

# i = 0.0000001 # amount to increment by
# e = 0.000001 # margin of error (absolute)
# z = 0 # starting angle in degrees
# s = 5 # stopping angle in degrees

def increment_f( id, i, e, z, s):

	f = math.atan(196 / (400 * (2.2 * math.cos(z) -1)))
	z = z / ( 360 ) * (2 * math.pi) # converting degree input to radians
	s = s / ( 360 ) * (2 * math.pi) # converting degree input to radians
	while (((abs(f - z)) >= e) and (e <= s )):
		print id, f, ' is not within ', e, ' radians of ', f
		z +=i
		f = math.atan(196 / (400 * (2.2 * math.cos(z) -1)))

	f = f / (2 * math.pi) * 360 # converting radians to degrees for the function output
	z = z / (2 * math.pi) * 360 # converting radians to degrees for the angle

	print 'Success, ', f, ' is close to ', z

try:
	thread.start_new_thread ( increment_f, ( thread-1, 0.0001, 0.001, 0, 5 ))
		# i = 0.0001
		# e = 0.001
		# z = 0
		# s = 5
		# id = thread-1
	
	thread.start_new_thread ( increment_f, ( thread-2, 0.0001, 0.001, 5, 9 ))
                # i = 0.0001
                # e = 0.001
                # z = 5
                # s = 9
		# id = thread-2
except:
	print 'Error: unable to start thread'


