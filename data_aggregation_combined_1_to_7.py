import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_1_to_2 = numpy.loadtxt('loaded_complete_data_1_to_2_2_sec.csv', delimiter=',')
loaded_complete_data_3_to_4 = numpy.loadtxt('loaded_complete_data_3_to_4_2_sec.csv', delimiter=',')
loaded_complete_data_5_to_6 = numpy.loadtxt('loaded_complete_data_5_to_6_2_sec.csv', delimiter=',')
loaded_complete_data_7 = numpy.loadtxt('loaded_complete_data_7_2_sec.csv', delimiter=',')

loaded_complete_data = numpy.concatenate((loaded_complete_data_1_to_2, loaded_complete_data_3_to_4, loaded_complete_data_5_to_6, loaded_complete_data_7), axis=0)	

numpy.savetxt('loaded_complete_data_2_sec.csv', loaded_complete_data, delimiter=',')	
