import numpy as np
from ypstruct import structure
import random

individual = structure()
individual.analysts = np.array(random.sample(range(1, 16), 9))
individual.cost = None

def mutate(x, mu):
    y = x.deepcopy()
    flag = np.random.rand(*x.analysts.shape) <= mu
    ind = np.argwhere(flag)
    y.analysts[ind] = random.randint(1, 16)
    return y

i = 0
print(individual)
mutated = individual.deepcopy()
while((mutated.analysts==individual.analysts).all()):
    mutated = mutate(individual, 0.01)
    i += 1


print(mutated)
print(i)