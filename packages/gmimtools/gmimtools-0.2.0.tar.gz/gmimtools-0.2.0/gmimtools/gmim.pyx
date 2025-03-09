""" A suite of codes to compute ground motion intensity measures (GMIMs) based on ground motion records.
"""

import numpy as np
cimport numpy as np
from scipy import integrate
import json
cimport cython
from libc.math cimport pi, pow, fabs, ceil

__author__ = 'A. Renmin Pretell Ductram'

#===================================================================================================
# Get max from an array of numbers
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef max_cy(double[:] values):
	cdef int Nvals = len(values)
	cdef int i
	cdef double max_val
	max_val = -999.
	for i in range(Nvals):
		if max_val < values[i]:
			max_val = values[i]
	return max_val

#===================================================================================================
# Sum
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef sum_cy(double[:] array_A):
	cdef int N_vals = len(array_A)
	cdef double sum_ = 0.
	cdef int i
	for i in range(N_vals):
		sum_ += array_A[i]
	return sum_

#===================================================================================================
# Absolute value of array
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef abs_cy(double[:] array_A):
	cdef int N = len(array_A)
	cdef double[:] array_B = np.zeros(N,dtype='float64')
	cdef int i
	for i in range(N):
		array_B[i] = fabs(array_A[i])
	return np.asarray(array_B)

#===================================================================================================
# Cythonized cumsum
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef cumsum_cy(double[:] array_A):
	cdef int N = len(array_A)
	cdef double[:] array_B = np.zeros(N,dtype='float64')
	cdef double tmp = 0.
	cdef int i
	for i in range(N):
		tmp += array_A[i]
		array_B[i] = tmp*1
	return np.asarray(array_B)

#===================================================================================================
# Power for an array
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef pow_array(double[:] array_A, double exponent):
	cdef N = len(array_A)
	cdef double[:] array_B = np.zeros(N,dtype='float64')
	cdef int i
	for i in range(N):
		array_B[i] = pow(array_A[i],exponent)
	return np.asarray(array_B)

#===================================================================================================
# Cythonized linspace
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef linspace_cy(double start, double stop, int N):
	cdef double[:] out_series = np.zeros(N,dtype='float64')
	cdef double step = (stop-start)/(N-1)
	cdef int i
	for i in range(N):
		out_series[i] = start+i*step
	return out_series

#===================================================================================================
# Get index, compare array to float
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_index(double[:] array_A, double value):
	cdef int N = len(array_A)
	cdef int i
	for i in range(N):
		if array_A[i] > value:
			return i
	return N

#===================================================================================================
# Peak ground acceleration (PGA)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_PGA_cy(double[:] accel):
	"""
	Parameter
	=========
	accel: Acceleration time series. 

	Returns
	=======
	PGA in same units as input.
	"""
	return max_cy(abs_cy(accel))

#===================================================================================================
# Peak ground velocity (PGV)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_PGV_cy(double[:] accel, double dt):
	"""
	Parameter
	=========
	accel: Acceleration time series in m/s**2.
	dt: Time step in s.

	Returns
	=======
	PGV in m/s.
	"""
	vel = integrate.cumulative_trapezoid(accel,dx=dt)
	return max_cy(abs_cy(vel))

#===================================================================================================
# Arias intensity (Ia) - Arias (1970)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_Ia_cy(double[:] accel, double dt):
	"""
	Parameter
	=========
	accel: Acceleration time series in m/s**2.
	dt: Time step in s.
	
	Returns
	=======
	Ia in m/s.
	"""
	a_sqr = pow_array(accel,2)
	Ia    = sum_cy(a_sqr)*dt*pi/2/9.81
	Ia_sc = cumsum_cy(a_sqr)*dt*pi/2/9.81
	return Ia,np.asarray(Ia_sc)

#===================================================================================================
# Arias intensity (Ia) times
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_Ia_times_cy(double[:] accel,double dt, double[:] percentages):
	"""
	Parameter
	=========
	accel: Acceleration time series in m/s**2.
	dt: Time step in s.
	percentages: Ia percentages at which to compute the times.

	Returns
	=======
	Ia times in s.
	"""
	cdef int N_acc = len(accel)
	cdef int N_per = len(percentages)
	cdef double[:] gmtime = linspace_cy(dt,dt*N_acc,N_acc)
	cdef double[:] Ia_times = np.zeros(N_per,dtype='float64')
	cdef double[:] Ia
	cdef int i

	Ia = pow_array(accel,2)
	Ia = cumsum_cy(Ia)*dt*pi/2/9.81
	for i in range(N_per):
		val  = percentages[i]*Ia[N_acc-1]
		indx = get_index(Ia,val)
		Ia_times[i] = gmtime[indx]

	return np.asarray(Ia_times)

#===================================================================================================
# Cumulative absolute velocity (CAV)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_CAV_cy(double[:] accel,double dt):
	"""
	Parameter
	=========
	accel: Acceleration time series.
	dt: Time step in s.

	Returns
	=======
	CAV in units consistent with input.
	"""
	return sum_cy(abs_cy(accel))*dt

#===================================================================================================
# Cumulative absolute velocity with acceleration threshold = "n" (e.g., n = 5 cm/s**2 for CAV_5)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_CAVn_cy(double[:] accel,double dt, double threshold):
	"""
	Parameter
	=========
	accel: Acceleration time series.
	dt: Time step in s.
	threshold: Acceleration threshold in same units as "accel."

	Returns
	=======
	CAV_n in units consistent with input.
	"""
	cdef int N_acc = len(accel)
	cdef double[:] abs_accel = np.zeros(N_acc,dtype='float64')

	abs_acc = abs_cy(accel)
	abs_acc[abs_acc < threshold] = 0
	
	return sum_cy(abs_acc)*dt

#===================================================================================================
# Standardized cumulative absolute velocity - Campbell and Bozorgnia (2011)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_CAVstd_cy(double[:] accel,double dt):

	"""
	Parameter
	=========
	accel: Acceleration time series in m/s**2.
	dt: Time step in s.

	Returns
	=======
	CAV_n in m/s.
	"""

	cdef int N_acc = len(accel)
	cdef int n_intervals = int(ceil(len(accel)*dt))
	cdef int n_steps_1sec = int(1/dt)
	cdef double pga_i
	cdef int i,j

	for i in range(n_intervals):
		pga_i = get_PGA_cy(accel[n_steps_1sec*i:n_steps_1sec*(i+1)])
		if pga_i < 0.025*9.81:
			accel[n_steps_1sec*i:n_steps_1sec*(i+1)] = 0

	return sum_cy(abs_cy(accel))*dt

#===================================================================================================
# Damage-potential CAV - Campbell and Bozorgnia (2011)
#===================================================================================================
def get_CAVdp_cy(double CAVstd_gm,double max_CAVstd,double max_PSA,double max_PSV,int PSV_check=1):
	"""
	Parameter
	=========
	CAVstd_gm: Geometric average CAVstd of the two horizontal components in m/s
	max_CAVstd: Maximum CAVstd of the three components in m/s
	max_PSA: Maximum PSA (2 - 10 Hz) of the the three horizontal components in m/s**2
	max_PSV: Maximum PSV (1 - 2 Hz) of the the three horizontal components in m/s
	PSV_check: Flag, to check (or not) for PSV threshold (default = 1)

	Returns
	=======
	CAVdp: Damage potential CAV in m/s
	"""

	cdef double PSA_cutoff    = 0.20 *9.81
	cdef double CAVstd_cutoff = 0.16*9.81
	cdef double PSV_cutoff    = 15.34/100

	if max_PSA>PSA_cutoff and max_CAVstd>CAVstd_cutoff:
		if PSV_check:
			if max_PSV>PSV_cutoff and max_CAVstd>CAVstd_cutoff:
				return CAVstd_gm
			else:
				return 0
		else:
			return CAVstd_gm
	else:
		return 0
