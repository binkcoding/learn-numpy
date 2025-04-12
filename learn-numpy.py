import numpy as np
from numpy import arange
from numpy import linspace
from numpy import eye
from numpy import random


#One dimensional array
sample_list = [1, 2, 3]

#Two dimensional array
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Arrange function
np.arange(1, 11, 2)
np.zeros(4)
np.ones(4)

#Linspace usage
np.linspace(0, 1, 10)

#Eye function
np.eye(4)

#Random
np.random.rand(5)

#Display all outputs
print(np.random.rand(4))
print(np.eye(4))
print(np.linspace(0, 1, 11))
print(np.ones(4))
print(np.zeros(4))
print(np.arange(1, 11, 2))
print(np.array(my_matrix))
print(np.array(sample_list))


