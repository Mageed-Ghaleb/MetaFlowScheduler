
import numpy as np
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
    return end_times[schedule[-1], -1]

def generate_neighbors(schedule):
    neighbors = []
    for i in range(len(schedule)):
        for j in range(i+1, len(schedule)):
            neighbor = schedule[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def tabu_search(max_iters=100, tabu_size=20):
    current = list(range(NUM_JOBS))
    random.shuffle(current)
    best = current[:]
    best_cost = evaluate(best)
    tabu_list = []

    costs = []

    print("Running Tabu Search for scheduling...")
    start_time = time.time()

    for it in range(max_iters):
        neighbors = generate_neighbors(current)
        neighbors = [n for n in neighbors if n not in tabu_list]

        if not neighbors:
            break

        neighbor_costs = [(evaluate(n), n) for n in neighbors]
        neighbor_costs.sort()
        best_neighbor_cost, best_neighbor = neighbor_costs[0]

        current = best_neighbor
        if best_neighbor_cost < best_cost:
            best = best_neighbor[:]
            best_cost = best_neighbor_cost

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        costs.append(best_cost)

        print(f"Iteration {it+1}: Best Makespan = {best_cost:.2f}")

    end_time = time.time()
    print(f"Final best schedule: {best}")
    print(f"Final best makespan: {best_cost:.2f}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

    return best, costs

if __name__ == "__main__":
    best, costs = tabu_search()

    plt.plot(costs, label="Tabu Search Makespan")
    plt.xlabel("Iteration")
    plt.ylabel("Makespan")
    plt.title("Tabu Search Convergence")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../results/tabu_convergence.png")
    plt.show()
