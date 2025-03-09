# -*- coding: utf-8 -*-
""" A suite of ground motion intensity measure tools.
"""

import numpy as np
import pandas as pd

__author__ = 'A. Renmin Pretell Ductram'

#===================================================================================================
# Read *.AT2
#===================================================================================================
def read_AT2(file,scaling,Nskip=4):
	"""
	Parameter
	=========
	file: File name including extension ".AT2"
	scaling: A scaling factor, e.g., to convert from g to m/s**2
	Nskip: Number of rows to skip (default = 4)
	
	Returns
	=======
	accel: Array of accelerations. 
	dt: Time step.
	"""
	data = pd.read_csv(file,delimiter=',',header=None,skiprows=Nskip-1,nrows=1,engine='python').values[0]
	dt   = data[1].split('DT=')[1]
	
	try:
		dt = float(dt.split('SEC')[0])
	except:
		pass
	
	data  = pd.read_csv(file,sep='\\s+',engine='python',header=None,skiprows=Nskip)
	data  = data.to_numpy()
	
	[h_dim, w_dim]= np.shape(data)
	
	accel = data.reshape(h_dim*w_dim,1)
	accel = np.asarray(accel, dtype = np.float64)
	accel = np.concatenate(accel)
	accel = accel[~np.isnan(accel)]
	accel = scaling*accel

	return accel, dt
