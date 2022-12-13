import numpy
from tensorflow.random import set_seed
from numpy.random import seed

# setting the seed
seed(1)
set_seed(1)

loaded_complete_data_5_1 = numpy.loadtxt('decimated_input_data_with_labels_5_1_800_1800.csv', delimiter=',')
loaded_complete_data_5_2 = numpy.loadtxt('decimated_input_data_with_labels_5_2_800_1800.csv', delimiter=',')
loaded_complete_data_5_3 = numpy.loadtxt('decimated_input_data_with_labels_5_3_800_1800.csv', delimiter=',')
loaded_complete_data_5_4 = numpy.loadtxt('decimated_input_data_with_labels_5_4_800_1800.csv', delimiter=',')
loaded_complete_data_5_5 = numpy.loadtxt('decimated_input_data_with_labels_5_5_800_1800.csv', delimiter=',')

loaded_complete_data_6_1 = numpy.loadtxt('decimated_input_data_with_labels_6_1_800_1800.csv', delimiter=',')
loaded_complete_data_6_2 = numpy.loadtxt('decimated_input_data_with_labels_6_2_800_1800.csv', delimiter=',')
loaded_complete_data_6_3 = numpy.loadtxt('decimated_input_data_with_labels_6_3_800_1800.csv', delimiter=',')
loaded_complete_data_6_4 = numpy.loadtxt('decimated_input_data_with_labels_6_4_800_1800.csv', delimiter=',')
loaded_complete_data_6_5 = numpy.loadtxt('decimated_input_data_with_labels_6_5_800_1800.csv', delimiter=',')


loaded_complete_data_5_to_6 = numpy.concatenate((loaded_complete_data_5_1, loaded_complete_data_5_2, loaded_complete_data_5_3, loaded_complete_data_5_4, loaded_complete_data_5_5, loaded_complete_data_6_1, loaded_complete_data_6_2, loaded_complete_data_6_3, loaded_complete_data_6_4, loaded_complete_data_6_5), axis=0)	

numpy.savetxt('loaded_complete_data_5_to_6_2_sec.csv', loaded_complete_data_5_to_6, delimiter=',')	
