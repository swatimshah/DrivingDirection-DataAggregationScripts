import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_8 = numpy.loadtxt('loaded_complete_data_8_2_sec.csv', delimiter=',')
loaded_complete_data_9 = numpy.loadtxt('loaded_complete_data_9_2_sec.csv', delimiter=',')
loaded_complete_data_10 = numpy.loadtxt('loaded_complete_data_10_2_sec.csv', delimiter=',')

loaded_complete_unseen_data = numpy.concatenate((loaded_complete_data_8, loaded_complete_data_9, loaded_complete_data_10), axis=0)	

numpy.savetxt('loaded_complete_unseen_data_2_sec.csv', loaded_complete_unseen_data, delimiter=',')	
