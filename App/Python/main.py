import random
import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import ga

costs = np.array([200, 100, 400, 500, 120, 220, 300, 600, 700, 230, 450, 310, 420, 180, 530])
# costs = np.array(random.sample(range(400, 2500), 15))

print(costs)
# Sphere Test Function
def project_cost(analysts):
    cost = 0
    for analyst in analysts:
        cost += costs[analyst-1]
    
    factor = len(analysts) - len(set(analysts))
    cost *= pow(1 + factor, factor)
    return cost

# Problem Definition
problem = structure()
problem.costfunc = project_cost
problem.nvar = 9
problem.varmin = 1
problem.varmax = 15

# GA Parameters
params = structure()
params.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 5
params.mu = 0.01

# Run GA
out = ga.run(problem, params)

print(out.bestsol)

# Results
plt.plot(out.bestcost)
# plt.semilogy(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm (GA)')
plt.grid(True)
plt.show()

