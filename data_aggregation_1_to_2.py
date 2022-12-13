import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_1_1 = numpy.loadtxt('decimated_input_data_with_labels_1_1_800_1800.csv', delimiter=',')
loaded_complete_data_1_2 = numpy.loadtxt('decimated_input_data_with_labels_1_2_800_1800.csv', delimiter=',')

loaded_complete_data_2 = numpy.loadtxt('decimated_input_data_with_labels_2_800_1800.csv', delimiter=',')

loaded_complete_data_1_to_2 = numpy.concatenate((loaded_complete_data_1_1, loaded_complete_data_1_2, loaded_complete_data_2), axis=0)	

numpy.savetxt('loaded_complete_data_1_to_2_2_sec.csv', loaded_complete_data_1_to_2, delimiter=',')	
