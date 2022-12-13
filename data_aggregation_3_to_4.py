import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_3_1 = numpy.loadtxt('decimated_input_data_with_labels_3_1_800_1800.csv', delimiter=',')
loaded_complete_data_3_2 = numpy.loadtxt('decimated_input_data_with_labels_3_2_800_1800.csv', delimiter=',')
loaded_complete_data_3_3 = numpy.loadtxt('decimated_input_data_with_labels_3_3_800_1800.csv', delimiter=',')

loaded_complete_data_4_1 = numpy.loadtxt('decimated_input_data_with_labels_4_1_800_1800.csv', delimiter=',')
loaded_complete_data_4_2 = numpy.loadtxt('decimated_input_data_with_labels_4_2_800_1800.csv', delimiter=',')
loaded_complete_data_4_3 = numpy.loadtxt('decimated_input_data_with_labels_4_3_800_1800.csv', delimiter=',')
loaded_complete_data_4_4 = numpy.loadtxt('decimated_input_data_with_labels_4_4_800_1800.csv', delimiter=',')


loaded_complete_data_3_to_4 = numpy.concatenate((loaded_complete_data_3_1, loaded_complete_data_3_2, loaded_complete_data_3_3, loaded_complete_data_4_1, loaded_complete_data_4_2, loaded_complete_data_4_3, loaded_complete_data_4_4), axis=0)	

numpy.savetxt('loaded_complete_data_3_to_4_2_sec.csv', loaded_complete_data_3_to_4, delimiter=',')	
