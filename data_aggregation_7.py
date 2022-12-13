import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_7_1 = numpy.loadtxt('decimated_input_data_with_labels_7_1_800_1800.csv', delimiter=',')
loaded_complete_data_7_2 = numpy.loadtxt('decimated_input_data_with_labels_7_2_800_1800.csv', delimiter=',')
loaded_complete_data_7_3 = numpy.loadtxt('decimated_input_data_with_labels_7_3_800_1800.csv', delimiter=',')
loaded_complete_data_7_4 = numpy.loadtxt('decimated_input_data_with_labels_7_4_800_1800.csv', delimiter=',')
loaded_complete_data_7_5 = numpy.loadtxt('decimated_input_data_with_labels_7_5_800_1800.csv', delimiter=',')

loaded_complete_data_7 = numpy.concatenate((loaded_complete_data_7_1, loaded_complete_data_7_2, loaded_complete_data_7_3, loaded_complete_data_7_4, loaded_complete_data_7_5), axis=0)	

numpy.savetxt('loaded_complete_data_7_2_sec.csv', loaded_complete_data_7, delimiter=',')	
