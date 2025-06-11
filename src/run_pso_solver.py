
import numpy as np
from deap import base, creator, tools, algorithms
import random
import matplotlib.pyplot as plt
import time

# Example problem setup: 5 jobs, 3 machines
PROCESSING_TIMES = np.array([
    [4, 5, 6],
    [7, 8, 9],
    [3, 2, 4],
    [6, 4, 3],
    [5, 7, 6]
])

NUM_JOBS = PROCESSING_TIMES.shape[0]
NUM_MACHINES = PROCESSING_TIMES.shape[1]

def evaluate(schedule):
    end_times = np.zeros((NUM_JOBS, NUM_MACHINES))
    for i, job in enumerate(schedule):
        for m in range(NUM_MACHINES):
            if m == 0:
                prev_job_time = end_times[schedule[i-1], m] if i > 0 else 0
                end_times[job, m] = prev_job_time + PROCESSING_TIMES[job][m]
            else:
                end_times[job, m] = max(end_times[job, m-1], end_times[schedule[i-1], m] if i > 0 else 0) + PROCESSING_TIMES[job][m]
    makespan = end_times[schedule[-1], -1]
    return makespan,

def run_pso(n_generations=30, pop_size=30):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(NUM_JOBS), NUM_JOBS)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxPartialyMatched)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)

    print("Running PSO-style GA for scheduling...")
    start_time = time.time()
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=n_generations,
                        stats=stats, halloffame=hof, verbose=True)
    end_time = time.time()

    print(f"Best schedule found: {hof[0]}")
    print(f"Best makespan: {hof[0].fitness.values[0]:.2f}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

    return hof[0], stats

if __name__ == "__main__":
    best, stats = run_pso()

    # Plot convergence
    gen = list(range(len(stats)))
    min_vals = stats.select("min")
    avg_vals = stats.select("avg")

    plt.plot(gen, min_vals, label="Min Makespan")
    plt.plot(gen, avg_vals, label="Avg Makespan")
    plt.xlabel("Generation")
    plt.ylabel("Makespan")
    plt.title("PSO Scheduling Convergence")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../results/pso_convergence.png")
    plt.show()
