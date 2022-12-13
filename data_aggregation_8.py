import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_8_1 = numpy.loadtxt('decimated_input_data_with_labels_8_1_800_1800.csv', delimiter=',')
loaded_complete_data_8_2 = numpy.loadtxt('decimated_input_data_with_labels_8_2_800_1800.csv', delimiter=',')

loaded_complete_data_8 = numpy.concatenate((loaded_complete_data_8_1, loaded_complete_data_8_2), axis=0)	

numpy.savetxt('loaded_complete_data_8_2_sec.csv', loaded_complete_data_8, delimiter=',')	
