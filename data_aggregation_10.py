import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_10_1 = numpy.loadtxt('decimated_input_data_with_labels_10_1_800_1800.csv', delimiter=',')
loaded_complete_data_10_2 = numpy.loadtxt('decimated_input_data_with_labels_10_2_800_1800.csv', delimiter=',')
loaded_complete_data_10_3 = numpy.loadtxt('decimated_input_data_with_labels_10_3_800_1800.csv', delimiter=',')
loaded_complete_data_10_4 = numpy.loadtxt('decimated_input_data_with_labels_10_4_800_1800.csv', delimiter=',')
loaded_complete_data_10_5 = numpy.loadtxt('decimated_input_data_with_labels_10_5_800_1800.csv', delimiter=',')
loaded_complete_data_10_6 = numpy.loadtxt('decimated_input_data_with_labels_10_6_800_1800.csv', delimiter=',')

loaded_complete_data_10 = numpy.concatenate((loaded_complete_data_10_1, loaded_complete_data_10_2, loaded_complete_data_10_3, loaded_complete_data_10_4, loaded_complete_data_10_5, loaded_complete_data_10_6), axis=0)	

numpy.savetxt('loaded_complete_data_10_2_sec.csv', loaded_complete_data_10, delimiter=',')	
