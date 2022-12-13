import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_9_1 = numpy.loadtxt('decimated_input_data_with_labels_9_1_800_1800.csv', delimiter=',')
loaded_complete_data_9_2 = numpy.loadtxt('decimated_input_data_with_labels_9_2_800_1800.csv', delimiter=',')
loaded_complete_data_9_3 = numpy.loadtxt('decimated_input_data_with_labels_9_3_800_1800.csv', delimiter=',')
loaded_complete_data_9_4 = numpy.loadtxt('decimated_input_data_with_labels_9_4_800_1800.csv', delimiter=',')
loaded_complete_data_9_5 = numpy.loadtxt('decimated_input_data_with_labels_9_5_800_1800.csv', delimiter=',')
loaded_complete_data_9_6 = numpy.loadtxt('decimated_input_data_with_labels_9_6_800_1800.csv', delimiter=',')

loaded_complete_data_9 = numpy.concatenate((loaded_complete_data_9_1, loaded_complete_data_9_2, loaded_complete_data_9_3, loaded_complete_data_9_4, loaded_complete_data_9_5, loaded_complete_data_9_6), axis=0)	

numpy.savetxt('loaded_complete_data_9_2_sec.csv', loaded_complete_data_9, delimiter=',')	
