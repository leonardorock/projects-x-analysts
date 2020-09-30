import numpy as np
import sys
import random
from ypstruct import structure

def run(problem, params):
    
    # Problem Information
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax

    # Parameters
    maxit = params.maxit
    npop = params.npop
    pc = params.pc
    nc = int(np.round(pc*npop/2)*2)
    gamma = params.gamma
    mu = params.mu

    # Empty Individual Template
    empty_individual = structure()
    empty_individual.analysts = None
    empty_individual.cost = None

    # Best Solution Ever Found
    bestsol = empty_individual.deepcopy()
    bestsol.cost = np.inf

    # Initialize Population
    pop = empty_individual.repeat(npop)
    for i in range(npop):
        pop[i].analysts = np.array(random.sample(range(varmin, varmax + 1), nvar))
        pop[i].cost = costfunc(pop[i].analysts)
        if pop[i].cost < bestsol.cost:
            bestsol = pop[i].deepcopy()

    # Best Cost of Iterations
    bestcost = np.empty(maxit)
    
    # Main Loop
    for it in range(maxit):

        # costs = np.array([x.cost for x in pop])
        # avg_cost = np.mean(costs)
        # if avg_cost != 0:
        #     costs = costs/avg_cost
        # probs = np.exp(-beta*costs)

        popc = []
        for _ in range(nc//2):

            # Select Parents
            q = np.random.permutation(npop)
            p1 = pop[q[0]]
            p2 = pop[q[1]]

            # Perform Roulette Wheel Selection
            # p1 = pop[roulette_wheel_selection(probs)]
            # p2 = pop[roulette_wheel_selection(probs)]
            
            # Perform Crossover
            c1, c2 = crossover(p1, p2, gamma)

            # Perform Mutation
            c1 = mutate(c1, mu, varmin, varmax)
            c2 = mutate(c2, mu, varmin, varmax)

            # Apply Bounds
            apply_bound(c1, varmin, varmax)
            apply_bound(c2, varmin, varmax)

            # Evaluate First Offspring
            c1.cost = costfunc(c1.analysts)
            if c1.cost < bestsol.cost:
                bestsol = c1.deepcopy()

            # Evaluate Second Offspring
            c2.cost = costfunc(c2.analysts)
            if c2.cost < bestsol.cost:
                bestsol = c2.deepcopy()

            # Add Offsprings to popc
            popc.append(c1)
            popc.append(c2)
        

        # Merge, Sort and Select
        pop += popc
        pop = sorted(pop, key=lambda x: x.cost)
        pop = pop[0:npop]

        # Store Best Cost
        bestcost[it] = bestsol.cost

        # Show Iteration Information
        print("Iteration {}: Best Cost = {}".format(it, bestcost[it]))

    # Output
    out = structure()
    out.pop = pop
    out.bestsol = bestsol
    out.bestcost = bestcost
    return out

def crossover(p1, p2, gamma=5):
    c1 = p1.deepcopy()
    c2 = p1.deepcopy()
    c1.analysts = np.append(p1.analysts[:gamma], p2.analysts[gamma:])
    c2.analysts = np.append(p2.analysts[:gamma], p1.analysts[gamma:])
    return c1, c2

def mutate(x, mu, varmin, varmax):
    y = x.deepcopy()
    flag = np.random.rand(*x.analysts.shape) <= mu
    ind = np.argwhere(flag)
    y.analysts[ind] = random.randint(varmin, varmax + 1)
    return y

def apply_bound(x, varmin, varmax):
    x.analysts = np.maximum(x.analysts, varmin)
    x.analysts = np.minimum(x.analysts, varmax)

def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
